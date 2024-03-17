"""
Modelo que representa un post en el blog
"""
from django.db import models
from django.conf import settings
from django.db.models import QuerySet
from django.urls import reverse
from django.utils.text import slugify
from taggit.managers import TaggableManager

from tinymce.models import HTMLField

from apps.core.models import TimeStampedModel


class PublishedManager(models.Manager):
    """
    Manager que devuelve los posts con status 'published'
    """
    def get_queryset(self) -> QuerySet:
        """
        Devuelve los posts con status 'published'
        :return: QuerySet[Post]
        """
        return super().get_queryset().filter(status=Post.Status.PUBLISHED)


class Post(TimeStampedModel):
    """
    Modelo que representa un post en el blog
    """

    class Status(models.TextChoices):
        PUBLISHED = 'PB', 'Published'
        DRAFT = 'DR', 'Draft'

    title = models.CharField(max_length=250)

    slug = models.SlugField(max_length=255,
                            unique_for_date='published_at')

    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE,
                               related_name='blog_posts')

    content = models.TextField()

    cover_image = models.URLField(max_length=255, blank=True, null=True)

    published_at = models.DateTimeField(auto_now_add=True)

    status = models.CharField(max_length=2,
                              choices=Status.choices,
                              default=Status.DRAFT)

    content2 = HTMLField(blank=True, null=True)

    # Managers
    objects = models.Manager()
    published = PublishedManager()
    tags = TaggableManager()

    class Meta:
        ordering = ('-published_at',)
        indexes = (
            models.Index(fields=('slug', 'published_at')),
        )

    def get_absolute_url(self) -> str:
        """
        Devuelve la URL absoluta del post
        :return: str
        """
        return reverse(
            # URL namespace
            'blog:post-detail',
            # URL args
            args=[
                self.published_at.year,
                self.published_at.month,
                self.published_at.day,
                self.slug
            ]
        )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.title

"""
Archivo de configuración de la interfaz de administración de Django para la app blog.
"""
from django.contrib import admin
from django.db.models import QuerySet
from django.http import HttpRequest

from apps.blog.models.post_model import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """
    Configuración de la interfaz de administración de Post
    """
    list_display = ['title', 'slug', 'author', 'published_at', 'status', 'tag_list']
    list_filter = ['status', 'created_at', 'published_at', 'author']
    search_fields = ['title', 'body']
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ['author']
    date_hierarchy = 'published_at'
    ordering = ['status', 'published_at']

    def get_queryset(self, request: HttpRequest) -> QuerySet[Post]:
        return super().get_queryset(request).prefetch_related('tags')

    def tag_list(self, obj):
        """
        Devuelve la lista de tags del post
        :param obj:
        :return: LiteralString
        """
        return u", ".join(o.name for o in obj.tags.all())

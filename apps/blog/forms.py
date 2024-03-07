"""
Archivo para el manejo de formularios de la app blog
"""
from typing import List

from django import forms
from django.contrib.auth.models import User
from django.core.files.uploadedfile import InMemoryUploadedFile

from taggit.models import Tag

from .models.post_model import Post


class PostForm(forms.ModelForm):
    """
    Formulario para el modelo Post
    """
    image_file = None

    class Meta:
        """
        Clase Meta para el formulario PostForm
        """
        model = Post
        fields = ['title', 'content', 'cover_image']
        error_messages = {
            'title': {
                'required': 'Este campo es requerido'
            },
            'content': {
                'required': 'Este campo es requerido'
            },
        }

    cover_image = forms.FileField(required=False, allow_empty_file=True)
    tags = forms.CharField(required=False)

    def is_valid(self):
        """
        Validar el formulario
        :return: bool
        """
        valid = super().is_valid()
        print(f'{valid=}')
        print(f'{self.errors=}')
        if not valid:
            if 'cover_image' in self.errors:
                del self.errors['cover_image']
                valid = super().is_valid()
            self.cleaned_data['cover_image'] = self.image_file
        return valid

    def save(self, author: User = None, commit=True, *args, **kwargs) -> Post:
        """
        Guardar el formulario
        :param author: Instancia de User
        :param commit: bool
        :return: Post
        """
        post: Post = super().save(commit=False)
        post.cover_image = ''
        tags: List[str] | None = self.cleaned_data.get('tags')
        # print('tags', self.cleaned_data)
        if author:
            post.author = author
            post.save()
        if tags:
            post.tags.add(*tags)
        return post

    def clean_tags(self):
        """
        Validar el campo tags
        :return: list | None
        """
        valid_tags: list[str] | None = None
        tags: str | None = self.cleaned_data.get('tags')
        if tags:
            tags_list: list[str] = list(map(lambda tag: tag.strip(), tags.split(',')))
            all_tags = Tag.objects.all()
            valid_tags = [tag.name for tag in all_tags if tag.name in tags_list]

            # print('tags_list', valid_tags)
        return valid_tags

    def clean_cover_image(self):
        """
        Validar el campo cover_image
        :return: InMemoryUploadedFile | None
        """
        cover_image: InMemoryUploadedFile | None = self.cleaned_data.get('cover_image')
        # print('cover_image', cover_image, type(cover_image))
        if cover_image:
            self.image_file = cover_image
        return cover_image

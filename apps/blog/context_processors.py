"""
Context processors for the blog app
"""
from django.http import HttpRequest
from taggit.models import Tag


def tags_processor(request: HttpRequest) -> dict:
    """
    Procesador de contexto que devuelve el listado de tags
    :param request: HttpRequest
    :return: dict
    """
    return {
        'tags': Tag.objects.all()
    }

"""
Módulo que contiene la clase abstracta TimeStampedModel
"""
from django.db import models


class TimeStampedModel(models.Model):
    """
    Clase abstracta que proporciona auto-actualización
    """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

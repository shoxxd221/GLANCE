from django.db import models


class Category(models.Model):
    """Модель категории"""
    name = models.CharField(
        max_length=255,
        verbose_name='Название категории'
    )

from django.db import models

from .constants import DEFAULT_MAX_LENGTH


class Category(models.Model):
    """Модель категории"""
    name = models.CharField(
        max_length=DEFAULT_MAX_LENGTH,
        verbose_name='Название категории'
    )

    def __str__(self):
        return self.name


class Goods(models.Model):
    """Модель товара"""
    name = models.CharField(
        max_length=DEFAULT_MAX_LENGTH,
        verbose_name='Название товара'
    )
    price = models.PositiveSmallIntegerField(
        verbose_name='Стоимость товара в BYN'
    )
    description = models.TextField(
        verbose_name='Описание товара'
    )
    category = models.ForeignKey(
        to=Category,
        on_delete=models.CASCADE,
        verbose_name='Категория товара'
    )
    characteristics = models.JSONField(
        null=True,
        blank=True
    )
    quantity = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.name

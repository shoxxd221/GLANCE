from django.db import models


class Category(models.Model):
    """Модель категории"""
    name = models.CharField(
        max_length=255,
        verbose_name='Название категории'
    )

    def __str__(self):
        return self.name


class Goods(models.Model):
    """Модель товара"""
    name = models.CharField(
        max_length=255,
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

    def __str__(self):
        return self.name

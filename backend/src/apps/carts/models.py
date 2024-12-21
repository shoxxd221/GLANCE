from django.db import models
from django.contrib.auth import get_user_model

from apps.goods.models import Goods


class Cart(models.Model):
    """Модель корзины"""
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        verbose_name='Пользователь, которому соответсвует товар в корзине',
        unique=True
    )
    goods = models.ManyToManyField(
        Goods,
        verbose_name='Товары в коризине'
    )

    class Meta:
        ordering = ['user']
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'

    def __str__(self):
        return f'Корзина пользователя {self.user.name} с товарами {self.goods}'

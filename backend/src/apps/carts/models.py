from django.db import models
from django.contrib.auth import get_user_model

from apps.goods.models import Goods


class Cart(models.Model):
    """Модель корзины"""
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        verbose_name='Пользователь, которому соответсвует товар в корзине'
    )
    goods = models.ForeignKey(
        Goods,
        on_delete=models.CASCADE,
        verbose_name=
        'Товар, который пользователь добавил в корзину'
    )
    quantity = models.PositiveSmallIntegerField()

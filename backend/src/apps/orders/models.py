from django.db import models
from django.contrib.auth import get_user_model

from apps.goods.models import Goods
from apps.constants import DEFAULT_MAX_LENGTH


class Order(models.Model):
    """Модель заказов"""
    user = models.ForeignKey(
        to=get_user_model(),
        on_delete=models.CASCADE,
        verbose_name='Пользователь',
    )
    goods = models.ManyToManyField(
        to=Goods,
        verbose_name='Товары'
    )
    total_price = models.PositiveSmallIntegerField(
        verbose_name='Общая стоимость'
    )
    delivery_address = models.CharField(
        max_length=DEFAULT_MAX_LENGTH,
        verbose_name='Адрес доставки'
    )

    class Meta:
        ordering = ['total_price']
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f'Заказ пользователя {self.user.name} с общей стоимостью {self.total_price}'

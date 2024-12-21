from django.contrib.auth.models import AbstractUser
from django.db import models

from apps.constants import DEFAULT_MAX_LENGTH, PHONE_NUMBER_LENGTH


class User(AbstractUser):
    """Модель пользователя"""
    full_name = models.CharField(
        max_length=DEFAULT_MAX_LENGTH,
        verbose_name='ФИО',
        blank=True,
        null=True
    )
    phone_number = models.CharField(
        max_length=PHONE_NUMBER_LENGTH,
        verbose_name='Номер телефона'
    )

    class Meta:
        ordering = ['full_name']
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username

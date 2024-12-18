from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Модель пользователя"""
    full_name = models.CharField(
        max_length=255,
        verbose_name='ФИО',
        blank=True,
        null=True
    )
    phone_number = models.CharField(
        max_length=14,
        verbose_name='Номер телефона',
        unique=True
    )

    class Meta:
        ordering = ['full_name']
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username

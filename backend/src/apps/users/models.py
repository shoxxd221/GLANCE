from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Модель пользователя"""
    full_name = models.CharField(
        max_length=255,
        verbose_name='ФИО'
    )
    phone_number = models.CharField(
        max_length=14,
        verbose_name='Номер телефона'
    )

    def __str__(self):
        return self.username

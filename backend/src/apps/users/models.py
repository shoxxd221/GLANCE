from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    avatar = models.ImageField(
        verbose_name='Аватар',
        upload_to='images/',
        blank=True,
        null=True,
    )
    bio = models.TextField()
    website = models.URLField(
        verbose_name='Веб-сайт'
    )
    facebook = models.URLField(
        verbose_name='Фейсбук'
    )
    twitter = models.URLField(
        verbose_name='Твиттер'
    )
    instagram = models.URLField(
        verbose_name='Инстаграм'
    )

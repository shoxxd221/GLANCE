from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    avatar = models.ImageField(
        verbose_name='Avatar',
        upload_to='images/',
        blank=True,
        null=True,
    )
    bio = models.TextField()
    website = models.URLField(
        verbose_name='Web-site'
    )
    facebook = models.URLField(
        verbose_name='Facebook'
    )
    twitter = models.URLField(
        verbose_name='Twitter'
    )
    instagram = models.URLField(
        verbose_name='Instagram'
    )

    def __str__(self):
        return self.username

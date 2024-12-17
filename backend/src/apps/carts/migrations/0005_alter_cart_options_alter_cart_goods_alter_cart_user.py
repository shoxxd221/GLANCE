# Generated by Django 5.0.6 on 2024-12-17 22:05

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0004_remove_cart_quantity'),
        ('goods', '0002_alter_category_options_alter_goods_options_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cart',
            options={'ordering': ['user'], 'verbose_name': 'Корзина', 'verbose_name_plural': 'Корзины'},
        ),
        migrations.AlterField(
            model_name='cart',
            name='goods',
            field=models.ManyToManyField(to='goods.goods', verbose_name='Товары в коризине'),
        ),
        migrations.AlterField(
            model_name='cart',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, unique=True, verbose_name='Пользователь, которому соответсвует товар в корзине'),
        ),
    ]
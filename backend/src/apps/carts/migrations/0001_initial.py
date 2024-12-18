# Generated by Django 5.0.6 on 2024-12-15 21:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('goods', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveSmallIntegerField(verbose_name='Количество товара в заказе')),
                ('goods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.goods', verbose_name='Товар, который пользователь добавил в корзину')),
            ],
        ),
    ]

from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from apps.carts.models import Cart
from apps.goods.models import Goods


class CartSerializer(serializers.ModelSerializer):
    """Сериализатор корзины"""

    class Meta:
        model = Cart
        fields = ['id', 'user', 'goods']
        read_only_fields = ['user']

    def create(self, validated_data):
        """Создание корзины"""
        goods = validated_data.pop('goods')
        cart = Cart.objects.create(
            user=self.context['request'].user,
        )

        for good in goods:
            try:
                Goods.objects.get(id=good.pk)
            except Goods.DoesNotExist:
                raise ValidationError(f'Товар с id {good.pk} не существует')

            cart.goods.add(good.pk)

        return cart

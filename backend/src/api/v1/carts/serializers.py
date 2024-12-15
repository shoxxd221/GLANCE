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
        goods_ids = validated_data.pop('goods')

        cart = Cart.objects.create(
            user=self.context['request'].user,
        )

        for goods_id in goods_ids:
            try:
                goods = Goods.objects.get(id=goods_id)
            except Goods.DoesNotExist:
                raise ValidationError(f'Товар с id {goods_id} не существует')

            cart.goods.add(goods)

        return cart

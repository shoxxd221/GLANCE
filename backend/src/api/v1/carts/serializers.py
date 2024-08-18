from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer

from apps.carts.models import Cart
from apps.goods.models import Goods

from api.v1.goods.serializers import GoodsSerializer


class CartSerializer(ModelSerializer):
    """Серриализатор корзины"""
    goods = GoodsSerializer(read_only=True)
    goods_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Cart
        fields = ['id', 'goods', 'goods_id']
        read_only_fields = ['id', 'goods']

    def create(self, validated_data):
        """Создание корзины"""
        goods_id = validated_data.pop('goods_id')
        try:
            goods = Goods.objects.get(id=goods_id)
        except Goods.DoesNotExist:
            raise ValidationError(f'Товар с id {goods_id} не существует')
        if goods.quantity <= 0:
            raise ValidationError(f'Товара с id {goods_id} нет на складе')
        cart = Cart.objects.create(user=self.context['request'].user, goods=goods)
        return cart

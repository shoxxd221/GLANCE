from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from apps.orders.models import Order
from apps.goods.models import Goods


class OrderSerializer(serializers.ModelSerializer):
    """Сериализатор заказов"""

    class Meta:
        model = Order
        fields = '__all__'
        read_only_fields = ['user', 'total_price']

    def create(self, validated_data):
        """Создание заказа"""
        goods = validated_data.pop('goods')

        order = Order.objects.create(
            user=self.context['request'].user,
            delivery_address=self.validated_data.pop('delivery_address'),
            total_price=sum(good.price for good in goods)
        )

        for good in goods:
            try:
                Goods.objects.get(id=good.pk)
            except Goods.DoesNotExist:
                raise ValidationError(f'Товар с id {good.pk} не существует')

            order.goods.add(good.pk)

        return order

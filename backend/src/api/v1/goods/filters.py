import django_filters.rest_framework as filters
from django.db.models import Q

from apps.goods.models import Goods, Category


class GoodsFilter(filters.FilterSet):
    """FilterSet товаров"""
    min_price = filters.NumberFilter(
        field_name="price",
        lookup_expr='gte'
    )
    max_price = filters.NumberFilter(
        field_name="price",
        lookup_expr='lte'
    )
    category = filters.ModelChoiceFilter(
        queryset=Category.objects.all()
    )
    characteristics = filters.CharFilter(
        method='filter_by_characteristics'
    )

    class Meta:
        model = Goods
        fields = ['name', 'price']

    def filter_by_characteristics(self, queryset, name, value):
        """ Фильтрует товары по указанным характеристикам."""
        import json
        characteristics = json.loads(value)
        q_filters = Q()
        for key, val in characteristics.items():
            q_filters &= Q(characteristics__contains={key: val})
        return queryset.filter(q_filters)

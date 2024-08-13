from rest_framework.serializers import ModelSerializer

from apps.goods.models import Category


class CategorySerializer(ModelSerializer):
    """Серриализатор для категорий"""
    class Meta:
        model = Category
        fields = '__all__'
        read_only_fields = ['id']

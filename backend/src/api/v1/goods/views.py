from rest_framework import viewsets

from apps.goods.models import Category, Goods

from api.v1.goods.serializers import CategorySerializer, GoodsSerializer
from api.v1.goods.permissions import IsSuperuserOrStaffOrReadOnly
from api.v1.goods.filters import GoodsFilter


class CategoryViewSet(viewsets.ModelViewSet):
    """Viewset для категорий"""
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsSuperuserOrStaffOrReadOnly, )
    http_method_names = ('get', 'post', 'patch', 'delete')


class GoodsViewSet(viewsets.ModelViewSet):
    """Viewset для товаров"""
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    permission_classes = (IsSuperuserOrStaffOrReadOnly, )
    http_method_names = ('get', 'post', 'patch', 'delete')
    filterset_class = GoodsFilter
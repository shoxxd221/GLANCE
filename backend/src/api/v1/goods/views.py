from api.v1.cached_viewset import CachedViewSet
from apps.goods.models import Category, Goods

from api.v1.goods.serializers import CategorySerializer, GoodsSerializer
from api.v1.goods.permissions import IsSuperuserOrStaffOrReadOnly
from api.v1.goods.filters import GoodsFilter


class CategoryViewSet(CachedViewSet):
    """Viewset для категорий"""
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsSuperuserOrStaffOrReadOnly, )
    http_method_names = ('get', 'post', 'patch', 'delete')


class GoodsViewSet(CachedViewSet):
    """Viewset для товаров"""
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    permission_classes = (IsSuperuserOrStaffOrReadOnly, )
    http_method_names = ('get', 'post', 'patch', 'delete')
    filterset_class = GoodsFilter

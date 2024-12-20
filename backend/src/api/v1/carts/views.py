from rest_framework.permissions import IsAuthenticated

from api.v1.base_viewsets import PermissionViewSet
from apps.carts.models import Cart

from api.v1.carts.serializers import CartSerializer


class CartViewSet(PermissionViewSet):
    """Viewset для корзины пользователя"""
    queryset = Cart.objects.prefetch_related('goods').all()
    serializer_class = CartSerializer
    permission_classes = (IsAuthenticated, )
    http_method_names = ('get', 'post', 'patch', 'delete')

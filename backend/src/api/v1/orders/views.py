from rest_framework.permissions import IsAuthenticated

from api.v1.base_viewsets import PermissionViewSet
from apps.orders.models import Order

from api.v1.orders.serializers import OrderSerializer


class OrderViewSet(PermissionViewSet):
    """Viewset для корзины пользователя"""
    queryset = Order.objects.prefetch_related('goods').all()
    serializer_class = OrderSerializer
    permission_classes = (IsAuthenticated, )
    http_method_names = ('get', 'post', 'patch', 'delete')

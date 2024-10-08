from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import DestroyModelMixin, ListModelMixin, CreateModelMixin
from rest_framework.permissions import IsAuthenticated

from apps.carts.models import Cart

from api.v1.carts.serializers import CartSerializer


class CartViewSet(
    DestroyModelMixin,
    ListModelMixin,
    CreateModelMixin,
    GenericViewSet
):
    """Viewset для корзины пользователя"""
    queryset = Cart.objects.select_related('goods').all()
    serializer_class = CartSerializer
    permission_classes = (IsAuthenticated, )
    http_method_names = ('get', 'post', 'delete')

    def get_queryset(self):
        """Получение корзины определенного пользователя"""
        return self.queryset.filter(user=self.request.user)

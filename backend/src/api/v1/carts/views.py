from rest_framework.permissions import IsAuthenticated

from api.v1.cached_viewset import CachedViewSet
from apps.carts.models import Cart

from api.v1.carts.serializers import CartSerializer


class CartViewSet(CachedViewSet):
    """Viewset для корзины пользователя"""
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = (IsAuthenticated, )
    http_method_names = ('get', 'post', 'patch', 'delete')

    def get_queryset(self):
        """Получение корзины определенного пользователя"""
        return self.queryset.filter(user=self.request.user)

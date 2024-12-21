from django.urls import include, path

from rest_framework.routers import SimpleRouter

from api.v1.orders.views import OrderViewSet


router = SimpleRouter()

router.register(r'orders', OrderViewSet)


urlpatterns = [
    path('', include(router.urls)),
]

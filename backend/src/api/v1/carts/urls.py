from django.urls import path, include

from rest_framework.routers import SimpleRouter

from api.v1.carts.views import CartViewSet


router = SimpleRouter()

router.register(r'carts', CartViewSet)


urlpatterns = [
    path('', include(router.urls)),
]

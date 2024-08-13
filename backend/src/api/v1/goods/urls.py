from django.urls import include, path

from rest_framework.routers import SimpleRouter

from api.v1.goods.views import CategoryViewSet


router = SimpleRouter()

router.register(r'category', CategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

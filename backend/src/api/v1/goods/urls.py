from django.urls import include, path

from rest_framework.routers import SimpleRouter

from api.v1.goods.views import CategoryViewSet, GoodsViewSet


router = SimpleRouter()

router.register(r'category', CategoryViewSet)
router.register(r'goods', GoodsViewSet)


urlpatterns = [
    path('', include(router.urls)),
]

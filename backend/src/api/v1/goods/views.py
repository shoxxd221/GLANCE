from rest_framework import viewsets

from apps.goods.models import Category

from api.v1.goods.serializers import CategorySerializer
from api.v1.goods.permissions import IsSuperuserOrStaffOrReadOnly


class CategoryViewSet(viewsets.ModelViewSet):
    """Viewset для категорий"""
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsSuperuserOrStaffOrReadOnly, )

from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework import viewsets


class CachedViewSet(viewsets.ModelViewSet):
    """Базовый класс ViewSet с кэшированием"""

    @method_decorator(cache_page(60))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class PermissionViewSet(CachedViewSet):
    """Базовый класс ViewSet с кешированием и выдачей queryset в зависимости от роли"""

    def get_queryset(self):
        if self.request.user.is_staff:
            return self.queryset.all()
        return self.queryset.filter(user=self.request.user)

from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework import viewsets


class CachedViewSet(viewsets.ModelViewSet):
    """Базовый класс ViewSet с кэшированием"""

    @method_decorator(cache_page(60))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
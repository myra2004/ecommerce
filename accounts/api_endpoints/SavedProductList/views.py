from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from .serializers import SavedProductListSerializer
from common.rediscache import RedisCacheMixin


class SavedProductListAPIView(RedisCacheMixin, ListAPIView):
    serializer_class = SavedProductListSerializer
    permission_classes = [IsAuthenticated]

    def get_cache_key(self):
        return f'saved-products-user-{self.request.user.id}'

    def get_queryset(self):
        return self.request.user.saved_products.all()

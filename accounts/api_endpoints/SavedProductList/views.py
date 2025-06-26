from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from .serializers import SavedProductListSerializer
from common.rediscache import RedisCacheMixin


class SavedProductListAPIView(RedisCacheMixin, ListAPIView):
    serializer_class = SavedProductListSerializer
    cache_key = 'saved-products'
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.request.user.saved_products.all()

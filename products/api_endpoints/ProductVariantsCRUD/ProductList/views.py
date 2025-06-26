from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, GenericAPIView

from products.models import ProductVariant
from .serializers import ProductVariantListSerializer
from common.rediscache import RedisCacheMixin


class ProductVariantListAPIView(RedisCacheMixin, ListAPIView):
    queryset = ProductVariant.objects.all()
    serializer_class = ProductVariantListSerializer
    cache_key = 'product-variant-list'

    def get(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
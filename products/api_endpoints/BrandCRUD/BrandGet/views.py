from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, GenericAPIView

from products.models import Brand
from .serializers import BrandGetSerializer
from common.rediscache import RedisCacheMixin


class BrandListAPIView(RedisCacheMixin, ListAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandGetSerializer
    cache_key = 'brand-list'

    def get(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
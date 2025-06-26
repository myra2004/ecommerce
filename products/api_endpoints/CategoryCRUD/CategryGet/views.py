from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, GenericAPIView

from products.models import Category
from .serializers import CategoryGetSerializer
from common.rediscache import RedisCacheMixin


class CategoryListAPIView(RedisCacheMixin, ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryGetSerializer
    cache_key = 'category-list'

    def get(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, GenericAPIView

from products.models import Color
from .serializers import ColorGetSerializer
from common.rediscache import RedisCacheMixin


class ColorListAPIView(RedisCacheMixin, ListAPIView):
    queryset = Color.objects.all()
    serializer_class = ColorGetSerializer
    cache_key = 'color-list'

    def get(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
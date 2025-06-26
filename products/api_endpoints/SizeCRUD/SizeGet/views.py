from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, GenericAPIView

from products.models import Size
from .serializers import SizeGetSerializer
from common.rediscache import RedisCacheMixin


class SizeListAPIView(RedisCacheMixin, ListAPIView):
    queryset = Size.objects.all()
    serializer_class = SizeGetSerializer
    cache_key = 'size-list'

    def get(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
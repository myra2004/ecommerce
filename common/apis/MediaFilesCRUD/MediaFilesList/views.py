from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, GenericAPIView

from common.models import MediaFile
from .serializers import MediaFileGetSerializer
from common.rediscache import RedisCacheMixin


class MediaFileGetAPIView(RedisCacheMixin, ListAPIView):
    queryset = MediaFile.objects.all()
    serializer_class = MediaFileGetSerializer
    cache_key = 'mediafile-list'


    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
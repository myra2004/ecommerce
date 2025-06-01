from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, GenericAPIView

from common.models import MediaFile
from .serializers import MediaFileGetSerializer


class MediaFileGetAPIView(ListAPIView):
    queryset = MediaFile.objects.all()
    serializer_class = MediaFileGetSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
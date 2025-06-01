from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, GenericAPIView

from common.models import MediaFile
from .serializers import MediaFileCreateSerializer


class MediaFileCreateAPIView(CreateAPIView):
    queryset = MediaFile.objects.all()
    serializer_class = MediaFileCreateSerializer

    def post(self, request, *args, **kwargs):
        serializer = MediaFileCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
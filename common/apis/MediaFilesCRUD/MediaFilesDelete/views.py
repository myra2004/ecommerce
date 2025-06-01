from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import DestroyAPIView, GenericAPIView

from products.models import MediaFile


class MediaFileDeleteAPIView(DestroyAPIView):
    queryset = MediaFile.objects.all()

    def delete(self, request, *args, **kwargs):
        return Response(status=status.HTTP_204_NO_CONTENT)
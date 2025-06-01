from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, GenericAPIView

from products.models import Color
from .serializers import ColorGetSerializer


class ColorListAPIView(ListAPIView):
    queryset = Color.objects.all()
    serializer_class = ColorGetSerializer

    def get(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
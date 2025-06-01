from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import UpdateAPIView, GenericAPIView

from products.models import ProductVariant
from .serializers import ProductVariantUpdateSerializer


class ProductVariantUpdateAPIView(UpdateAPIView):
    queryset = ProductVariant.objects.all()
    serializer_class = ProductVariantUpdateSerializer

    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, GenericAPIView

from products.models import ProductVariant
from .serializers import ProductVariantCreateSerializer


class ProductVariantCreateAPIView(CreateAPIView):
    queryset = ProductVariant.objects.all()
    serializer_class = ProductVariantCreateSerializer

    def post(self, request, *args, **kwargs):
        serializer = ProductVariantCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
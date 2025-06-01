from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import (
    GenericAPIView,
    ListAPIView,
    CreateAPIView,
    ListCreateAPIView,
)

from products.models import Product
from products.api_endpoints.ProductList.serializers import ProductListSerializer


class ProductListAPIView1(APIView):
    """
    APIView da uzimiz router(view) nima qilish kerakligini yozamiz,
    yani get, post, put/patch, delete metodlarini uzimiz qulda yozib chiqamiz
    """
    serializer_class = ProductListSerializer

    def get(self, request, *args, **kwargs):
        serializer = self.serializer_class(self.get_queryset(), many=True)
        return Response(serializer.data)

    def get_queryset(self):
        queryset = Product.objects.filter(is_active=True)
        return queryset


class ProductListAPIView2(GenericAPIView):
    """
    GenericAPIView da http metodlarini default yozilgan buladi,
    faqat ularni chaqirish kere buladi
    """
    queryset = Product.objects.filter(is_active=True)
    serializer_class = ProductListSerializer

    def get(self, request, *args, **kwargs):
        serializer = self.serializer_class(self.get_queryset(), many=True)
        return Response(serializer.data)


class ProductListAPIView3(ListCreateAPIView):
    """
    ListCreateAPIView da get va post metodi yozilgan,
    faqat qaysi model, va serializerni kursatse uzi swaggerda chiqarib beradi
    """
    queryset = Product.objects.filter(is_active=True)
    serializer_class = ProductListSerializer

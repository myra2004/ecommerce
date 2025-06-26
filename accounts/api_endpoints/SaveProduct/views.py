from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404

from products.models import Product
from .serializers import SaveProductSerializer


from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from django.shortcuts import get_object_or_404

from products.models import Product
from .serializers import SaveProductSerializer  # путь подставь свой

class SaveProductAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        request_body=SaveProductSerializer
    )
    def post(self, request, *args, **kwargs):
        product_id = request.data.get('id')
        if not product_id:
            return Response({'detail': 'Product ID is required'}, status=status.HTTP_400_BAD_REQUEST)

        product = get_object_or_404(Product, id=product_id)

        user = request.user  # user гарантированно есть, потому что IsAuthenticated

        if product in user.saved_products.all():
            user.saved_products.remove(product)
            action = 'removed'
        else:
            user.saved_products.add(product)
            action = 'added'

        return Response({'detail': f'Product successfully {action} to saved list'}, status=status.HTTP_200_OK)


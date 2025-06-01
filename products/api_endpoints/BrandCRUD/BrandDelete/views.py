from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import DestroyAPIView, GenericAPIView

from products.models import Brand


class BrandDeleteAPIView(DestroyAPIView):
    queryset = Brand.objects.all()
    lookup_field = 'id'

    def delete(self, request, *args, **kwargs):
        response = self.destroy(request, *args, **kwargs)
        return Response(status=status.HTTP_204_NO_CONTENT)


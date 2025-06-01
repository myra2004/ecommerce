from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, GenericAPIView, DestroyAPIView

from products.models import Size


class SizeDeleteAPIView(DestroyAPIView):
    queryset = Size.objects.all()
    look_up_field = 'id'

    def delete(self, request, *args, **kwargs):
        response = self.destroy(request, *args, **kwargs)
        return Response(status=status.HTTP_204_NO_CONTENT)
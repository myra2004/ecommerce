from rest_framework import permissions
from rest_framework.generics import UpdateAPIView, GenericAPIView

from .serializers import CartItemUpdateSerializer
from accounts.models import CartItem


class CartItemUpdateAPIView(GenericAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemUpdateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


__all__ = ['CartItemUpdateAPIView']
from rest_framework.generics import GenericAPIView
from rest_framework import permissions, status
from rest_framework.response import Response

from accounts.models import CartItem


class CartItemDeleteAPIView(GenericAPIView):
    queryset = CartItem.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


__all__ = ['CartItemDeleteAPIView']
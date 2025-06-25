from rest_framework.generics import CreateAPIView
from rest_framework import permissions

from .serializer import CheckOutSerializer


class CheckOutAPIView(CreateAPIView):
    serializer_class = CheckOutSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
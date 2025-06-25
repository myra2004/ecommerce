from drf_yasg.utils import swagger_auto_schema
from rest_framework.generics import CreateAPIView
from rest_framework import permissions

from .serializers import TransactionSerializer
from payments.models import Transaction


class WooPayCreateAPIView(CreateAPIView):
    # serializer_class = TransactionSerializer
    queryset = Transaction
    permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(
        request_body=TransactionSerializer
    )

    def get_serializer_class(self):
        context = super().get_serializer_context()
        context['user'] = self.request.user
        return context
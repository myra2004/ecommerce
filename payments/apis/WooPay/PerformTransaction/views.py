from django.core.serializers import serialize
from drf_yasg.utils import get_serializer_class
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import permissions, status

from .serializers import WooPayPerformSerializer
from payments.models import Transaction
from .services import handle_perform_transaction


class WooPayPerformAPIView(GenericAPIView):
    queryset = Transaction.objects.all()
    serializer_class = WooPayPerformSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        detail_message = handle_perform_transaction(serializer.validated_data)

        if not detail_message:
            return Response({
                'detail': 'You cant perform a transaction for non-exist order'
            }, status=status.HTTP_400_BAD_REQUEST)

        return Response({'detail': detail_message}, status=status.HTTP_200_OK)
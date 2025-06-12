from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from .serializers import SavedProductListSerializer


class SavedProductListAPIView(ListAPIView):
    serializer_class = SavedProductListSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.request.user.saved_products.all()

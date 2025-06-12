from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated

from products.models import Product, Review, Comment
from .serializers import ReviewCreateSerializer, CommentCreateSerializer


class ReviewCreateAPIView(CreateAPIView):
    serializer_class = ReviewCreateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)


class CommentCreateAPIView(CreateAPIView):
    serializer_class = CommentCreateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)
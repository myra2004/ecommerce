from rest_framework.generics import ListAPIView
from rest_framework import permissions

from products.models import Review, Comment
from .serializers import UserReviewsListSerializer, UserCommentsListSerializer
from common.rediscache import RedisCacheMixin


class UserReviewsListAPIView(RedisCacheMixin, ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserReviewsListSerializer
    cache_key = 'user-reviews'

    def get_queryset(self):
        user = Review.objects.filter(user=self.request.user).order_by('-created_at')
        return user


class UserCommentsListAPIView(RedisCacheMixin, ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserCommentsListSerializer
    cache_key = 'user-comments'

    def get_queryset(self):
        user = Comment.objects.filter(user=self.request.user).order_by('-created_at')
        return user
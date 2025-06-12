from rest_framework import serializers

from products.models import Review, Comment


class ReviewCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = [
            'id',
            'rating',
            'product',
        ]
        read_only_fields = ['id']


class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = [
            'id',
            'text',
            'product',
        ]
        read_only_fields = ['id']
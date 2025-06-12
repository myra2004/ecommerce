from rest_framework import serializers

from products.models import Review, Comment, Product


class ProductNestedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'id',
            'name',
        ]


class UserReviewsListSerializer(serializers.ModelSerializer):
    product = ProductNestedSerializer()
    class Meta:
        model = Review
        fields = [
            'id',
            'product',
            'rating',
            'review',
            'created_at',
        ]


class UserCommentsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = [
            'id',
            'product',
            'text',
            'created_at',
        ]
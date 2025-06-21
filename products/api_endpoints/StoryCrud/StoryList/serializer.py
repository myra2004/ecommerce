from rest_framework import serializers

from products.models import Story, Product


class ProductStorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'id',
            'name',
        ]


class StoryListSerializer(serializers.ModelSerializer):
    product = ProductStorySerializer(read_only=True)
    class Meta:
        model = Story
        fields = ['id', 'title', 'product', 'image', 'is_active']
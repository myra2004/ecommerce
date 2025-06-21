from rest_framework import serializers

from products.models import Product, Story


class StoryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Story
        fields = [
            'title',
            'image',
            'product',
        ]
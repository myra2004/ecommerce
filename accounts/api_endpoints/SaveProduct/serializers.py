from rest_framework import serializers

from products.models import Product


class SaveProductSerializer(serializers.Serializer):
    id = serializers.IntegerField()
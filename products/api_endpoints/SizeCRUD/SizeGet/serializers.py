from rest_framework import serializers

from products.models import Size


class SizeGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = ('name', 'slug',)
from rest_framework import serializers

from products.models import Product


class ProductListSerializer(serializers.ModelSerializer):
    """bu serializer kiruvchi malumotlar uchun"""
    class Meta:
        model = Product
        fields = [
            'id',
            'name',
            'description',
            'brand',
            'slug',
        ]

    def to_representation(self, instance):
        """bu chiquvchi malumotlar uchun"""
        instance = {
            'id': instance.id,
            'name': instance.name,
            'description': instance.description,
            'brand': instance.brand.name,
            'slug': instance.slug,
            'is_active': instance.is_active,
            'category': instance.category.name if instance.category else 'Not Available'
        }

        return instance
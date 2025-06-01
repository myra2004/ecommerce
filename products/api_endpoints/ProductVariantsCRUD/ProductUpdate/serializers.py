from rest_framework import serializers

from products.models import ProductVariant


class ProductVariantUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductVariant
        fields = (
            'name',
            'price',
            'product',
            'color',
            'size',
            'stock',
        )

    def to_representation(self, instance):
        instance = {
            'id': instance.id,
            'name': instance.name,
            'price': instance.price,
            'product': instance.product.name if instance.product else 'Not Available',
            'color': instance.color.name if instance.color else 'Not Available',
            'size': instance.size.name if instance.size else 'Not Available',
            'stock': instance.stock,
        }
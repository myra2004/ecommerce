from rest_framework import serializers

from products.models import Brand


class BrandCreateSerializer(serializers.ModelSerializer):
    logo = serializers.ImageField(use_url=True)

    class Meta:
        model = Brand
        fields = (
            'name',
            'slug',
            'logo',
        )

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'name': instance.name,
            'slug': instance.slug,
            'logo': instance.logo.url if instance.logo and hasattr(instance.logo, 'url') else None,
        }

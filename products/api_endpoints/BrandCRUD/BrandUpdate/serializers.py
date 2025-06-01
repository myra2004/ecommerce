from rest_framework import serializers

from products.models import Brand


class BrandUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = (
            'name',
            'slug',
            'logo',
        )

    def to_representation(self, instance):
        instance = {
            'id': instance.id,
            'name': instance.name,
            'slug': instance.slug,
            'logo': instance.logo
        }

        return instance

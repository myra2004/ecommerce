from rest_framework import serializers

from products.models import Brand


class BrandGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = (
            'name',
            'slug',
            'logo',
        )

    def to_representation(self, instance):
        print('>>>', bool(instance.logo))
        instance = {
            'id': instance.id,
            'name': instance.name,
            'slug': instance.slug,
            'logo': {
                str(instance.logo.url),
                str(instance.logo)
            } if bool(instance.logo) is not False else ''
        }

        return instance
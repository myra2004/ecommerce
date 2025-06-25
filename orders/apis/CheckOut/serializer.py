from rest_framework import serializers

from orders.choices import CheckoutSourceChoices
from .services import create_order


class CheckOutSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    source = serializers.ChoiceField(CheckoutSourceChoices.choices, required=True, write_only=True)
    product = serializers.IntegerField(required=True, write_only=True)
    quantity = serializers.IntegerField(required=True, write_only=True)

    def create(self, validated_data):
        created_order = create_order(**validated_data)
        if not created_order:
            raise serializers.ValidationError('Order could not be created.')
        return created_order
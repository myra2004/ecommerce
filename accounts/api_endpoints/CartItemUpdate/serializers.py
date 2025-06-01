from rest_framework import serializers

from accounts.models import CartItem, Cart


class CartItemUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ['quantity',]

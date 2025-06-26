from rest_framework import serializers

from products.models import Contact


class ContactListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['id', 'name', 'email', 'message']
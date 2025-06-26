from rest_framework import serializers
from products.models import Contact


class ContactCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']

        read_only_fields = ['id']
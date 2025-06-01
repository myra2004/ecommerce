from rest_framework import serializers

from accounts.models import User


class ProfileUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "first_name",
            "last_name",
            "phone_number",
            "avatar",
            "bio"
        ]
        read_only_fields = ["id"]
from rest_framework import serializers

from accounts.models import User
from .tokens import generate_email_verification_token
from .send_email import send_verification_email

class RegisterSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        token = generate_email_verification_token(user)
        send_verification_email(user, user.email, token)
        return user

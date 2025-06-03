from django.contrib.auth.hashers import make_password
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from rest_framework import serializers

from accounts.models import User
from core import settings


# class RegisterSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = [
#             "email",
#             "password",
#         ]
#
#     def validate_email(self, value):
#         if User.objects.filter(email=value).exists():
#             raise serializers.ValidationError("Email is already in use")
#         return value
#
#
#     def create(self, validated_data):
#
#         user = User.objects._create_user(
#             email=validated_data["email"],
#             password=validated_data["password"],
#         )
#         user.is_active = False
#         user.save()
#
#         self.context['send_email'](user)
#
#
#
#         # Email yuborish
#         send_mail(
#             "Verify your email",
#             f"Click here to verify your account: {verify_url}",
#             settings.DEFAULT_FROM_EMAIL,
#             [user.email],
#             fail_silently=False,
#         )
#
#         return user


class RegisterSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate_email(self, value):
        if User.objects.filter(email=value, is_active=True).exists():
            raise serializers.ValidationError("Email is already in use")
        #hash password dhango

        return value


    def create(self, validated_data):
        print(">>>", validated_data.get("email"))
        email = validated_data.get("email")
        password = make_password(validated_data.get("password"))

        user = User.objects.filter(email=email, is_active=False).first()
        if user:
            user.password = password
            user.save()
        else:
            user = User.objects._create_user(email=email, password=password)
            user.is_active = False  # Important: stay inactive until email confirmed
            user.save()

        uid = urlsafe_base64_encode(force_bytes(user.pk))
        token = default_token_generator.make_token(user)

        verify_url = f"http://localhost:8000/accounts/verify-email/{uid}/{token}/"
        self.context['send_email'](user, token, verify_url)

        return user

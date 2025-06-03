from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.models import User
from drf_yasg.utils import swagger_auto_schema
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from accounts.api_endpoints.Profile.Registration.send_email import send_verify_email
from accounts.api_endpoints.Profile.Registration.serializer import RegisterSerializer
from accounts.models import User


class RegisterView(APIView):
    permission_classes = []
    @swagger_auto_schema(
        request_body=RegisterSerializer
    )

    def post(self, request):
        serializer = RegisterSerializer(data=request.data, context={
            'send_email': send_verify_email
        })
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Verification email sent. Please check your inbox."},
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VerifyEmailView(APIView):
    def get(self, request, uidb64, token):
        try:
            uid = urlsafe_base64_decode(uidb64).decode()
            user = User.objects.get(pk=uid)
        except (User.DoesNotExist, ValueError):
            return Response({'error': 'Invalid link'}, status=status.HTTP_400_BAD_REQUEST)

        if default_token_generator.check_token(user, token):
            user.is_active = True
            user.save()
            return Response({'message': 'Email verified successfully!'}, status=status.HTTP_200_OK)
        return Response({'error': 'Invalid or expired token'}, status=status.HTTP_400_BAD_REQUEST)

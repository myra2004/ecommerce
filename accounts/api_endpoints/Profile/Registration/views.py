from rest_framework.response import Response
from rest_framework.views import APIView

from .tokens import verify_email_verification_token
from accounts.models import User


class VerifyEmailAPIView(APIView):
    permission_classes = []

    def get(self, request, token):
        user_id = verify_email_verification_token(token)
        if not user_id:
            return Response({"detail": "Invalid or expired token."}, status=400)

        user = User.objects.get(pk=user_id)
        user.is_email_verified = True
        user.save()
        return Response({"detail": "Email successfully verified!"}, status=200)

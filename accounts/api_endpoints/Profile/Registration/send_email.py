# from django.core.mail import send_mail
# from django.conf import settings
# from django.urls import reverse
# from django.utils.http import urlsafe_base64_encode
# from django.utils.encoding import force_bytes
# from django.contrib.auth.tokens import default_token_generator
#
# def send_verification_email(self, user):
#     uid = urlsafe_base64_encode(force_bytes(user.pk))
#     token = default_token_generator.make_token(user)
#     verify_url = f"http://localhost:8001/accounts/verify-email/{uid}/{token}/"
#
#     send_mail(
#         subject='Verify your email',
#         message=f'Click this link to verify your account: {verify_url}',
#         from_email=settings.DEFAULT_FROM_EMAIL,
#         recipient_list=[user.email],
#     )


from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings


def send_verify_email(user, token, verify_url):
    print(f"Sending email to: {user.email}")
    print(f"Verification link: {verify_url}")

    subject = 'Verify your email'
    to_email = user.email
    context = {
        'user': user,
        'token': token,
        'frontend_url': verify_url,
    }
    html_content = render_to_string('send_verify_email.html', context)
    email = EmailMessage(subject, html_content, to=[to_email])
    email.content_subtype = 'html'
    email.send()
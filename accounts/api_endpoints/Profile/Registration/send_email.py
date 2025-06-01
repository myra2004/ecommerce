from django.core.mail import EmailMessage
from django.template.loader import render_to_string


def send_verification_email(user, email, token):
    subject = 'Verify your email'
    context = {
        'user': user,
        'token': token,
        'frontend_url': "http://example.com/verify-email"
    }
    html_content = render_to_string('verify_email.html', context)
    email = EmailMessage(subject, html_content, to=[email])
    email.content_subtype = 'html'
    email.send()

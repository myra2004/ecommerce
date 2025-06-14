from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
from celery import shared_task


@shared_task
def send_password_reset_email(user, token):
    subject = 'Reset your password'
    to_email = user.email
    context = {
        'user': user,
        'token': token,
        'frontend_url': settings.FRONTEND_URL,
    }
    html_content = render_to_string('reset_password_email.html', context)
    email = EmailMessage(subject, html_content, to=[to_email])
    email.content_subtype = 'html'
    email.send()
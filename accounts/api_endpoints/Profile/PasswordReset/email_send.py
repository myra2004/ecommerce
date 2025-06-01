from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings

def send_password_reset_email(user, email, token):
    subject = 'Reset your password'
    to_email = email
    context = {
        'user': user,
        'token': token,
        'frontend_url': "voocomerce.com"
    }
    html_content = render_to_string('reset_password_email.html', context)
    email = EmailMessage(subject, html_content, to=[to_email])
    email.content_subtype = 'html'
    email.send()
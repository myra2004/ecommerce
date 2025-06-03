from django.core.mail import EmailMessage
from django.template.loader import render_to_string


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
from django.core.signing import TimestampSigner, BadSignature, SignatureExpired

signer = TimestampSigner(salt='email-verification')

def generate_email_verification_token(user):
    return signer.sign(user.pk)

def verify_email_verification_token(token):
    try:
        return int(signer.unsign(token, max_age=86400))  # 24 soat
    except (BadSignature, SignatureExpired):
        return None

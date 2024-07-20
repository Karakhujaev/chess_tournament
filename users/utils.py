from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.core.mail import send_mail
from django.urls import reverse

def generate_email_verification_token(user):
    return default_token_generator.make_token(user)

def generate_uid(user):
    return urlsafe_base64_encode(force_bytes(user.pk))

def send_verification_email(user):
    token = generate_email_verification_token(user)
    uid = generate_uid(user)
    verification_link = reverse('verify-email', kwargs={'uidb64': uid, 'token': token})
    verification_url = f"http://yourdomain.com{verification_link}"

    subject = 'Email Verification'
    message = f'Hi {user.username},\n\nPlease click the link below to verify your email address:\n{verification_url}'
    send_mail(subject, message, 'your-email@example.com', [user.email])

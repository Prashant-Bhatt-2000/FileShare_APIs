from django.core.mail import send_mail
from django.conf import settings


def sendemail(email, token): 
    subject = "Your account verification email"
    message = f'Please click on this link http://127.0.0.1:8000/api/accounts/verifytoken/{token}'
    email_from = settings.EMAIL_HOST_USER

    send_mail(subject, message, email_from, [email])

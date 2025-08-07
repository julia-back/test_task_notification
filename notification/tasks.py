from celery import shared_task
from django.core.mail import send_mail
from config.settings import EMAIL_HOST_USER
import smtplib


@shared_task
def send_email_notification(email, subject, message):
    try:
        send_mail(recipient_list=[email], subject=subject, message=message,
                from_email=EMAIL_HOST_USER, fail_silently=False)
        return True
    except Exception as e:
        return False


@shared_task
def send_sms_notification(phone_number, subject, message):
    try:
        send_mail(recipient_list=[email], subject=subject, message=message, from_email=EMAIL_HOST_USER)
        return True
    except Exception as e:
        return False


@shared_task
def send_telegram_notification(telegram_username, subject, message):
    try:
        send_mail(recipient_list=[email], subject=subject, message=message, from_email=EMAIL_HOST_USER)
        return True
    except Exception as e:
        return False

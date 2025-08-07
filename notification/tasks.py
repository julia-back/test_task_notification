from celery import shared_task
from django.core.mail import send_mail
from config.settings import EMAIL_HOST_USER, TELEGRAM_BOT_TOKEN, SMSC_RU_LOGIN, SMSC_RU_PASSWORD
import smtplib
from telegram import Bot
from telegram.error import TelegramError
import requests


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
        url = "https://smsc.ru/sys/send.php"
        params = {
            "login": SMSC_RU_LOGIN,
            "psw": SMSC_RU_PASSWORD,
            "phones": phone_number,
            "mes": message,
            "sender": "DjangoNotification",
            "fmt": 3,
        }
        requests.get(url, params=params)
        return True
    except Exception as e:
        return False


@shared_task
def send_telegram_notification(chat_id, subject, message):
    try:
        url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
        requests.post(url, json={"chat_id": chat_id, "text": subject + "\n" + message})
        return True
    except Exception as e:
        return False

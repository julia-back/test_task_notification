from sys import stdout
import logging
from .tasks import send_email_notification, send_sms_notification, send_telegram_notification
from .models import RecipientModel
import smtplib


def send_notification(recipient: RecipientModel, subject, message):
    info = ""

    task_result = send_email_notification.delay(recipient.email, subject, message)
    if task_result.get():
        info = info + "Задача на отправку по email поставлена в очередь.\n"
    else:
        info = info + "Не удалось отправить по email.\n"

    task_result = send_sms_notification.delay(recipient.phone_number, subject, message)
    if task_result.get():
        info = info + "Задача на отправку по SMS поставлена в очередь.\n"
    else:
        info = info + "Не удалось отправить по SMS.\n"

    task_result = send_telegram_notification.delay(recipient.telegram_chat_id, subject, message)
    if task_result.get():
        info = info + "Задача на отправку в Telegram поставлена в очередь.\n"
    else:
        info = info + "Не удалось отправить в Telegram.\n"

    return info

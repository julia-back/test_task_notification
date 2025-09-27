from celery import shared_task
from .services import EmailChannel, SMSChannel, TelegramChannel


@shared_task
def send_email_notification(email, subject, message) -> bool:
    """Задача для отправки в фоновом режиме уведомления по email."""

    return EmailChannel().send(email, subject, message)


@shared_task
def send_sms_notification(phone_number, subject, message) -> bool:
    """Задача для отправки в фоновом режиме уведомления по SMS."""

    return SMSChannel().send(phone_number, subject, message)


@shared_task
def send_telegram_notification(chat_id, subject, message) -> bool:
    """Задача для отправки в фоновом режиме уведомления в Telegram."""

    return TelegramChannel.send(chat_id, subject, message)

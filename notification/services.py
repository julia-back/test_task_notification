from .tasks import send_email_notification, send_sms_notification, send_telegram_notification
from .models import RecipientModel


def send_notification(recipient: RecipientModel):
    pass

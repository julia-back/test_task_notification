from .tasks import send_email_notification, send_sms_notification, send_telegram_notification
from .models import RecipientModel
from abc import ABC, abstractmethod
from django.core.mail import send_mail
from config.settings import EMAIL_HOST_USER, TELEGRAM_BOT_TOKEN, SMSC_RU_LOGIN, SMSC_RU_PASSWORD

import requests


# def send_notification(recipient: RecipientModel, subject, message):
#     """
#     Сервисная функция для отправки уведомления получателю различными способоами.
#     Добавляет в ответ запроса информацию об успешном или неуспешном добавлении в очередь
#     Celery для отправки уведомления.
#     """
#
#     info = ""
#
#     task_result = send_email_notification.delay(recipient.email, subject, message)
#     if task_result.get():
#         info = info + "Задача на отправку по email поставлена в очередь.\n"
#     else:
#         info = info + "Не удалось отправить по email.\n"
#
#     task_result = send_sms_notification.delay(recipient.phone_number, subject, message)
#     if task_result.get():
#         info = info + "Задача на отправку по SMS поставлена в очередь.\n"
#     else:
#         info = info + "Не удалось отправить по SMS.\n"
#
#     task_result = send_telegram_notification.delay(recipient.telegram_chat_id, subject, message)
#     if task_result.get():
#         info = info + "Задача на отправку в Telegram поставлена в очередь.\n"
#     else:
#         info = info + "Не удалось отправить в Telegram.\n"
#
#     return info


class NotificationChannel(ABC):

    @abstractmethod
    def send(self, recipient, subject, message):
        pass


class EmailChannel(NotificationChannel):

    def send(self, email, subject, message):
        try:
            send_mail(recipient_list=[email], subject=subject, message=message,
                      from_email=EMAIL_HOST_USER, fail_silently=False)
            return True
        except Exception:
            return False


class SMSChannel(NotificationChannel):

    def send(self, phone_number, subject, message):
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
        except Exception:
            return False


class TelegramChannel(NotificationChannel):

    def send(self, chat_id, subject, message):
        try:
            url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
            requests.post(url, json={"chat_id": chat_id, "text": subject + "\n" + message})
            return True
        except Exception:
            return False


class NotificationManager:
    """
    Менеджер для отправки уведомления получателю различными способоами.
    """

    notification_channels: list[str]

    def __init__(self, channels: list) -> None:
        self.notification_channels = channels

    def send_notification(self, recipient: RecipientModel, subject, message):
        """
        Менеджер для отправки уведомления получателю различными способоами.
        Добавляет в ответ запроса информацию об успешном или неуспешном добавлении в очередь
        Celery для отправки уведомления.
        """

        info = ""
        is_send = False

        for channel in self.notification_channels:
            if is_send is False:

                if channel == "email":
                    task_result = send_email_notification.delay(recipient.email, subject, message)
                    if task_result.get():
                        info = info + "Задача на отправку по email поставлена в очередь.\n"
                        is_send = True
                    else:
                        info = info + "Не удалось отправить по email.\n"

                elif channel == "sms":
                    task_result = send_sms_notification.delay(recipient.phone_number, subject, message)
                    if task_result.get():
                        info = info + "Задача на отправку по SMS поставлена в очередь.\n"
                    else:
                        info = info + "Не удалось отправить по SMS.\n"
                    is_send = True

                elif channel == "telegram":
                    task_result = send_telegram_notification.delay(recipient.telegram_chat_id, subject, message)
                    if task_result.get():
                        info = info + "Задача на отправку в Telegram поставлена в очередь.\n"
                    else:
                        info = info + "Не удалось отправить в Telegram.\n"
                    is_send = True

            else:
                break

        return info

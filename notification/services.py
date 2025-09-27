from .tasks import send_email_notification, send_sms_notification, send_telegram_notification
from .models import RecipientModel


class NotificationService:
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

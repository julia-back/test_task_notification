from celery import shared_task


@shared_task
def send_email_notification():
    pass


@shared_task
def send_sms_notification():
    pass


@shared_task
def send_telegram_notification():
    pass

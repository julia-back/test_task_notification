from django.db import models


class RecipientModel(models.Model):
    """Модель получателя уведомления, не смешана с моделью пользователя для удобной тестовой отладки."""

    email = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=12)
    telegram_chat_id = models.CharField(max_length=50)

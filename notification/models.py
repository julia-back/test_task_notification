from django.db import models


class RecipientModel(models.Model):

    email = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=12)
    telegram_username = models.CharField(max_length=50)

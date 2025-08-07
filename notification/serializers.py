from rest_framework import serializers


class SendNotificationSerializers(serializers.Serializer):
    """Класс сериализатора для представления отправки уведомления."""

    subject = serializers.CharField(max_length=50)
    message = serializers.CharField(max_length=255)

from rest_framework import serializers


class SendNotificationSerializers(serializers.Serializer):

    subject = serializers.CharField(max_length=50)
    message = serializers.CharField(max_length=255)

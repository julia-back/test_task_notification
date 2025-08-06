from rest_framework import serializers


class SendNotificationSerializer(serializers.Serializer):

    recipient = serializers.CharField(max_length=50)
    subject = serializers.CharField(max_length=255)
    message = serializers.CharField(max_length=50)

from rest_framework.views import APIView
from rest_framework.response import Response
from .services import send_notification
from rest_framework import status
from .models import RecipientModel
from .serializers import SendNotificationSerializers
import smtplib


class SendNotificationAPIView(APIView):

    def post(self, request, recipient_id):
        serializer = SendNotificationSerializers(data=request.data)

        if serializer.is_valid():
            message = serializer.data.get("message")
            subject = serializer.data.get("subject")

            try:
                recipient = RecipientModel.objects.get(id=recipient_id)
            except RecipientModel.DoesNotExist:
                return Response({"status": "error", "message": "Recipient not found"},
                                status=status.HTTP_404_NOT_FOUND)

            send_result = send_notification(recipient, subject, message)
            return Response({"result": send_result}, status=status.HTTP_200_OK)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

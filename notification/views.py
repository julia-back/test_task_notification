from rest_framework.views import APIView
from rest_framework.response import Response
from .services import send_notification
from rest_framework import status
from .models import RecipientModel


class SendNotificationAPIView(APIView):

     def post(self, request, recipient_id):
          recipient = RecipientModel.objects.get(id=recipient_id)
          try:
               send_notification(recipient)
               return Response(
                    {"status": "success", "message": "Уведомление отправлено"},
                    status=status.HTTP_200_OK
               )
          except Exception as e:
               return Response(
                    {"status": "error", "message": str(e)},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR
               )

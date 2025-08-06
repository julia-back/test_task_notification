from rest_framework.views import APIView
from services import send_message
from serializers import SendNotificationSerializer


class SendNotificationAPIView(APIView):

     def post(self, request):
          serializer = SendNotificationSerializer(request)
          return send_message()

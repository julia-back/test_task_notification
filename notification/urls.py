from django.urls import path
from notification.apps import NotificationConfig
from .views import SendNotificationAPIView


app_name = NotificationConfig.name


urlpatterns = [
    path("send_notification/<int:recipient_id>/", SendNotificationAPIView.as_view(), name="send_notification"),
]

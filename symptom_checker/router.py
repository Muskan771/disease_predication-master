from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path('ws/symptom-check/', consumers.SymptomConsumer.as_asgi()),
]

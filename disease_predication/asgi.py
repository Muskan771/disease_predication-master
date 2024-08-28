"""
ASGI config for disease_predication project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator, OriginValidator
from symptom_checker import router  # Replace 'your_app' with the name of your app

# Set the default Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'disease_predication.settings')

# Create the ASGI application instance
application = ProtocolTypeRouter({
    # HTTP protocol handled by Django's ASGI application
    "http": get_asgi_application(),

    # WebSocket protocol
    "websocket": AllowedHostsOriginValidator(
        AuthMiddlewareStack(
            URLRouter(
                router.websocket_urlpatterns  # Ensure you define this in your routing.py
            )
        )
    ),
})






import symptom_checker.routing

        URLRouter(
            symptom_checker.routing.websocket_urlpatterns
        )
    ),


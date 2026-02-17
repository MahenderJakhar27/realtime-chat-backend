import os
import django
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from django.urls import path

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from chat.consumers import ChatConsumer

application = ProtocolTypeRouter({
    "http": get_asgi_application(),

    "websocket": URLRouter([
        path("ws/chat/<int:room_id>/", ChatConsumer.as_asgi()),
    ]),
})

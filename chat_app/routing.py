from django.urls import path
from . import consumers

websocket_urlpattern = [
    path('ws/chat/', consumers.ChatAsyncConsumer.as_asgi()),
    path('ws/chat/<int:id>/', consumers.ChatAsyncConsumer.as_asgi()),
]
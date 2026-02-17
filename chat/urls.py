from django.urls import path
from .views import (
    CreateChatRoomView,
    UserChatRoomsView,
    SendMessageView,
    RoomMessagesView
)

urlpatterns = [
    path('rooms/create/', CreateChatRoomView.as_view()),
    path('rooms/', UserChatRoomsView.as_view()),
    path('messages/send/', SendMessageView.as_view()),
    path('rooms/<int:room_id>/messages/', RoomMessagesView.as_view()),
]

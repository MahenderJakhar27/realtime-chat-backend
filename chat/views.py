from rest_framework import generics, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import ChatRoom, Message
from .serializers import (
    ChatRoomSerializer,
    CreateChatRoomSerializer,
    MessageSerializer
)


# Create chat room
class CreateChatRoomView(generics.CreateAPIView):
    serializer_class = CreateChatRoomSerializer
    permission_classes = [permissions.IsAuthenticated]


# List rooms for logged-in user
class UserChatRoomsView(generics.ListAPIView):
    serializer_class = ChatRoomSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.request.user.chat_rooms.all()


# Send message
class SendMessageView(generics.CreateAPIView):
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(sender=self.request.user)


# Get messages of a room
class RoomMessagesView(generics.ListAPIView):
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        room_id = self.kwargs['room_id']
        return Message.objects.filter(room_id=room_id).order_by('timestamp')

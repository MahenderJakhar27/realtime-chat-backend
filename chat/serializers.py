
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import ChatRoom, Message


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


class ChatRoomSerializer(serializers.ModelSerializer):
    users = UserSerializer(many=True, read_only=True)

    class Meta:
        model = ChatRoom
        fields = ['id', 'name', 'users', 'created_at']


class CreateChatRoomSerializer(serializers.ModelSerializer):
    user_ids = serializers.ListField(
        child=serializers.IntegerField(), write_only=True
    )

    class Meta:
        model = ChatRoom
        fields = ['name', 'user_ids']

    def create(self, validated_data):
        user_ids = validated_data.pop('user_ids')
        room = ChatRoom.objects.create(**validated_data)
        users = User.objects.filter(id__in=user_ids)
        room.users.set(users)
        return room


class MessageSerializer(serializers.ModelSerializer):
    sender = UserSerializer(read_only=True)

    class Meta:
        model = Message
        fields = ['id', 'room', 'sender', 'content', 'timestamp']
        read_only_fields = ['sender']


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
        request = self.context.get('request')

        room = ChatRoom.objects.create(**validated_data)

        # Get selected users
        users = list(User.objects.filter(id__in=user_ids))

        # Always add creator
        if request and request.user not in users:
            users.append(request.user)

        room.users.set(users)
        return room



class MessageSerializer(serializers.ModelSerializer):
    sender = UserSerializer(read_only=True)

    class Meta:
        model = Message
        fields = ['id', 'room', 'sender', 'content', 'timestamp']
        read_only_fields = ['sender']

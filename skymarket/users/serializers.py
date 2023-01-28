from djoser.serializers import UserCreateSerializer, UserSerializer
from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class UserRegistrationSerializer(UserCreateSerializer):
    image = serializers.ImageField(required=False)
    password = serializers.CharField(write_only=True)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = '__all__'


class CustomSerializer(UserSerializer):
    email = serializers.EmailField(read_only=True)

    class Meta:
        model = User
        fields = '__all__'

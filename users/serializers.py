from rest_framework import serializers
from .models import User
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model
User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    email = serializers.CharField(write_only=True)
    name = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ('email', 'name', 'password')
    def create(self, validated_data):
        name = validated_data['name']
        email = validated_data['email']
        password = validated_data['password']
        user = User(email=email, name=name)
        # Sets the user's password to the given raw string,
        # taking care of the password hashing. Doesn't save the User object.
        user.set_password(password)
        # save() method to save the user object
        user.save()
        return user

class TokenSerializer(serializers.Serializer):
    token = serializers.CharField(max_length=255)
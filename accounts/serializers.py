from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from collections import OrderedDict


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email')


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            validated_data['email'], validated_data['email'], validated_data['password'])
        return user


class LoginSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(
            **OrderedDict([('username', v) if k == 'email' else (k, v) for k, v in data.items()]))
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect Credentials")

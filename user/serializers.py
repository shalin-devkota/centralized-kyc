from rest_framework import serializers
from .models import VerifiedUser, AuthUser


class UserDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = VerifiedUser
        fields = "__all__"


class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthUser
        fields = "__all__"

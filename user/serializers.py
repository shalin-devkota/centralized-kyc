from rest_framework import serializers
from .models import VerifiedUser


class UserDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = VerifiedUser
        fields = "__all__"

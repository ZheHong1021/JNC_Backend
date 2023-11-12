from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # 白名單
        fields = ['url', 'username', 'email', 'is_staff']


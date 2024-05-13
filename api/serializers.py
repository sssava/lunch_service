from rest_framework import serializers
from django.contrib.auth import get_user_model
from core.constants import ROLE_CHOICES, EMPLOYEE


User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True, max_length=100)
    first_name = serializers.CharField(required=False, max_length=255)
    last_name = serializers.CharField(required=False, max_length=255)
    role = serializers.ChoiceField(choices=ROLE_CHOICES, required=True)

    class Meta:
        model = User
        fields = ["id", 'email', "username", "password", "first_name", "last_name", "role"]

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

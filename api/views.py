from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from .serializers import UserSerializer
from django.contrib.auth import get_user_model


User = get_user_model()


class UserCreateAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

import datetime

from rest_framework.generics import CreateAPIView, ListCreateAPIView
from rest_framework.response import Response
from api.serializers import UserSerializer, CreateMenuSerializer, MenuSerializer
from django.contrib.auth import get_user_model
from api.models import Menu
from api.custom_permissions import IsRestaurantOnly
from rest_framework import permissions


User = get_user_model()


class UserCreateAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class MenuListCreateAPIView(ListCreateAPIView):
    queryset = Menu.objects.filter(menu_date=datetime.date.today())
    serializer_class = MenuSerializer

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CreateMenuSerializer
        return self.serializer_class

    def create(self, request, *args, **kwargs):
        print(request.user.id)
        if self.is_user_id_equals_request_user(user_id=request.data.get('user')):
            if Menu.objects.filter(user=request.user, menu_date=datetime.date.today()).exists():
                return Response(data={"error": "You already added menu today"})

            return super().create(request, *args, **kwargs)
        return Response(data={"error": "User id does not equals to request user id"})

    def is_user_id_equals_request_user(self, user_id):
        return int(user_id) == self.request.user.id

    def get_permissions(self):
        if self.request.method == "POST":
            self.permission_classes = [permissions.IsAuthenticated, IsRestaurantOnly]
        else:
            self.permission_classes = [permissions.IsAuthenticated]

        return [permission() for permission in self.permission_classes]

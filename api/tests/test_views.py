from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from django.contrib.auth import get_user_model


User = get_user_model()


class AuthenticateRegister(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='ssava', password="1234ssava345", role="Employee")

    def test_authenticate(self):
        url = reverse('token_obtain_pair')
        data = {"username": self.user.username, "password": "1234ssava345"}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response_after_login = self.client.get(
            path=reverse('menu'),
            headers={"Authorization": f"Bearer {response.data['access']}"},
            format='json'
        )
        self.assertEqual(response_after_login.status_code, status.HTTP_200_OK)

    def test_authenticate_with_wrong_token(self):
        url = reverse('token_obtain_pair')
        data = {"username": self.user.username, "password": "1234ssava345"}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response_after_login = self.client.get(
            path=reverse('menu'),
            headers={"Authorization": f"Bearer INIWENoisnori493492ng"},
            format='json'
        )
        self.assertEqual(response_after_login.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_register(self):
        url = reverse('user-create')
        data = {"username": "test", "email": "test@gmail.com", "password": "1234test4321", "role": "Employee"}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.all().count(), 2)

    def test_register_with_existing_username(self):
        url = reverse('user-create')
        data = {"username": self.user.username, "email": "test@gmail.com", "password": "1234test4321", "role": "Employee"}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(User.objects.all().count(), 1)
        self.assertEqual(response.data['username'][0], "A user with that username already exists.")

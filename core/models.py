from django.contrib.auth.models import AbstractUser
from django.db import models
from core.constants import ROLE_CHOICES, EMPLOYEE


class User(AbstractUser):
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default=EMPLOYEE)

    def __str__(self):
        return f"{self.username} - {self.role}"

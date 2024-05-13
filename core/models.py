from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    RESTAURANT = "Restaurant"
    EMPLOYEE = "Employee"

    ROLE_CHOICES = [
        (RESTAURANT, "Restaurant"),
        (EMPLOYEE, "Employee"),
    ]

    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default=EMPLOYEE)

    def __str__(self):
        return f"{self.username} - {self.role}"

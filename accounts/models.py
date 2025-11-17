from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    bio = models.TextField(max_length=500, blank=True)
    age = models.IntegerField(default=0)

    def __str__(self):
        return self.username
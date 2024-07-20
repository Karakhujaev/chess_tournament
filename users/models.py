from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    is_admin = models.BooleanField(default=False)
    email = models.EmailField()
    is_active = models.BooleanField(default=True)
    is_verified = models.BooleanField(default=False)
    name = models.CharField(max_length=250)
    age = models.IntegerField()
    rate = models.IntegerField()
    country = models.CharField(max_length=250)

    def __str__(self):
        return self.username

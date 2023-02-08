from django.db import models
from django.contrib.auth.models import AbstractUser
from django.forms import CharField

class User(AbstractUser):
    username = CharField(max_length=255)
    email = CharField(max_length=255, unique=True)
    password = CharField(max_length=255)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = 'username'
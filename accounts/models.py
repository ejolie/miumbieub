from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class User(AbstractUser):
    from_user = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="to_user")

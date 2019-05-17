from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class User(AbstractUser):
    from_user = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="to_user")

    def get_score(self):
        return round(self.ratings.aggregate(models.Avg('score'))['score__avg'], 2)

    def get_recommend(self):
        return self.ratings.order_by('-score').first()

    def __str__(self):
        return self.username

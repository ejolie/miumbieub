from django.db import models
from django.contrib.auth import get_user_model


class Genre(models.Model):
    type = models.CharField(max_length=150)


class Movie(models.Model):
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, related_name='movies')
    title = models.CharField(max_length=150)
    director = models.CharField(max_length=45)
    summary = models.TextField()


class Rating(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='ratings')
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='ratings')
    comment = models.TextField()
    score = models.IntegerField()

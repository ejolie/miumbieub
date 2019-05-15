from django.db import models
from django.contrib.auth import get_user_model


class Genre(models.Model):
    type = models.CharField(max_length=150)
    
    def __str__(self):
        return self.type


class Movie(models.Model):
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, related_name='movies')
    title = models.CharField(max_length=150)
    director = models.CharField(max_length=45)
    summary = models.TextField()

    def __str__(self):
        return self.genre

class Rating(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='ratings')
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='ratings')
    comment = models.TextField()
    score = models.IntegerField()

    def __str__(self):
        return f'{self.movie} | {self.score} | {self.comment}'
from datetime import datetime
from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator


class Genre(models.Model):
    type = models.CharField(max_length=150)

    def __str__(self):
        return self.type


class Movie(models.Model):
    genres = models.ManyToManyField(Genre, related_name='movies')
    title = models.CharField(max_length=150)
    title_eng = models.CharField(max_length=150, default="", blank=True)
    title_org = models.CharField(max_length=150, default="", blank=True)
    audience = models.IntegerField(default=0)
    release = models.DateField(default=datetime.now, blank=True)
    thumb_url = models.URLField(max_length=200, default="", blank=True)
    poster_url = models.URLField(max_length=200, default="", blank=True)
    running_time = models.IntegerField(default=0)
    director = models.CharField(max_length=45, default="", blank=True)
    film_rating = models.CharField(max_length=45, default="", blank=True)
    actor1 = models.CharField(max_length=45, default="", blank=True)
    actor2 = models.CharField(max_length=45, default="", blank=True)
    actor3 = models.CharField(max_length=45, default="", blank=True)

    def __str__(self):
        return self.title

    @classmethod
    def max_audience(cls):
        return cls.objects.order_by('-audience')[0]


class Rating(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='ratings')
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='ratings')
    comment = models.TextField()
    score = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])

    def username(self):
        return self.user.username

    def __str__(self):
        return f'{self.movie} | {self.score} | {self.comment}'

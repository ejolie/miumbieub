from django.contrib import admin
from .models import Genre, Movie, Rating

admin.site.register(Genre)
admin.site.register(Movie)
admin.site.register(Rating)

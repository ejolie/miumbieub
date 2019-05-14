from rest_framework import serializers
from .models import Genre, Movie, Rating


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        field = "__all__"


class MovieSerializer(serializers.ModelSerializer):
    ratings = RatingSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        field = "__all__"


class GenreSerializer(serializers.ModelSerializer):
    movies = MovieSerializer(many=True, read_only=True)

    class Meta:
        model = Genre
        field = "__all__"

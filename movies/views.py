from django.shortcuts import render, get_object_or_404
from django.conf import settings
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Genre, Movie, Rating
from .serializers import GenreSerializer, MovieSerializer, RatingSerializer
import json
import os


def index(request):
    movie_of_week = Movie.max_audience()
    return render(request, 'movies/home.html', {'movie': movie_of_week})


def movies_view(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    return render(request, 'movies/detail.html', {'movie': movie})


def genres_view(request):
    genre = get_object_or_404(Genre, type=request.GET.get('type'))
    return render(request, 'movies/genre.html', {'genre': genre})


@api_view(["GET"])
def genres_list(request):
    genres = Genre.objects.all()
    serializer = GenreSerializer(genres, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def genres_detail(request, pk):
    genre = get_object_or_404(Genre, pk=pk)
    serializer = GenreSerializer(genre)
    return Response(serializer.data)


@api_view(["GET"])
def movies_list(request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def movies_detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)


@api_view(["GET", "POST"])
def ratings_list(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == "GET":
        ratings = movie.ratings.all()
        serializer = RatingSerializer(ratings, many=True)
        return Response(serializer.data)
    else:
        if request.user.is_authenticated:
            request.data["movie"] = movie.id
            request.data["user"] = request.user.id
            serializer = RatingSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)


@api_view(["GET", "DELETE", "PUT"])
def ratings_detail(request, pk):
    rating = get_object_or_404(Rating, pk=pk)
    if request.method == 'GET':
        serializer = RatingSerializer(rating)
        return Response(serializer.data)
    else:
        if request.user == rating.user:
            request.data["movie"] = rating.movie.id
            request.data["user"] = request.user.id
            if request.method == 'PUT':
                serializer = RatingSerializer(rating, data=request.data)
                if serializer.is_valid(raise_exception=True):
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
            elif request.method == 'DELETE':
                rating.delete()
                return Response({"message": "삭제되었습니다."}, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)


def load(request):
    data = []
    json_data = os.path.join(settings.BASE_DIR, 'static', "data/data.json")
    with open(json_data, encoding='UTF-8') as f:
        data = json.load(f)
    for rec in data:
        # 'genre': rec['genre'].split('/'),
        context = {
            'id': rec['id'],
            'title': rec['title'],
            'title_eng': rec['title_eng'],
            'title_org': rec['title_org'],
            'audience': rec['audience'],
            'release': rec['release'],
            'thumb_url': rec['thumb_url'],
            'poster_url': rec['poster_url'],
            'running_time': rec['running_time'],
            'director': rec['director'],
            'film_rating': rec['film_rating'],
            'actor1': rec['actor1'],
            'actor2': rec['actor2'],
            'actor3': rec['actor3'],
        }
        movie = Movie.objects.create(**context)
        for genre_name in rec['genre'].split('/'):
            obj, created = Genre.objects.get_or_create(type=genre_name)
            movie.genres.add(obj)
        movie.save()

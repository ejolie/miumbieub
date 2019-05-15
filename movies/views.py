from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Genre, Movie, Rating
from .serializers import GenreSerializer, MovieSerializer, RatingSerializer


def index(request):
    return render(request, 'movies/home.html')
    
def detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    return render(request, 'movies/detail.html', { 'movie': movie })

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
        serializer = RatingSerializer(ratings, Many=True)
        return Response(serializer.data)
    else:
        if request.user.is_authenticated():
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
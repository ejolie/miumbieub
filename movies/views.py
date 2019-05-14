from django.shortcuts import render


def index(request):
    return render(request, 'movies/app.html')


def genres_list(request):
    pass


def genres_detail(request, pk):
    pass


def movies_list(request):
    pass


def movies_detail(request, pk):
    pass


def ratings_list(request, movie_pk):
    pass


def ratings_detail(request, movie_pk, rating_pk):
    pass

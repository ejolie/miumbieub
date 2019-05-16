from . import views
from django.urls import path

app_name = "movies"
urlpatterns = [
    path('', views.index, name="index"),
    path('genres/', views.genres_view, name="genres_view"),
    path('movies/<int:pk>/', views.movies_view, name="movies_view"),
    path('api/genres/', views.genres_list, name="genres_list"),
    path('api/genres/<int:pk>/', views.genres_detail, name="genres_detail"),
    path('api/movies/', views.movies_list, name="movies_list"),
    path('api/movies/<int:pk>/', views.movies_detail, name="movies_detail"),
    path('api/movies/<int:pk>/ratings/', views.ratings_list, name="ratings_list"),
    path('api/ratings/<int:pk>/', views.ratings_detail, name="ratings_detail"),
    path('load/', views.load),
]

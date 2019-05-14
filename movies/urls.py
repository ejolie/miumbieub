from . import views
from django.urls import path

app_name = "movies"
urlpatterns = [
    path('', views.index),
    path('genres/', views.genres_list),
    path('genres/<int:pk>/', views.genres_detail),
    path('movies/', views.movies_list),
    path('movies/<int:pk>/', views.movies_detail),
    path('movies/<int:movie_pk>/ratings/', views.ratings_list),
    path('movies/<int:movie_pk>/ratings/<int:rating_pk>/', views.ratings_detail),
]

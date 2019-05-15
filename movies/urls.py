from . import views
from django.urls import path

app_name = "movies"
urlpatterns = [
    path('', views.index, name="index"),
    path('<int:pk>/', views.detail, name="detail"),
    path('genres/', views.genres_list, name="genres_list"),
    path('genres/<int:pk>/', views.genres_detail, name="genres_detail"),
    path('movies/', views.movies_list, name="movies_list"),
    path('movies/<int:pk>/', views.movies_detail, name="movies_detail"),
    path('movies/<int:pk>/ratings/', views.ratings_list, name="ratings_list"),
    path('ratings/<int:pk>/', views.ratings_detail, name="ratings_detail"),
    path('load/', views.load),
]

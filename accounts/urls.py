from django.urls import path
from . import views

app_name = "accounts"
urlpatterns = [
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    path('signup/', views.signup, name="signup"),
    path('<str:username>/', views.profile_view, name="profile_view"),
    path('<str:username>/follow/', views.profile_follow, name="profile_follow"),
    path('api/<str:username>/', views.profile_detail, name="profile_detail"),
]

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import UserCustomCreationForm
from .serializers import UserSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse


def login(request):
    if request.user.is_authenticated:
        return redirect('movies:index')
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect(request.GET.get('next') or 'movies:index')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})


@login_required
def logout(request):
    auth_logout(request)
    return redirect('movies:index')


def signup(request):
    if request.user.is_authenticated:
        return redirect('movies:index')
    if request.method == 'POST':
        user_form = UserCustomCreationForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            auth_login(request, user)
            return redirect('movies:index')
    else:
        user_form = UserCustomCreationForm()
    return render(request, 'accounts/signup.html', {'form': user_form})


def profile_view(request, username):
    user = get_object_or_404(get_user_model(), username=username)
    return render(request, 'accounts/profile.html', {'person': user})


@api_view(["GET"])
def profile_detail(request, username):
    user = get_object_or_404(get_user_model(), username=username)
    serializer = UserSerializer(user)
    return Response(serializer.data)


@login_required
def profile_follow(request, username):
    user = get_object_or_404(get_user_model(), username=username)
    is_follow = False
    if user in request.user.from_user.all():
        request.user.from_user.remove(user)
    elif user != request.user:
        request.user.from_user.add(user)
        is_follow = True
    return JsonResponse({'is_follow': is_follow}, json_dumps_params={'ensure_ascii': True})

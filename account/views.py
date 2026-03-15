from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def user_login(request):
    if request.user.is_authenticated:
        return redirect('home_app:home')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')


        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home_app:home')

    return render(
        request,
        'account/login.html',
    )

def user_register(request):
    if request.user.is_authenticated:
        return redirect('home_app:home')

    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        if password != password2:
            messages.error(request, 'Passwords do not match')
            return render(
                request,
                "account/register.html",
            )

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists')
            return render(
                request,
                "account/register.html",
            )

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists')
            return render(
                request,
                "account/register.html",
            )

        user = User.objects.create_user(username=username, email=email, password=password)
        login(request, user)
        return redirect('home_app:home')
    return render(
        request,
        "account/register.html",
    )
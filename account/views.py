from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login

# Create your views here.
def user_login(request):
    print('hi my name is def user_login ヾ(•ω•`)o')
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')


        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')

    return render(
        request,
        'account/login.html',
    )

def user_register(request):

    return render(
        request,
        "account/register.html",
        context={

        }
    )
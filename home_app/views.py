from django.shortcuts import render, redirect
from django.contrib.auth import logout

# Create your views here.
def home(request):
    return render(
        request,
        'home_app/index.html'
    )

def log_out(request):
    logout(request)
    return redirect('account:login')
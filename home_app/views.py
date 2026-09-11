from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout
from blog.models import BlogPost

# Create your views here.
def home(request):
    return render(
        request,
        'home_app/index.html',
        context={
            'articels_most_likes': BlogPost.obj.most_likes(),
            'articel_offr_admin' : BlogPost.obj.offers_admin(),
        }
    )

def log_out(request):
    logout(request)
    return redirect('account:login')
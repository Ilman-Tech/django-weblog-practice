from django.urls import path
from .views import *

app_name = 'blog'

urlpatterns = [
    path('blog/<slug:slug>', blog_detail, name='blog_detail'),
    path('blog-list/', blog_list, name='blog_list'),
]
from django.contrib import admin
import django
from django.urls import path


urlpatterns = [
    path('admin/', admin.site.urls),
]

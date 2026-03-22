from django.contrib import admin
from .models import BlogPost
# Register your models here.
for i in [BlogPost]:
    admin.site.register(i)
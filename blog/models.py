from django.db import models
from django.contrib.auth.models import User

class BlogPost(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_DEFAULT, default=1)
    title = models.CharField(max_length=60)
    body = models.TextField()
    curren_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    img = models.ImageField(upload_to="blog/img/", blank=True)

    def __str__(self):
        return f"{self.title} - {self.author}"
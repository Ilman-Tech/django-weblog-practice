from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
# from django.utils import timezone
from datetime import timedelta
import uuid

def getnerate():
    return uuid.uuid4()

class Category(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.title}"

class BlogPostManager(models.Manager):
    def counter(self):
        return self.all().count()

    def actually(self):
        return self.all().count() * 3

    def recant_posts(self):
        return self.all().order_by('-curren_time')[:5]

    def last_update_post(self):
        return self.all().order_by('-update_time')[:5]

    def most_likes(self):
        return self.all().order_by('-likes')[:6]

    def offers_admin(self):
        return self.all().filter(is_admin_pick=True).order_by('-curren_time')[:3]

class BlogPost(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_DEFAULT, default=1)
    category = models.ManyToManyField(Category, related_name='blog_posts')
    title = models.CharField(max_length=60)
    body = models.TextField()
    curren_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    img = models.ImageField(upload_to="blog/img/", blank=True)
    binary_file = models.BinaryField(null=True, blank=True)
    is_admin_pick = models.BooleanField(default=False)
    likes = models.IntegerField(default=0)
    objects = models.Manager()
    obj = BlogPostManager()

    # این فیلد فقط طمان رو ذخیره میکنه
    # TestTimeFild = models.TimeField()

    # این فیلد هم فقط تاریخ رو ذخیره میکنه
    # TestDatefield = models.DateField()

    # این مدل زیر هم میتونیم برای اشتراک چقدر مونده و... استفاده کنیم
    # TestDurationField = models.DurationField(default=timedelta(days=16, hours=2, minutes=30, seconds=30))

    slug = models.SlugField(max_length=300, unique=True, editable=False)

    def save(
        self,
        *,
        force_insert = False,
        force_update = False,
        using = None,
        update_fields = None,
    ):
        self.slug = slugify(self.title)
        super(BlogPost, self).save()


    def get_absolute_url(self):
        return reverse("blog:blog_detail", kwargs={"slug": self.slug})

    def __str__(self):
        return f"{self.title} - {self.author}"
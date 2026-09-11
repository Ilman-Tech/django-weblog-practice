from django.contrib import admin
from .models import BlogPost, Category
# Register your models here.

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = [v.name for v in BlogPost._meta.fields if v.name not in ['body', 'binary_file']]
    list_display_links = [v.name for v in BlogPost._meta.fields if v.name not in ['img', 'body', 'binary_file']]
    list_filter = ('is_admin_pick',)
    readonly_fields = ("slug",)

for i in [Category]:
    admin.site.register(i)
from blog.models import BlogPost, Category

def recent(request):
    context = {
        'recent_posts' : BlogPost.obj.recant_posts(),
        'recent_update' : BlogPost.obj.last_update_post(),
        'categorys' : Category.objects.all()
    }

    return context
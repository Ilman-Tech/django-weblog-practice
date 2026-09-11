from django.shortcuts import render, get_object_or_404

from blog.models import BlogPost, Category


# Create your views here.
def blog_detail(request, slug):
    return render(
            request,
            'blog/post-details.html',
            context={
                'blog' : get_object_or_404(BlogPost, slug=slug),
            }
    )

def blog_list(request):

    category = request.GET.get('category')

    if category:
        cat = get_object_or_404(Category, pk=category)
        blog = cat.blog_posts.all()
    else:
        blog = BlogPost.objects.all()

    context = {
        'blogs' : blog,
    }
    return render(
        request,
        'blog/blog_list.html',
        context=context
    )

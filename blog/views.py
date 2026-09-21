from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from blog.models import BlogPost, Category


# Create your views here.
def blog_detail(request, slug):
    return render(
        request,
        'blog/post-details.html',
        context={
            'blog': get_object_or_404(BlogPost, slug=slug),
        }
    )


def blog_list(request):
    category = request.GET.get('category', None)
    items = request.GET.get('items', '2')
    page_number = request.GET.get('page')

    posts = BlogPost.objects.all().order_by("-id")

    if category and category.isdigit():
        cat = get_object_or_404(Category, id=category)
        posts = cat.blog_posts.all().order_by("-id")

    if items == 'all':
        page_range = None
        page_obj = posts
    else:
        try:
            pre_page = int(items)
        except ValueError:
            pre_page = 2

        paginator = Paginator(posts, pre_page)
        page_obj = paginator.get_page(page_number)

        page_range = range(
            max(1, page_obj.number - 1),
            min(page_obj.paginator.num_pages, page_obj.number + 1) + 1
        )

    return render(
        request,
        'blog/blog_list.html',
        context={
            'page_obj': page_obj,
            'page_range': page_range,
            'items': items,
        }
    )

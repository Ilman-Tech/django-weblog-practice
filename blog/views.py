from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
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
    items = request.GET.get('items', '2')
    page_number = request.GET.get('page')

    if items == 'all':
        page_objects = BlogPost.objects.all().order_by('-id')
        return render(
            request,
            'blog/blog_list.html',
            context={
                'page_obj': page_objects,
                'page_range': None,
                "items": items,
            }
        )

    try:
        p = Paginator(BlogPost.objects.all(), int(items))
    except ValueError:
        p = Paginator(BlogPost.objects.all(), 2)

    page_obj = p.get_page(page_number)

    page_range = range(
        max(1, page_obj.number - 1),
        min(page_obj.paginator.num_pages , page_obj.number +1 ) +1,
    )

    return render(
        request,
        'blog/blog_list.html',
        {
            'page_obj' : page_obj,
            'page_range' : page_range,
            "items" : items,
        }
    )


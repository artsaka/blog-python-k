from django.shortcuts import render
from django.http import HttpResponse
from category.models import Category
from .models import Blogs
from django.core.paginator import Paginator, EmptyPage, InvalidPage

# Create your views here.
def index(request):
    # return HttpResponse("<h1>Hello World! I am Django Framework!</>")
    categories = Category.objects.all()
    blogs = Blogs.objects.all()
    latest = Blogs.objects.all().order_by('-pk')[:2]

    # popularity articles, gets the highest number of views for three articles
    popular = Blogs.objects.all().order_by('-views')[:3]

    # suggestion articles, gets the least number of views for three 
    suggestion = Blogs.objects.all().order_by('views')[:3]

    # paginator setting number of articles per page
    paginator = Paginator(blogs, 4)
    # clickable next group of pages 
    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1

    # rendering blogs per page
    try:
        blogPerPage = paginator.page(page)
    except(EmptyPage, InvalidPage):
        # if not available, live at the last page
        blogPerPage = paginator.page(paginator.num_pages)       

    return render(request, "frontend/index.html", {'categories': categories, 'blogs':blogPerPage, 'latest':latest, 'popular':popular, 'suggestion': suggestion })

def blogDetail(request, id):
    categories = Category.objects.all()
    popular = Blogs.objects.all().order_by('-views')[:3]
    suggestion = Blogs.objects.all().order_by('views')[:3]

    singleBlog = Blogs.objects.get(id=id)
    # iterate number of view blog
    singleBlog.views = singleBlog.views + 1
    singleBlog.save()
    return render(request, "frontend/blogDetail.html", {"blog": singleBlog, 'categories': categories, 'popular':popular, 'suggestion': suggestion})

def searchCategory(request, cat_id):
    blogs = Blogs.objects.filter(category_id=cat_id)
    popular = Blogs.objects.all().order_by('-views')[:3]
    suggestion = Blogs.objects.all().order_by('views')[:3]
    categoryName = Category.objects.get(id=cat_id)
    categories = Category.objects.all()
    return render(request, "frontend/searchCategory.html", {"blogs": blogs,'categories': categories, 'popular':popular, 'suggestion': suggestion, 'categoryName': categoryName})

def searchWriter(request, writer):
    blogs = Blogs.objects.filter(writer = writer)

    categories = Category.objects.all()
    popular = Blogs.objects.all().order_by('-views')[:3]
    suggestion = Blogs.objects.all().order_by('views')[:3]

    return render(request, "frontend/searchWriter.html", {"blogs": blogs,'categories': categories, 'popular':popular, 'suggestion': suggestion, 'writer':writer})
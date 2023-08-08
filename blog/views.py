from django.shortcuts import render,redirect
from django.http.response import HttpResponse
from blog.models import Blog, Category   


data = {
    "blogs" : [
        {
            "id" : 1,
            "title": "komple web geliştirme",
            "image" : "1.jpeg",
            "is_active" : True,
            "is_home" : True,
            "description" : "başari orai yüksek",
        },

        {
            "id" : 2,
            "title": "python",
            "image" : "2.jpeg",
            "is_active" : True,
            "is_home" : True,
            "description" : "başari orani yüksek",
        },

        {
            "id" : 3,
            "title": "django",
            "image" : "3.jpeg",
            "is_active" : True,
            "is_home" : True,
            "description" : "başari orani yüksek",
        }
    ]
}

# Create your views here.

def index (request):
    if not request.user.is_authenticated:
       return redirect("login")

    context = {
        "blogs" : Blog.objects.filter(is_home=True, is_active=True),
        "categories" : Category.objects.all()
    }

    return render (request, "blog/index.html", context)
def blogs (request):
    if not request.user.is_authenticated:
       return redirect("login")   
    context = {
        "blogs" : Blog.objects.filter(is_active=True),
        "categories" : Category.objects.all()

    }
    return render (request, "blog/blogs.html", context)

def blog_details (request, slug):
    if not request.user.is_authenticated:
       return redirect("login")       
    blog = Blog.objects.get(slug=slug)
    return render (request, "blog/blog-details.html", {
        "blog": blog
    })

def blogs_by_category (request, slug):
    if not request.user.is_authenticated:
       return redirect("login")       
    context = {
        "blogs" : Category.objects.get(slug=slug).blog_set.filter(is_active=True),
        #"blogs":Blog.objects.filter(is_active=True, category__slug=slug),
        "categories": Category.objects.all(),
        "selected_category" : slug
        
    
    }
    return render(request, "blog/blogs.html", context)
from django.shortcuts import render,redirect
from django.http.response import HttpResponse
from blog.models import Blog, Category   



def index (request):
    if not request.user.is_authenticated:
       return redirect("login")

    context = {
        "blogs" : Blog.objects.filter(is_home=True, is_active=True),
        "categories" : Category.objects.all()
    }

    return render (request, "blog/index.html", context)

def blogs (request):
    context = {
        "blogs" : Blog.objects.filter(is_active=True),
        "categories" : Category.objects.all()

    }
    return render (request, "blog/blogs.html", context)

def blog_details (request, slug):
    
    if not request.user.is_authenticated:
       return redirect("login")       
    blog = Blog.objects.get(slug=slug)
    category = blog.categories
    return render (request, "blog/blog-details.html", {
        "blog": blog,
    })

def blogs_by_category (request, slug):
     
    context = {
        "blogs" : Category.objects.get(slug=slug).blog_set.filter(is_active=True),
        "blog" :Category.objects.filter(slug=slug),
        #"blogs":Blog.objects.filter(is_active=True, category__slug=slug),
        "categories": Category.objects.all(),
        "selected_category" : slug
    }
    return render(request, "blog/blogs.html", context)

def musterikayit (request):
    if not request.user.is_authenticated:
           return redirect("home")
     

    yenimusteri = Category()
    if request.method == "POST":
        yenimusteri = Category()
        name = request.POST["musteriadi"]
        yenimusteri.name = name
        mail = request.POST["musterimail"]
        yenimusteri.mail = mail
        telefon = request.POST["musteritelefon"]
        yenimusteri.telefon = telefon
        adres = request.POST["musteriadres"]
        yenimusteri.adres = adres
        yenimusteri.save()
    return render(request, "blog/musterikayit.html")

from django.shortcuts import render
from .models import TechBlog

# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'service.html')

def projects(request):
    return render(request, 'project.html')

def blogs(request):
    all_blogs = TechBlog.objects.all()
    print(all_blogs)
    return render(request, 'blog.html', {'all_blog':all_blogs})

def get_blog_details(request,id):
    blog = TechBlog.objects.get(id=id)
    print("blog details", blog)
    return render(request, 'get_blog_details.html', {'get_blog':blog})
    
def contact(request):
    return render(request, 'contact.html')

from django.urls import path
from .views import index,about,contact,services,projects,blogs,get_blog_details
urlpatterns = [
    path('', index, name='index'),
    path('about', about, name='about'),
    path('contact',contact , name='contact'),
    path('services', services, name='services'),
    path('projects', projects, name='projects'),
    path('blogs', blogs, name='blogs'),
    path('blog/<int:id>/', get_blog_details, name='blog'),
]

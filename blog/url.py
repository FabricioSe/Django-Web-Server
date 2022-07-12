
from django.urls import path
from . import views ###. -> Current directory

urlpatterns = [
    #path('home/', views.home, name="blog-home"), ###  localhost:8000/blog/home
    path('', views.home, name="blog-home"), ###  localhost:8000/blog/home, without mentioning home/
    path('about/', views.about, name="blog-about"), ###  localhost:8000/blog/about
    path('contact/', views.contact, name="blog-contact") ###  localhost:8000/blog/contact
]


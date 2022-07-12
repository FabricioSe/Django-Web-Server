from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.
# Inyection of data in a HTML page
posts = [
    {
        'author':'Marry',
        'title':'Blog Post 1',
        'content':'The Fist Post Content',
        'date_posted':'November 20, 2021'       
    },
    {
        'author':'Anna',
        'title':'Blog Post 2',
        'content':'The Second Post Content',
        'date_posted':'November 25, 2021'
    }
]

def home(request):
    #return HttpResponse("<h1>Welcome To Our Home Page</h1>")
    #return render(request, 'blog/home.html', {'post':posts, 'title':'Home'}) ## dummy data
     return render(request, 'blog/home.html', {'posts':Post.objects.all(), 'title':'Home'})
    
def about(request):
    #return HttpResponse("<h1>Our About Page</h1>")
    return render(request, 'blog/about.html', {'title':'About'})

def contact(request):
    return render(request, 'blog/contact.html')
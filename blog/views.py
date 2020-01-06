from django.shortcuts import render
from django.http import HttpResponse


posts = [
    {
        'author' : 'Lionel',
        'title' : 'blog post 1',
        'content' : 'First post content',
        'date_posted' : 'January 06, 2020',
    },
     {
        'author' : 'Jane doe',
        'title' : 'blog post 2',
        'content' : 'Second post content',
        'date_posted' : 'January 06, 2020',
    }
]

# Create your views here.

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})


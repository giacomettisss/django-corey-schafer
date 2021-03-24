from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


posts = [
    {
        'author' : 'CoreyMs',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'August 27,2028'
    },
    {
        'author' : 'Marcelo',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'August 28,2028'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
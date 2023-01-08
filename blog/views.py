from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'Tommi',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'January 7, 2023'
    },
    {
        'author': 'Aija',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'January 8, 2023'
    } 
]

def home(request):
    context = {
            'posts': posts,
            'title': 'Home'
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html')

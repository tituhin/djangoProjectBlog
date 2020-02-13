from django.shortcuts import render
from django.http import HttpResponse


posts = [
    {
        'author': 'Tariqul Islam',
        'title': "Blog Post",
        'content': 'First post content',
        'date_posted': 'August 11,2019'
    },
    {
        'author': 'Saddam Hossain',
        'title': "Blog Post 2",
        'content': 'First post content',
        'date_posted': 'February 12,2019'
    },
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', { 'title' : 'About'} )

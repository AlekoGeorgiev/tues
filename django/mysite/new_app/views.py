from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    context = {
        'title':'Home',
        'content':'Welcome to the homepage',
    }
    return render(request, 'new_app/home.html', context)

def index(request):
    context = {
        'title':'Index Page',
        'content':'I don\'t know why this page exists',
    }
    return render(request, 'new_app/home.html', context)

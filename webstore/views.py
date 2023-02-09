from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from .models import *

# Create your views here.

def index(request): 
    announcement = telephones_Base.objects.all()
    return render(request, 'webstore/index.html', {'title': 'Webstore', 'announcement': announcement})

def login(request):
    return render(request, 'webstore/login.html', {'title': 'Sign in'})

def pageNotFound(request,exception):
    return HttpResponseNotFound('<h1>Page not found</h1>')

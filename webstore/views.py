from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.

def index(request): 
    return render(request, 'webstore/index.html', {'title': 'Webstore'})

def login(request):
    return render(request, 'webstore/login.html', {'title': 'Sign in'})

def pageNotFound(request,exception):
    return HttpResponseNotFound('<h1>Page not found</h1>')

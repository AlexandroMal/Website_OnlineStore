from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from .models import *

# Create your views here.

def index(request): 
    announcement = product_data.objects.all()
    categories = Category.objects.all()
    print(categories)
    context = {
        'title' : 'Webstore',
        'categories': categories,
        'announcement': announcement,    
    }
    
    return render(request, 'webstore/index.html', context=context)

def category_show(request, cat_id):
    announcement = product_data.objects.filter(category=cat_id)
    categories = Category.objects.all()
    print(categories)
    context = {
        'title' : 'Category',
        'categories': categories,
        'announcement': announcement,    
    }
    
    return render(request,'webstore/index.html', context=context)

def login_user(request):
    return render(request, 'webstore/login.html', {'title': 'Sign in'})

def register_user(request):
    return render(request, 'webstore/registration.html', {'title': 'Sign up'})

def pageNotFound(request,exception):
    return HttpResponseNotFound('<h1>Page not found</h1>')

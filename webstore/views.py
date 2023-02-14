from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpResponse, HttpResponseNotFound
from django.views.generic import ListView, DetailView, CreateView
from .models import *
from .forms import *

# Create your views here.

class WebstoreHome(ListView):
    model = product_data
    template_name = 'webstore/index.html'
    context_object_name = 'announcement'
    extra_context = {'title': 'Webstore'}


class ShowCategory(ListView):
    model = product_data
    template_name = 'webstore/index.html'
    context_object_name = 'announcement'
    extra_context = {'title': 'Webstore'}
    allow_empty = False
    
    def get_queryset(self):
        return product_data.objects.filter(category__slug=self.kwargs['cat_slug'])

class ShowPost(DetailView):
    model = product_data
    template_name = 'webstore/post.html'
    slug_url_kwarg = 'slug_post'
    context_object_name = 'post'
    
    def get_context_data(self,*, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context['post']
        return context
    
class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'webstore/registration.html'
    success_url = reverse_lazy('login_page')




def login_user(request):
    return render(request, 'webstore/login.html', {'title': 'Sign in'})

def pageNotFound(request,exception):
    return HttpResponseNotFound('<h1>Page not found</h1>')

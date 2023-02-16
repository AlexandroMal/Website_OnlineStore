from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.http import  HttpResponseNotFound
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout, login
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
    
    def get_context_data(self,*, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Sign Up'
        return context
    
    def form_valid(self, form):
        user = form.save()
        login(self.request,user)
        return redirect('home_page')

class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'webstore/login.html'
    
    def get_context_data(self,*, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Sign In'
        return context

    def get_success_url(self):
        return reverse_lazy('home_page')


def logout_user(request):
    logout(request)
    return redirect('home_page')


def pageNotFound(request,exception):
    return HttpResponseNotFound('<h1>Page not found</h1>')

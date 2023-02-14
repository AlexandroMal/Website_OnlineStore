from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import *

class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'placeholder': 'Enter username'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'placeholder': 'Enter email'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'placeholder': 'Enter password'}))   
    password2 = forms.CharField(label='Password again', widget=forms.PasswordInput(attrs={'placeholder': 'Enter password again'}))
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
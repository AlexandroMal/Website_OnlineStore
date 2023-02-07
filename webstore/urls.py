from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="home_page"),
    path('login/', login, name="login_page")
   
    
]


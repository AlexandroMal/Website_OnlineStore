from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="home_page"),
    path('login/', login_user, name="login_page"),
    path('registration/', register_user, name="registration_page"),
    path('category/<int:cat_id>/', category_show, name="category"),
    path('post/<int:id>/', post_show, name="post"),
    
]


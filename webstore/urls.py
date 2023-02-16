from django.urls import path
from .views import *

urlpatterns = [
    path('', WebstoreHome.as_view(), name="home_page"),
    path('login/', LoginUser.as_view(), name="login_page"),
    path('register/', RegisterUser.as_view(), name="registration_page"),
    path('logout/', logout_user, name="logout"),
    path('category/<slug:cat_slug>/', ShowCategory.as_view(), name="category"),
    path('post/<slug:slug_post>/', ShowPost.as_view(), name="post"),
    
]


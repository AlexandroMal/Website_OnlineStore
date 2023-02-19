from django.urls import path, include
from .views import *

app_name = 'cart'

urlpatterns = [
    path('cart/', include([
        path('', cart_list, name='cart_list'),
        path('<id>/add/', add_to_cart, name='add'),
        path('<id>/remove/', remove_cart, name='remove'),
        path('delete/', delete_cart, name='delete'),
    ])),
]
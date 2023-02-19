from django.shortcuts import render, redirect
from webstore.models import *

def cart_list(request):
    product_ids = request.session.get('cart', [])
    print(product_ids)
    id_list = [int(x) for x in product_ids]
    products = product_data.objects.filter(id__in=id_list)
    context = {'products': products}
    
    return render(request, 'webstore/basket.html', context=context)


def add_to_cart(request, id):
    if request.method == 'POST':
        if not request.session.get('cart'):
            request.session['cart'] = list()
            print('Create new session')
                
        else:
            request.session['cart'] = list(request.session['cart'])
            print('Session be created')
            
            
        cart_list = []
        for item in request.session.get('cart', []):
            cart_list.append(item)
        if id not in cart_list:
            cart_list.append(id)
    
    
        request.session['cart'] = cart_list
        request.session.modified = True
        
    return redirect(request.POST.get('url_from'))


def remove_cart(request, id):
    if request.method == 'POST':
        
        for item in request.session.get('cart', []):
            if item == id:
                request.session.get('cart', []).remove(item)
        request.session.modified = True
                    
        if not request.session.get('cart'):
            del request.session ['cart']
    
    request.session.modified = True
    return redirect(request.POST.get('url_from'))
  
  
def delete_cart(request):
    if request.session.get('cart'):
        del request.session['cart']
        
    return redirect(request.POST.get('url_from'))
    
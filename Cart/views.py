from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from Catalog.models import Product

def add_to_cart(request, honey_id):
    cart = request.session.get('shopping_cart', {})
    if honey_id not in cart:
        product = get_object_or_404(Product, pk=honey_id)
        # if product is found, add to the cart
        cart[honey_id] = {
            'id': honey_id,
            'title': Product.name,
            'price': Product.price
        }
        # save the cart back to sessions
        request.session['shopping_cart'] = cart
              
        messages.success(request, "Your product has been added to your cart!")
        return redirect('show_products')
        
    else:
        return redirect('show_products')
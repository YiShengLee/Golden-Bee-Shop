from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from Catalog.models import Product

# Add product to cart section
@login_required(login_url='/accounts/login/')
def add_to_cart(request, id):
    cart = request.session.get('shopping_cart', {})
    
    # we check if the id is not in the cart. If so, we will add it
    if id not in cart:
        honey = get_object_or_404(Product, pk=id)
        # honey is found, let's add it to the cart
        cart[id] = {
            'id':id,
            'name': honey.name,
            'price': str(honey.price),
            'image_url':honey.image.cdn_url,
            'quantity':1,
            'total_price':float(honey.price),
            }
        
        # save the cart back to sessions
        request.session['shopping_cart'] = cart
        messages.success(request, "Item has been added to your cart")
        return redirect('show_products')

        
    else:
        cart[id]['quantity']+=1
        cart[id]['total_price'] = round(int(cart[id]['quantity']) * float(cart[id]['price']),2)
        request.session['shopping_cart'] = cart
        return redirect('/cart/')


# View what item had been added to cart    
def view_cart(request):
    # retrieve the cart
    cart = request.session.get('shopping_cart', {})
    grand_total_price = 0.00
    for id,honey in cart.items():
        grand_total_price += honey['total_price']
    
    return render(request, 'view_cart.template.html', {
        'shopping_cart':cart,
        'grand_total_price':round(grand_total_price, 2)
    })

def total_price(request,id):
    honey = get_object_or_404(Product, pk=id)
    cart = request.session.get('shopping_cart', {})
    cart[id] = {
    'id':id,
    'name': honey.name,
    'price': str(honey.price),
    'image_url':honey.image.cdn_url,
    'quantity':cart['quantity'],
    'total_price':round(int(cart[id]['quantity']) * float(cart[id]['price']),2)
    }
    request.session['shopping_cart'] = cart
    return render(request, 'view_cart.template.html', {
            'total_price':total_price
        })        

def minus_from_cart(request, id):
    cart = request.session.get('shopping_cart', {})
    if id in cart:
        game = get_object_or_404(Product, pk=id) 
        if cart[id]['quantity'] > 1:
            cart[id]['quantity']-=1
            print(cart[id]['quantity'])
            cart[id]['total_price'] = round(int(cart[id]['quantity']) * float(cart[id]['price']),2)
        # save the cart back to sessions
            request.session['shopping_cart'] = cart
        return redirect('/cart/')

    
# Remove item from cart
def delete_from_cart(request, id):
    # retrieve the cart from session
    cart = request.session.get('shopping_cart',{})
    
    # if the course is in the cart
    if id in cart:
        # remove it from the cart
        del cart[id]
        # save back to the session
        request.session['shopping_cart'] = cart
        messages.success(request, "Item removed from cart successfully!")
        
    return redirect('/cart/')
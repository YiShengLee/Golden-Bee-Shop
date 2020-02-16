from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from Catalog.models import Product

# Add product to cart section
def add_to_cart(request, id):
    # cart = request.session.get('shopping_cart', {})
    # if id not in cart:
    #         product = get_object_or_404(Product, pk=id)
    #         # course is found, let's add it to the cart
    #         cart[id] = {
    #             'id':id,
    #             'name': product.name,
    #             'price': product.price
    #         }
            
    #         # save the cart back to sessions
    #         request.session['shopping_cart'] = cart
    #         messages.success(request, "Your product has been added to your cart!")
     
        
    # else:
    #     # cart[id] = int(cart[id])
    #     return redirect(reverse('show_products'))
    


    # Working
    # cart = request.session.get('cart', {})
    # if id in cart:
    #     cart[id] = cart[id]
    # else:
    #     product = get_object_or_404(Product, pk=id)
    #     cart[id] = {
    #         'id':id,
    #         'name':product.name
    #     }
    # messages.success(request, "Item has been added to cart!")
    # request.session['cart'] = cart
    # return redirect(reverse('show_products'))
    
    cart = request.session.get('shopping_cart', {})
    
    # we check if the game_id is not in the cart. If so, we will add it
    if id not in cart:
        honey = get_object_or_404(Product, pk=id)
        # game is found, let's add it to the cart
        cart[id] = {
            'id':id,
            'name': honey.name,
            'price': str(honey.price),
            # 'image_url':honey.image.cdn_url,
            }
        
        # save the cart back to sessions
        request.session['shopping_cart'] = cart
        messages.success(request, "Game has been added to your cart")
        return redirect('show_products')

        
    else:
        request.session['shopping_cart'] = cart
        return redirect('/cart/')

    
def view_cart(request):
    # retrieve the cart
    cart = request.session.get('shopping_cart', {})
    
    return render(request, 'view_cart.template.html', {
        'shopping_cart':cart
    })
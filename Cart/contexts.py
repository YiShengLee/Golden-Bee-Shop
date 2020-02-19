from django.shortcuts import get_object_or_404
from Catalog.models import Product


def cart_contents(request):
    # make the content of the shopping cart available to all templates
    cart = request.session.get("shopping_cart", {})
    
    cart_items = []
    total = 0
    item_count = 0
    
    
    for id, quantity in cart.items():
        product = get_object_or_404(Product, pk=id)
        total = product.price
        cart_items.append({
            'id': id,
            'product': product
        })
        
    
    return {
        'shopping_cart':cart,
        'number_of_items':len(cart)
    }
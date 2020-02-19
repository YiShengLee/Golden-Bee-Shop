from django.shortcuts import render, reverse, HttpResponse, get_object_or_404
from .forms import OrderForm, PaymentForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from .models import Charge  , LineItem

#import settings so that we can access the public stripe key
from django.conf import settings
import stripe
from Cart.models import CartProduct

from Catalog.models import Product

# Donate Section
def donate(request):
    return render(request, 'donate.template.html')

def calculate_cart_cost(request):
    cart = request.session.get('cart', {})
    amount = 0
    for id, quantity in cart.items():
        product = get_object_or_404(Product, pk=id)
        amount = Product.price
        print(amount)

    return amount


# Checkout Section
@login_required        
def checkout(request):
    all_products = CartProduct.objects.filter(owner=request.user)
    total_cost = calculate_cart_cost(request)
    return render(request, 'checkout.template.html') 





# Checkout Sucess Section
def checkout_success(request):
    return render(request, 'checkout_success.template.html')
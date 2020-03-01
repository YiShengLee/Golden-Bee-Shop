from django.shortcuts import render, reverse, HttpResponse, get_object_or_404
from .forms import OrderForm, PaymentForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from .models import Charge

#import settings so that we can access the public stripe key
from django.conf import settings
import stripe

from .forms import OrderForm, PaymentForm
from Cart.models import CartProduct
from Catalog.models import Product
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone

# Charge Section
@login_required    
def charge(request):
        amount = request.GET['amount']
        if request.method == 'GET':
            order_form = OrderForm()
            payment_form = PaymentForm()
            
            #show form
            return render(request, 'charge.template.html', {
                'publishable' : settings.STRIPE_PUBLISHABLE_KEY,
                'order_form' : OrderForm,
                'payment_form' : PaymentForm,
                'amount': amount,
            })
        
        else:
            # set secret key for Stripe API
            stripeToken = request.POST['stripe_id']
            stripe.api_key = settings.STRIPE_SECRET_KEY
            
            order_form = OrderForm(request.POST)
            payment_form = PaymentForm(request.POST)
    
            if order_form.is_valid() and payment_form.is_valid():
                try:
                    customer = stripe.Charge.create(
                            # stripe only accepts cents hence *100 and integer
                            amount=int(float(request.POST['amount'])*100),
                            currency='sgd',
                            description='Payment',
                            card=stripeToken
                        )
                
                    if customer.paid:
                        order = order_form.save(commit=False)
                        order.date = timezone.now()
                        order.save()
                        request.session['shopping_cart'] = {}
                        return render(request, 'checkout_success.template.html')
                    
                    else:
                        messages.error(request, "Your card has been declined!")
                        
                except stripe.error.CardError:
                        messages.error(request, "Your card was declined!")
                    
            else:
                 return render(request, 'charge.template.html', {
                'order_form' : OrderForm,
                'payment_form' : PaymentForm,
                'amount': amount,
                'publishable' : settings.STRIPE_PUBLISHABLE_KEY
            })



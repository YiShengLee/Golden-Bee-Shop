from django.shortcuts import render, reverse, HttpResponse, get_object_or_404
from .forms import OrderForm, PaymentForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone

#import settings so that we can access the public stripe key
from django.conf import settings
import stripe

from Catalog.models import Product

# Donate Section
def donate(request):
    return render(request, 'donate.template.html')


            

# Checkout Section
def checkout_success(request):
    return render(request, 'checkout_success.template.html')
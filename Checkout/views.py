from django.shortcuts import render, reverse, HttpResponse, get_object_or_404

#import settings so that we can access the public stripe key
from django.conf import settings
import stripe

from Catalog.models import Product

def donate(request):
    return render(request, 'donate.template.html')
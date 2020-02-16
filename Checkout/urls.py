from django.urls import path
from .views import donate, checkout, checkout_success

urlpatterns = [
    path('', checkout, name='checkout'),
    path('donate/', donate, name='donate'),
    path('success/', checkout_success),
]
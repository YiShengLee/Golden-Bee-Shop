from django.urls import path
from .views import donate, checkout_success

urlpatterns = [
    
    path('donate/', donate, name='donate'),
    path('success/', checkout_success),
]
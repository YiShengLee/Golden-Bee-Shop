from django.urls import path
from .views import add_to_cart

urlpatterns = [
  path('add/<honey_id>',add_to_cart, name="add_cart"),
]
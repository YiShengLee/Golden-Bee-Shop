from django.urls import path
from .views import add_to_cart, view_cart, delete_from_cart

urlpatterns = [
  path('add/<id>',add_to_cart, name="add_to_cart"),
  path('',view_cart, name="view_cart"),
  path('remove/<id>', delete_from_cart, name='delete_from_cart'),
]
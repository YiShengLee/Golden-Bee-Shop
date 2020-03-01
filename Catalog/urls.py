from django.urls import path
from .views import show_products, create_product, edit_product, delete_product, show_categories, create_category, honey_info

urlpatterns = [
    path('products/',show_products, name="show_products"),
    path('products_info/<id>',honey_info, name="honey_info"),
    path('create_product/',create_product, name="create_product"),
    path('edit_product/<id>', edit_product, name='edit_product'),
    path('delete_product/<id>', delete_product, name="delete_product"),
    path('categories/', show_categories, name="show_categories"),
    path('create_category/', create_category, name='create_category'),
]
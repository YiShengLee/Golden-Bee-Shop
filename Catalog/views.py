from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .forms import ProductForm
from .models import Product

# Create your views here.
def index(request):
    return render(request,'index.template.html')

# Show Product Section
def show_products(request):
    all_products = Product.objects.all()
    return render(request,'products.template.html',{
        'catalog':all_products
    })

# Create Product Section
def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST) #create a form
        # User submitted form
        if form.is_valid():
            form.save()
            return redirect(show_products)
        
    else:
        product_form = ProductForm()
        return render(request,'create_product.template.html',{
            'form':product_form
        })

# Edit Product Section
def edit_product(request,id):
    #pk means primary key
    product_edited = get_object_or_404(Product, pk=id)
    
    if request.method == 'POST':
        form = ProductForm(request.POST,instance=product_edited)
        if form.is_valid():
            form.save()
            return redirect(show_products)
        else:
            print(form.errors)
            return HttpResponse("Errors")
    
    else:
        edit_form = ProductForm(instance=product_edited)
        return render(request, 'edit_product.template.html', {
            'form':edit_form
        })        

# Delete Product Section
def delete_product(request, id):
    product_being_deleted = get_object_or_404(Product, pk=id)
    product_being_deleted.delete()
    return redirect(show_products)
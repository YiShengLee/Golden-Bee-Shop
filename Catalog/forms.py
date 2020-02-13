from django import forms
from .models import Product , Category
from pyuploadcare.dj.forms import ImageField, FileWidget
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, MultiField, Div, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions

class ProductForm(forms.ModelForm):
    
    # image = ImageField(label="Upload Image", widget=FileWidget())
    
    # Set the label of the forms
    name = forms.CharField(label="Product Name",widget=forms.TextInput(attrs={'placeholder': 'Search'}))
    # Inner Class
    class Meta:
        model = Product
        fields = ('name', 'price', 'stock', 'Category', 'image') #all information must be create in models.py
        # widgets = {
        #  'name': forms.TextInput(attrs={'class': 'productname'}),
        #  }
    
    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(

            PrependedText('name','<img src="https://img.icons8.com/dotty/20/000000/product.png">'),
            Div(
                'price', 
                css_class='productprice'
            ),
            Div(
                'stock', 
                css_class='productstock'
            ),
            Div(
                'Category', 
                css_class='productCategory'
            ),
            Row(
                'image',
                css_class='productimage'
                ),
                
            # Submit('submit', 'Submit', css_class='btn')
        )
        
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name',)
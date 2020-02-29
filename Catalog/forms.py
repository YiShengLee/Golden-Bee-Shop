from django import forms
from .models import Product , Category
from pyuploadcare.dj.forms import ImageField, FileWidget
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, MultiField, Div, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions

class ProductForm(forms.ModelForm):
    
    # image = ImageField(label="Upload Image", widget=FileWidget())
    

    # Inner Class
    class Meta:
        model = Product
        fields = ('name', 'price', 'stock', 'Category', 'description', 'image') #all information must be create in models.py
        # widgets = {
        #  'name': forms.TextInput(attrs={'class': 'productname'}),
        #  }
    
    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            # Input name box
            Div(
                PrependedText('name','<img src="https://img.icons8.com/dotty/20/000000/product.png">', placeholder="Enter your product name"),
                css_class='productname',
                ),
            
            Div(
                PrependedText('price','<img src="https://img.icons8.com/dotty/20/000000/expensive-2.png">', placeholder="Enter the honey cost in (\u00A2)"),
                css_class='productprice'
                ),
            Div(
                PrependedText('stock','<img src="https://img.icons8.com/dotty/20/000000/garage-open.png">', placeholder="Enter the quantities of honey"),
                css_class='productstock'
                ),
            Div(
                PrependedText('Category', '<img src="https://img.icons8.com/dotty/20/000000/sorting-answers.png">'),
                css_class='productCategory'
                ),
            Div(
                PrependedText('description', '<img src="https://img.icons8.com/dotty/20/000000/create-new.png">'),
                css_class='productdes'
                ),    
            
            Row(
                'image',
                css_class='productimage'
                ),
                
            Submit('submit', 'Submit', css_class='btn btn-warning')
        )
        
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name',)
        
class CategorySearchForm(forms.Form):
    search_terms = forms.CharField(required=False)
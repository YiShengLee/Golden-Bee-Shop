from django.db import models
from pyuploadcare.dj.models import ImageField

# Create your models here.
# Create Product Field
class Product(models.Model):
     name = models.CharField(max_length=200, blank=False, verbose_name="Product Name")
     price = models.DecimalField(max_digits=6, decimal_places=2, blank=False)
     stock = models.IntegerField(blank=False, verbose_name="No of Unit")
     Category = models.ForeignKey("Category", blank=True, null=True, on_delete=models.SET_NULL, verbose_name="Type of Honey")
     image = ImageField(blank=True, verbose_name="Upload Product Image")
     
     def __str__(self):
               return self.name + " $" + str(self.price) + " (x" + str(self.stock) + ")"

# Create Category Field
class Category(models.Model):
    name = models.CharField(max_length=100, blank=False)
    
    def __str__(self):
        return "{}".format(self.name)


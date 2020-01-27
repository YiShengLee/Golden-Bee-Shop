from django.db import models

# Create your models here.
class Product(models.Model):
     name = models.CharField(max_length=200, blank=False)
     price = models.DecimalField(max_digits=6, decimal_places=2, blank=False)
     stock = models.IntegerField(blank=False)
     
     def __str__(self):
               return self.name + " $" + str(self.price) + " (x" + str(self.stock) + ")"


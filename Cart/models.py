from django.db import models

# Create your models here.
class CartProduct(models.Model):

    product = models.ForeignKey('Catalog.Product', on_delete=models.CASCADE)
    owner = models.ForeignKey('Accounts.MyUser', on_delete=models.CASCADE)
    quantity = models.IntegerField(blank=False, default=0)

    def __str__(self):
        return self.product.name + " x " + str(self.quantity)
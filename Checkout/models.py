from django.db import models

# Create your models here.
class Charge(models.Model):
    full_name = models.CharField(max_length=50, blank=False)
    phone_number = models.CharField(max_length=20, blank=False)
    country = models.CharField(max_length=40, blank=False)
    postcode = models.CharField(max_length=20, blank=True)
    town_or_city = models.CharField(max_length=40, blank=False)
    street_address1 = models.CharField(max_length=40, blank=False)
    street_address2 = models.CharField(max_length=40, blank=False)
    county = models.CharField(max_length=40, blank=False)
    date = models.DateField()

    def __str__(self):
        return "{0}-{1}-{2}".format(self.id, self.date, self.full_name)
        

class LineItem(models.Model):
    product = models.ForeignKey(
        'Catalog.Product',
        null=True,
        on_delete=models.CASCADE)
    name = models.CharField(max_length=255, blank=False)
    price = models.IntegerField(blank=False)
    quantity = models.PositiveIntegerField(default=1)

    def cost(self):
        return self.price * self.quantity
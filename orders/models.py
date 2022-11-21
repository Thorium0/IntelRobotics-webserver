from django.db import models
from djmoney.models.fields import MoneyField
from products.models import Product
import datetime

class Order(models.Model):
    customerName = models.CharField(max_length=50)
    customerAddress = models.CharField(max_length=100)
    created_on = models.DateTimeField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


    def __str__(self):
        return f'({self.id})[{self.created_on}]: {self.customerName} - {self.product}'
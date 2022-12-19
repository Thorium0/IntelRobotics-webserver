from django.db import models
from djmoney.models.fields import MoneyField
from django.core.validators import MinLengthValidator, MaxLengthValidator
from PIL import Image

class Product(models.Model):
    productName = models.CharField(max_length=100)
    productNo = models.IntegerField(unique=True, validators=[MaxLengthValidator(6),MinLengthValidator(6)])
    productPrice = MoneyField(max_digits=15, decimal_places=2, default_currency='DKK')
    productDesc = models.TextField(max_length=500)
    productImg = models.ImageField(upload_to='product_pics/', default='default-product.png')


    def save(self, **kwargs):
        super().save()
        img = Image.open(self.productImg.path)
        if img.height > 500 or img.width > 600:
            size = (300, 300)
            img.thumbnail(size)
            img.save(self.productImg.path)

    def __str__(self):
        return f'{self.productNo}: {self.productName}'
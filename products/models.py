from django.db import models
from PIL import Image

class product:
    productName = models.IntegerField()
    productNum = models.IntegerField()
    productPrice = models.FloatField()
    productDesc = models.TextField()
    productImg = models.ImageField(upload_to='product_pics/', default='default-product.png')



    def __str__(self):
        return f'{self.productName}'


    def save(self, **kwargs):
        super().save()
        img = Image.open(self.image.path)
        if img.height > 600 or img.width > 600:
            size = (600, 600)
            img.thumbnail(size)
            img.save(self.image.path)
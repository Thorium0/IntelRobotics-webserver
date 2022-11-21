from django import forms
from django.contrib.auth.models import User
from .models import Product


class ProductCreationForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ['productName', 'productPrice', 'productDesc', 'productImg']
        labels = {
            'productName': 'Product Name',
            'productPrice': 'Product Price',
            'productDesc': 'Product Description',
            'productImg': 'Product Image'
        }



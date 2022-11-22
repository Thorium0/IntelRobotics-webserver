from django.shortcuts import render
from .forms import ProductCreationForm
from .models import Product
from django.contrib import messages
import random

# Create your views here.

def create(request):
    if request.method == 'POST':
        form = ProductCreationForm(request.POST, request.FILES)

        if form.is_valid():

            product = form.save(commit=False)

            while True:
                productNo = random.randint(100000, 999999)
                try:
                    Product.objects.get(orderNo=productNo)
                except:
                    break
        
            product.productNo = productNo

            try: product.save()
            except:
                messages.warning(request, 'Could not create product')
            else:
                messages.success(request, 'Product Created')


    else:
        form = ProductCreationForm()
        
    context = {
    "title": "Products",
    "form": form
    }
    return render(request, 'products/create.html.django', context)



def product(request, productId):

    product = Product.objects.get(id=productId)

    context = {
        "title": "Product - "+product.productName,
        "product": product
    }
    return render(request, 'products/product.html.django', context)
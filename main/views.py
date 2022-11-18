from django.shortcuts import render
from django.core.files.storage import default_storage


def home(request):
    
    context = {
    "title" : "Robotsalg",
    }
    return render(request, 'main/home.html.django', context)


def faq(request):
    context = {
    "title" : "FAQ"
    }
    return render(request, 'main/faq.html.django', context)


def about(request):
    context = {
    "title" : "About us",
    }
    return render(request, 'main/about.html.django', context)

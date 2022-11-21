from django.shortcuts import render
from django.core.files.storage import default_storage
from django.contrib.auth.models import User


class Counter:
    count = 0

    def increment(self):
        self.count += 1
        return ''

    def decrement(self):
        self.count -= 1
        return ''

    def double(self):
        self.count *= 2
        return ''


def home(request):
    
    context = {
    "title" : "Products",
    }
    return render(request, 'main/home.html.django', context)


def contact(request):
    context = {
    "title" : "Contact"
    }
    return render(request, 'main/contact.html.django', context)


def about(request):

    users = User.objects.all()

    context = {
    "title" : "About us",
    "users": users,
    "counter": Counter()
    }
    return render(request, 'main/about.html.django', context)

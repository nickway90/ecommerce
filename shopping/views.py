from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import Item


def index(request):
    return render(request, 'shopping/index.html')


def cart(request):
    return render(request, 'cart/index.html')


def items(request):
    context = {
        'items': Item.objects.all()
    }
    return render(request, 'items/index.html', context)


def item(request, id):
    return render(request, 'item/index.html')

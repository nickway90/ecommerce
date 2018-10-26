from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import loader
from django.shortcuts import render, get_object_or_404
from .models import Item


def index(request):
    return render(request, 'shopping/index.html')


def cart(request):
    return render(request, 'cart/index.html')


def items(request):
    items = Item.objects.all()
    return render(request, 'items/index.html', {'items': items})


def item(request, id):
    item = get_object_or_404(Item, pk=id)
    return render(request, 'item/index.html', {'item': item})

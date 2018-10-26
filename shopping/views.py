from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def index(request):
    template = loader.get_template('shopping/index.html')
    return HttpResponse(template.render())


def cart(request):
    template = loader.get_template('cart/index.html')
    return HttpResponse(template.render())


def items(request):
    template = loader.get_template('items/index.html')
    return HttpResponse(template.render())


def item(request, id):
    template = loader.get_template('item/index.html')
    return HttpResponse(template.render())

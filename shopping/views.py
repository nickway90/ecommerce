from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import loader
from django.shortcuts import render, redirect, get_object_or_404
from .models import Item, Cart, CartItem


def index(request):
    return render(request, 'shopping/index.html')


def cart(request):
    cart = Cart.objects.get(session_id=request.session.session_key)
    if not cart:
        cart = Cart.objects.create(session_id=request.session.session_key)
    return render(request, 'cart/index.html', {'cart': cart})


def items(request):
    items = Item.objects.all()
    return render(request, 'items/index.html', {'items': items})


def item(request, id):
    item = get_object_or_404(Item, pk=id)
    return render(request, 'item/index.html', {'item': item})


def add_item(request, id):
    item = get_object_or_404(Item, pk=id)
    if not request.session.session_key:
        request.session.create()
    try:
        cart = Cart.objects.get(session_id=request.session.session_key)
    except Cart.DoesNotExist:
        cart = Cart.objects.create(session_id=request.session.session_key)
    cart_item = CartItem.objects.create(cart=cart, item=item)
    return redirect('cart')

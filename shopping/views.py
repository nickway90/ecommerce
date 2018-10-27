from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import loader
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import F
from .models import Item, Cart, CartItem
from . import stripe


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
    CartItem.objects.get_or_create(cart=cart, item=item)
    CartItem.objects.filter(cart=cart, item=item).update(qty=F('qty')+1)
    return redirect('cart')


def remove_item(request, id):
    cart_item = get_object_or_404(CartItem, pk=id)
    if cart_item.qty <= 1:
        cart_item.delete()
    else:
        cart_item.qty = cart_item.qty - 1
        cart_item.save()
    return redirect('cart')


def remove_all(request, id):
    cart_item = get_object_or_404(CartItem, pk=id)
    cart_item.delete()
    return redirect('cart')


def process(request):
    if request.method == 'POST':
        try:
            cart = get_object_or_404(
                Cart, session_id=request.session.session_key)
            charge = stripe.Charge.create(
                amount=cart.stripe_total(),
                currency='usd',
                source=request.POST['stripeToken']
            )
            return render(request, 'cart/process.html', {'charge': charge, 'cart': cart})
        except:
            pass
    return redirect('cart')

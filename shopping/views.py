from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import loader
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import F
from .models import Item, Cart, CartItem, Order
from . import stripe


def index(request):
    return render(request, 'shopping/index.html')


def cart(request):
    try:
        cart = Cart.objects.get(session_id=request.session.session_key)
    except Cart.DoesNotExist:
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


def checkout(request):
    cart = get_object_or_404(
        Cart, session_id=request.session.session_key)
    print(request.user.id)
    if not request.user.is_authenticated:
        return redirect('../../customers/login')
    cart.customer = request.user
    cart.save()
    return render(request, 'cart/checkout.html', {'cart': cart})


def confirmation(request):
    if request.method == 'POST':
        cart = get_object_or_404(
            Cart, session_id=request.session.session_key)
        charge = stripe.Charge.create(
            amount=cart.stripe_total(),
            currency='usd',
            source=request.POST['stripeToken']
        )
        order = Order()
        order.from_cart(cart)
        order.save()
        cart.delete()
        return render(request, 'cart/confirmation.html', {'charge': charge, 'order': order})
    return redirect('cart')


def order_list(request):
    orders = Order.objects.filter(customer=request.user)
    return render(request, 'orders/index.html', {'orders': orders})


def view_order(request, id):
    order = get_object_or_404(Order, pk=id)
    return render(request, 'orders/view.html', {'order': order})

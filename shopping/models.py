from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


class Item(models.Model):
    sku = models.CharField(max_length=100)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    price = models.FloatField()
    created_at = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name


class Cart(models.Model):
    session_id = models.CharField(max_length=200)
    customer = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="cart", null=True)
    created_at = models.DateTimeField(default=datetime.now, blank=True)

    def item_count(self):
        ct = 0
        for cart_item in self.cart_items.all():
            ct = ct + cart_item.qty
        return ct

    def total(self):
        t = 0
        for cart_item in self.cart_items.all():
            t = t + (cart_item.qty * cart_item.item.price)
        return t

    def stripe_total(self):
        return int(self.total() * 100)

    def __str__(self):
        return 'Cart'


class CartItem(models.Model):
    cart = models.ForeignKey(
        Cart, on_delete=models.CASCADE, related_name="cart_items")
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    qty = models.IntegerField(default=0)
    created_at = models.DateTimeField(default=datetime.now, blank=True)

    def total(self):
        return self.qty * self.item.price

    def __str__(self):
        return '{} ({})'.format(self.item.name, self.qty)


class Order(models.Model):
    customer = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="order", null=True)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    total = models.FloatField()

    def from_cart(self, cart):
        self.customer = cart.customer
        self.total = cart.total
        for cart_item in cart.cart_items:
            order_item = OrderItem()
            order_item.from_cart_item(cart_item)
            self.order_items_set.add(order_item)


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name="order_items")
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    sku = models.CharField(max_length=100)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    price = models.FloatField()
    qty = models.IntegerField(default=0)
    total = models.FloatField()

    def from_cart_item(self, cart_item):
        self.item = cart_item.item
        self.sku = cart_item.item.sku
        self.name = cart_item.item.name
        self.description = cart_item.item.description
        self.price = cart_item.item.price
        self.qty = cart_item.qty
        self.total = cart_item.total


class OrderTransaction(models.Model):
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name="order_transactions")
    transaction_id = models.CharField(max_length=150)

from django.db import models
from datetime import datetime


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

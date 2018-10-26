from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cart', views.cart, name='cart'),
    path('items', views.items, name='items'),
    path('item/<int:id>', views.item, name='item'),
    path('item/<int:id>/add', views.add_item, name='add_item')
]

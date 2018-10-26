from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('shopping index')


def cart(request):
    return HttpResponse('shopping cart')


def items(request):
    return HttpResponse('shopping items')

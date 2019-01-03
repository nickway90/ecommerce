from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

# Create your views here.

def login(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST['email'], password=request.POST['password'])
        if user is None:
            return render(request, 'login/index.html')
    return redirect('../shopping')


def register(request):
    if request.method == 'POST':
        user = User.objects.create_user(
            request.POST['email'],
            request.POST['email'],
            request.POST['password'])
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.save()
    return render(request, 'register/index.html')
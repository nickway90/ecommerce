from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from .forms import UserForm


def login(request):
    if request.method == 'POST':
        user = authenticate(
            username=request.POST['email'], password=request.POST['password'])
        if user is not None:
            auth_login(request, user)
            return redirect('../shopping')
    return render(request, 'login/index.html')


def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            # form.save()
            user = User.objects.create_user(
                request.POST['email'],
                request.POST['email'],
                request.POST['password'])
            user.first_name = request.POST['first_name']
            user.last_name = request.POST['last_name']
            user.save()
    else:
        form = UserForm()
    return render(request, 'user/create.html', {'form': form})

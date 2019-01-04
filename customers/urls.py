from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('profile/view', views.view_profile, name='view_profile'),
    path('profile/edit', views.edit_profile, name='edit_profile')
]
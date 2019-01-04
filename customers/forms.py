from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import AddressType, UserAddress


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password']


class EditUserForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


class UserAddressForm(ModelForm):
    class Meta:
        model = UserAddress
        fields = ['type', 'primary', 'street_1', 'street_2',
                  'city', 'state', 'postal_code', 'telephone']

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group
from django import forms
from django.forms import ModelForm

from .models import Toilet, Provider



class ToiletForm(ModelForm):
    class Meta():
        model = Toilet
        fields = ['provider_id', 'ubication', 'description', 'accesibility', 'image_1']

class ProviderForm(ModelForm):
    class Meta():
        model = Provider
        fields = '__all__'

class CreateProviderForm(UserCreationForm):
    class Meta():
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
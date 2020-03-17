from django.forms import ModelForm
from django import  forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group
from leaflet.forms.widgets import LeafletWidget
from leaflet.forms.fields import PointField

from .models import Toilet
# , Provider

class ToiletForm(ModelForm):
    class Meta():
        model = Toilet
        fields = ['address', 'latitude', 'longitude', 'image_1', 'image_2', 'image_3', 'description', 'accesibility']

class ProviderForm(ModelForm):
    class Meta():
        model = User
        fields = '__all__'

class CreateProviderForm(UserCreationForm):
    class Meta():
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

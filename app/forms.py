from django.forms import ModelForm
from django import  forms
from leaflet.forms.widgets import LeafletWidget
from leaflet.forms.fields import PointField

from .models import Toilet

class ToiletForm(ModelForm):
    class Meta():
        model = Toilet

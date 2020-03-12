from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin

from .models import Toilet, Costumer, Provider
# Register your models here.
class ToiletAdmin(LeafletGeoAdmin):
    pass

admin.site.register(Toilet, ToiletAdmin)
admin.site.register(Costumer)
admin.site.register(Provider)

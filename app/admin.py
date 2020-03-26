from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin

from .models import Toilet
class ToiletAdmin(LeafletGeoAdmin):
    # load the map for admin site
    pass

admin.site.register(Toilet, ToiletAdmin)

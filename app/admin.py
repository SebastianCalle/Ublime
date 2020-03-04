from django.contrib import admin

from .models import Toilet, Costumer, Provider
# Register your models here.

admin.site.register(Toilet)
admin.site.register(Costumer)
admin.site.register(Provider)

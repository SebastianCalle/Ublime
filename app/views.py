from django.shortcuts import render
from django.contrib.gis.geos import GEOSGeometry
from .models import  Toilet
from .forms import ToiletForm

# Create your views here.

def home(request):
    # Home view
    context = {}
    return render(request, "home.html", context)

def singup_user_view(request):
    # Home view
    context = {}
    return render(request, "app/singup_user.html", context)

def singup_provider_view(request):
    # Home view
    context = {}
    return render(request, "app/singup_provider.html", context)

def user_interface(request):
    # Home view
    context = {}
    return render(request, "app/user_interface.html", context)

def test(request):
    # Home view
    context = {}
    return render(request, "app/test.html", context)

def ProviderView(request):
    # View for Provider
    form = ToiletForm()
    if (request.method == "POST"):
        print(request.POST)
        data = request.POST
        address = data['address']
        accesible = False
        longitude = data['longitude']
        latitude = data['latitude']
        point = "POINT({} {})".format(longitude, latitude)
        location = GEOSGeometry(point, srid=4326)
        image = data['image']
        #new_toilet = Toilet(address=address,
                            # accesible=accesible,
                            # latitude=latitude,
                            # longitude=longitude,
                            # location=location,
                            # image=image)
    # new_toilet.save()
    context = {'form': form}
    return render(request, "app/provider-interface.html", context)

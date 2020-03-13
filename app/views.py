from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, User
from django.contrib.auth.models import Group
from django.contrib.gis.geos import GEOSGeometry
from .models import Provider, Toilet
from .forms import ToiletForm



from .forms import ToiletForm, ProviderForm, CreateProviderForm
from .models import Toilet
# Create your views here.

def home(request):
    # Home view
    context = {}
    return render(request, "home.html", context)

def singupUser(request):
    # Home view
    context = {}
    return render(request, "app/singup-user.html", context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            UserName = request.POST.get('username')
            Password = request.POST.get('password')
            User = authenticate(username=UserName, password=Password)
            if User is not None:
                login(request, User)
                return redirect('home')
            else:
                messages.info(request, 'Username or Password is incorrect')
        context = {}
        return render(request, "app/login.html", context)

def logoutPage(request):
    logout(request)
    return redirect('loginPage')

def singupProvider(request):
    if request.user.is_authenticated:
        return  redirect('home')

    else:
        form = CreateProviderForm()
        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                user = form.save()
                UserName = form.cleaned_data.get('username')
                group = Group.objects.get(name='Provider')
                user.groups.add(group)
                Provider.objects.create(user=user,)
                messages.success(request, 'Account was created for  ' + UserName)

                return redirect('loginPage')

        context = {'form': form}
        return render(request, "app/singup-provider.html", context)

def userInterface(request):
    # View for user
    objects = Toilet.objects.all()
    context = {
        'objects': objects
    }
    return render(request, "user-interface.html", context)

def providerInterface(request):
    # View for Provider
    form = ToiletForm()
    if (request.method == "POST"):
        print("esto es form", form)
        data = request.POST
        print("esto es data ",data)
        address = data['address']
        accesible = False
        longitude = data['longitude']
        latitude = data['latitude']
        point = "POINT({} {})".format(longitude, latitude)
        location = GEOSGeometry(point, srid=4326)
        image = data['image']
        # new_toilet = Toilet(address=address,
                            # accesible=accesible,
                            # latitude=latitude,
                            # longitude=longitude,
                            # location=location,
                            # image=image)
    # new_toilet.save()
    context = {'form': form}
    return render(request, "app/provider-interface.html", context)

def createToilet(request):
    '''Creating view for CRUD: this es for Create'''

    form = ToiletForm()
    if request.method == 'POST':
        form = ToiletForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(request, "app/toilet-form.html", context)

def createProvider(request):
    Pform = ProviderForm()
    if request.method == 'POST':
        Pform = ProviderForm(request.POST)
        if Pform.is_valid():
             Pform.save()
    context = {'form': Pform}
    return render(request, 'app/provider-form.html', context)

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, User
from django.contrib.auth.models import Group
from .models import Provider



from .forms import ToiletForm, ProviderForm, CreateProviderForm
from .models import Toilet
# Create your views here.

def home(request):
    # Home view
    context = {}
    return render(request, "home.html", context)

def singup_user_view(request):
    # Home view
    context = {}
    return render(request, "app/singup_user.html", context)

def LoginPage(request):
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

def LogoutPage(request):
    logout(request)
    return redirect('LoginPage')

def singup_provider_view(request):
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
                Provider.objects.create(
                    user=user,
                )
                messages.success(request, 'Account was created for  ' + UserName)
                return redirect('LoginPage')

        context = {'form': form}
        return render(request, "app/singup_provider.html", context)

#@login_required(login_url='login')
def CreateToilet(request):
    '''Creating view for CRUD: this es for Create'''

    form = ToiletForm()
    if request.method == 'POST':
        form = ToiletForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(request, "app/Toilet_form.html", context)

def CreateProvider(request):
    Pform = ProviderForm()
    if request.method == 'POST':
        Pform = ProviderForm(request.POST)
        if Pform.is_valid():
             Pform.save()
    context = {'form': Pform}
    return render(request, 'app/Provider_form.html', context)

def toilets(request):
    objects = Toilet.objects.all()
    extend = {'objs': objects}
    return render(request, 'app/toilets.html', extend)


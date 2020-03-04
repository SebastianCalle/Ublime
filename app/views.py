from django.shortcuts import render

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

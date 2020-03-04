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

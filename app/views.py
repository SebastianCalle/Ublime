from django.shortcuts import render

# Create your views here.

def home(request):
    # Home view
    context = {}
    return render(request, "home.html", context)


def singup_view(request):
    # Home view
    context = {}
    return render(request, "app/singup.html", context)

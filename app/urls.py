from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path("", views.home, name='home'),
    path("user-interface", views.userInterface, name="userInterface"),
    path('provider-interface', views.providerInterface, name="providerInterface"),
    path("singup-provider", views.singupProvider, name="singupProvider"),
    path("create-provider", views.createProvider, name="createProvider"),
    path("login-page", views.loginPage, name="loginPage"),
    path("logout-page", views.logoutPage, name="logoutPage"),
    path("more-info", views.moreInfo, name="moreInfo"),
    path('toilet-requirements', views.toiletRequirements, name="toiletRequirements"),
    path('dashboard', views.dashboard, name='dashboard'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name='home'),
    path("singup_user", views.singup_user_view, name="singup_user"),
    path("user-interface", views.user_interface),
    path('provider-interface', views.ProviderView, name="provider"),
    path("singup_provider", views.singup_provider_view, name="singup_provider"),
    path("CreateToilet", views.CreateToilet, name="CreateToilet"),
    path("CreateProvider", views.CreateProvider, name="CreateProvider"),
    path("LoginPage", views.LoginPage, name="LoginPage"),
    path("LogoutPage", views.LogoutPage, name="LogoutPage"),
    path('toilets', views.toilets, name="toilets")
]

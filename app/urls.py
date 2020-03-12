from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name='home'),
    path("singup-user", views.singupUser, name="singupUser"),
    path("user-interface", views.userInterface, name="userInterface"),
    path('provider-interface', views.providerInterface, name="providerInterface"),
    path("singup-provider", views.singupProvider, name="singupProvider"),
    path("CreateToilet", views.createToilet, name="createToilet"),
    path("CreateProvider", views.createProvider, name="createProvider"),
    path("LoginPage", views.loginPage, name="loginPage"),
    path("LogoutPage", views.logoutPage, name="logoutPage"),
]

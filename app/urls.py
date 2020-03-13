from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name='home'),
    path("singup-user", views.singupUser, name="singupUser"),
    path("user-interface", views.userInterface, name="userInterface"),
    path('provider-interface', views.providerInterface, name="providerInterface"),
    path("singup-provider", views.singupProvider, name="singupProvider"),
    path("create-toilet", views.createToilet, name="createToilet"),
    path("create-provider", views.createProvider, name="createProvider"),
    path("login-page", views.loginPage, name="loginPage"),
    path("logout-page", views.logoutPage, name="logoutPage"),
]

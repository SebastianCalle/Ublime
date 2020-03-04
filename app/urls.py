from django.urls import path

from . import views

urlpatterns = [
    path("", views.home),
    path("singup_user", views.singup_user_view),
    path("singup_provider", views.singup_provider_view),
    path("user_interface", views.user_interface),
    path("test", views.test),
]

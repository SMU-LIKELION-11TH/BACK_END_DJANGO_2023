from django.urls import path
from . import views as views

app_name = "account"

urlpatterns = [
    path("home/", views.homepage),
    path("home/store/", views.store),
    path("login/", views.login),
]

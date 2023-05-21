from django.urls import path
from . import views as views

app_name = "account"

urlpatterns = [
    path("home/", views.homepage),
    path("home/store_1/", views.store_1),
    path("home/store_2/", views.store_2)
]

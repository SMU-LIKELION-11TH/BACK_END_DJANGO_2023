from django.urls import path
from . import views as views

urlpatterns = [
    path('', views.users_view),
]
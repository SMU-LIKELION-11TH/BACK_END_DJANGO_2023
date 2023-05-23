from django.urls import path
from . import views as views

urlpatterns = [
    path('user_login/',views.user_login),
    path('user_main/', views.user_main)

]

from django.urls import path
from . import views as views

urlpatterns = [
    path('info/', views.users_view, name='users_url'),
    path('login/', views.login_view, name='login_url'),
]



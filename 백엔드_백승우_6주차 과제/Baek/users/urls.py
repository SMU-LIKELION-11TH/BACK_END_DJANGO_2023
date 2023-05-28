from django.urls import path
from . import views as views

urlpatterns = [
    path('User/read/user_detail', views.user_detail, name='user_detail'),
    path('login/', views.login_view, name='login_view'),
]



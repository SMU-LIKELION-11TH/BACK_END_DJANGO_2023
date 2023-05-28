from django.urls import path
from . import views as views

urlpatterns = [
    path('user/detail/', views.user_detail, name='user_detail'),
    path('user/login/', views.login_view, name='login_view'),
]



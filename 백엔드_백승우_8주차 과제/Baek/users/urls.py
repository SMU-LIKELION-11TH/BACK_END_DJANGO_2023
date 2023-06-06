from django.urls import path
from . import views

urlpatterns = [
    path('user/detail/', views.UserDetailView.as_view(), name='user_detail'),
    path('user/login/', views.UserLoginView.as_view(), name='login_view'),
]



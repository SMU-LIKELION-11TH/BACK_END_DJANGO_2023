from django.urls import path
from . import views as views

urlpatterns = [
    path("home/", views.homepage),
    path("home/store/<int:id>/", views.store, name='store'),
    path("login/", views.login),
]
#cbv ppt확인
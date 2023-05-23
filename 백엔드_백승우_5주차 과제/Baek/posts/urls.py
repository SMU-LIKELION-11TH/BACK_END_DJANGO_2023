from django.urls import path
from . import views as views

urlpatterns = [
    path('posts/', views.post_view),
]
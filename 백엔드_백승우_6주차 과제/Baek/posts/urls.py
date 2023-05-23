from django.urls import path
from . import views as views

urlpatterns = [
    path('post/', views.post_view),
    path('category/', views.category_view),
]
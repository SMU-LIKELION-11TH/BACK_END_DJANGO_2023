from django.urls import path
from . import views as views

urlpatterns = [
    path('post_title/',views.post_title),
    path('post/<int:id>/', views.post_detail, name='post_detail'),

]

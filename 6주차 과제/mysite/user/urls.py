from django.urls import path
from . import views as views

urlpatterns = [
    path('user_list/',views.user_list),
    path('user_list2/', views.user_list2)

]

from django.urls import path
from . import views as views

app_name = "single_page"
urlpatterns = [
    path('',views.user_main,name ='home')
]
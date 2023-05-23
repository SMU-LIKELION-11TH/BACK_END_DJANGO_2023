from django.urls import path
from . import views as views

app_name ="liongram"

urlpatterns = [
    path("", views.home),
    path("post1/", views.post1),
    path("post2/", views.post2)
]
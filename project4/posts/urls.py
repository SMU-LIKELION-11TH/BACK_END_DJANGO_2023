from django.urls import path
from . import views as views

app_name ="lionlog"

urlpatterns = [
    path("", views.home),
    path("post/<int:id>/", views.post1),
]
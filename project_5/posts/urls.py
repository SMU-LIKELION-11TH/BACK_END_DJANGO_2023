from django.urls import path
from . import views as views

app_name ="lionlog"

urlpatterns = [
    path("", views.home),
    path("post/create/", views.post_create, name='post-create'),
    path("post/<int:id>/", views.post1),
    path("post/<int:id>/edit/", views. post_update),
    path("post/<int:id>/delete/", views. post_delete),
]
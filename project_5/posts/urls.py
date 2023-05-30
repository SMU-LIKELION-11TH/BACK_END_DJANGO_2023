from django.urls import path
from . import views as views

app_name ="post"

urlpatterns = [
    path("", views.home),
    path("create/", views.Post_create.as_view(), name='post-create'),
    path("<int:id>/", views.PostView.as_view()),
    path("<int:id>/edit/", views. Post_update.as_view(), name='post-update'),
    path("<int:id>/delete/", views.Post_delete.as_view(), name='post-delete'),
]

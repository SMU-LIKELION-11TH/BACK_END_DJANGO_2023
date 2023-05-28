from django.urls import path
from . import views as views

app_name ="project"

urlpatterns = [
    path("post_list1/", views.post_list1),
    path("post_list2/", views.post_list2)
]
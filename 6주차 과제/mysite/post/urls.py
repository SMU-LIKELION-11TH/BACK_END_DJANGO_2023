from django.urls import path
from . import views as views


urlpatterns = [
    path('list/',views.post_list,name='post_list'),
    path('<int:id>/', views.post_detail, name='post_detail'),
    path('create/', views.create_post, name='create_post'),
    path('<int:id>/update/',views.update_post,name='update_post'),
    path('<int:id>/delete/',views.delete_post,name='delete_post')


]

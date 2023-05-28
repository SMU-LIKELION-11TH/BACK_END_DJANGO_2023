from django.urls import path
from . import views as views

urlpatterns = [
    path('post/<int:post_id>/', views.post_view, name='post_detail'),
    path('post/list/', views.category_view, name='post_list'),
    path('post/create/', views.post_create, name='post_create'),
    path('post/<int:post_id>/delete/', views.post_delete, name='post_delete'),
    path('post/<int:post_id>/update/', views.post_update, name='post_update'),
    path('post/<int:post_id>/comment/create/', views.comment_create, name='comment_create'),
    path('comment/<int:comment_id>/delete/', views.comment_delete, name='comment_delete'),
    path('comment/<int:comment_id>/update/', views.comment_update, name='comment_update'),
]
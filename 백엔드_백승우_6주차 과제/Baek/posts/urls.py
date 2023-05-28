from django.urls import path
from . import views as views

urlpatterns = [
    path('Post/<int:post_id>/read/post_view/', views.post_view, name='post_detail'),
    path('Post/list/read/category_view/<int:user_id>/', views.category_view, name='post_list'),
    path('Post/<int:user_id>/create/post_create/', views.post_create, name='post_create'),
    path('Post/<int:post_id>/delete/post_delete/', views.post_delete, name='post_delete'),
    path('Post/<int:post_id>/update/post_update/', views.post_update, name='post_update'),
    path('comments/Comment/<int:post_id>/comment_create/', views.comment_create, name='comment_create'),
    path('comments/Comment/<int:comment_id>/comment_delete/', views.comment_delete, name='comment_delete'),
    path('comments/Comment/<int:comment_id>/comment_update/', views.comment_update, name='comment_update'),
]
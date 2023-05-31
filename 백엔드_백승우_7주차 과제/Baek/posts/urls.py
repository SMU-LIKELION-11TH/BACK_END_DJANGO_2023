from django.urls import path
from . import views

urlpatterns = [
    path('post/<int:post_id>/', views.PostDetailView.as_view(), name='post_detail'),
    path('post/list/', views.CategoryView.as_view(), name='post_list'),
    path('post/create/', views.PostCreateView.as_view(), name='post_create'),
    path('post/<int:post_id>/delete/', views.PostDeleteView.as_view(), name='post_delete'),
    path('post/<int:post_id>/update/', views.PostUpdateView.as_view(), name='post_update'),
    path('post/<int:post_id>/comment/create/', views.CommentCreateView.as_view(), name='comment_create'),
    path('comment/<int:comment_id>/delete/', views.CommentDeleteView.as_view(), name='comment_delete'),
    path('comment/<int:comment_id>/update/', views.CommentUpdateView.as_view(), name='comment_update'),
]
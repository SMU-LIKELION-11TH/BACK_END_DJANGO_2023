from django.urls import path
from . import views as views

app_name ="post"

urlpatterns = [
    path("", views.home),
    # path("create/", views.Post_create.as_view(), name='post-create'), //post create는 /home/에서
    path("<int:id>/", views.PostView.as_view(),name='post-list'),
    path("<int:id>/edit/", views.Post_update.as_view(), name='post-update'),

    # path("comment/<int:id>/", views.CommentView.as_view(), name='comment-list'),
    path("<int:id>/comment/create/", views.Comment_create.as_view(), name='comment-create'),
    path("<int:id>/comment/edit/", views.Comment_update.as_view(), name='comment-update'),

    # path("reply/<int:id>/", views.ReplyView.as_view(), name='reply-list'),
    path("<int:id>/reply/create/", views.Reply_create.as_view(), name='reply-create'),
    path("<int:id>/reply/delete/", views.Reply_delete.as_view(), name='reply-delete'),

]

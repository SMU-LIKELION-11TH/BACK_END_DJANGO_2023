from django.urls import path
from . import views as views

urlpatterns = [
    path('post_detail/',views.post_detail),
    path('add_comment/',views.add_comment),
    path('comment_created_at/',views.comment_created_at)


]

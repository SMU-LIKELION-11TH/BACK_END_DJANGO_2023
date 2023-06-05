from django.urls import path
from reply.views import create_reply

urlpatterns = [
    path('post/<int:post_id>/reply/', create_reply, name='create_reply'),
]

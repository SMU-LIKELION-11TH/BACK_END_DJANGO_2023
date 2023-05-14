from django.db import models
from ..post.models import Post
from ..user.models import User

# Create your models here.


class Comment(models.Model):
    post = models.ForeignKey(Post.id, null=False, on_delete=models.CASCADE)
    author = models.ForeignKey(User.id, null=False, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
from django.db import models
from ..comment.models import Comment
from ..user.models import User

# Create your models here.


class Reply(models.Model):
    comment = models.ForeignKey(Comment.id, null=False, on_delete=models.CASCADE)
    author = models.ForeignKey(User.id, null=False, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
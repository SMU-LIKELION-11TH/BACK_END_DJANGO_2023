from django.db import models

# Create your models here.


class Comment(models.Model):
    post = models.ForeignKey("post.Post", null=False, on_delete=models.CASCADE)
    author = models.ForeignKey("user.User", null=False, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
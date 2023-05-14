from django.db import models

# Create your models here.


class Reply(models.Model):
    comment = models.ForeignKey("comment.Comment", null=False, on_delete=models.CASCADE)
    author = models.ForeignKey("user.User", null=False, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
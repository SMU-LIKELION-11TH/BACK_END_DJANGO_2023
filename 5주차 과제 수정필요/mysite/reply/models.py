from django.db import models

# Create your models here.
class Reply(models.Model):
    liked = models.IntegerField()
    detail = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    comment = models.ForeignKey('comment.Comment', on_delete=models.CASCADE)
    user = models.ForeignKey('user.User', on_delete=models.CASCADE)

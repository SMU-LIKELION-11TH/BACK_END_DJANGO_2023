from django.db import models
from ..post.models import Post

# Create your models here.


class Comment(models.Model):
    content = models.CharField(max_length=100)
    # 역참조를 하려면 related_name으로 접근
    post = models.ForeignKey("post.Post", on_delete=models.CASCADE)
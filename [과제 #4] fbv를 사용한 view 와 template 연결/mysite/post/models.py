from django.db import models

# Create your models here.


class Post(models.Model):
    author = models.ForeignKey("user.User", null=False, on_delete=models.CASCADE)
    content = models.CharField(max_length=1000)

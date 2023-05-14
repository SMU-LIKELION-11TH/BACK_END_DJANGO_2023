from django.db import models
from ..user.models import User

# Create your models here.


class Post(models.Model):
    author = models.ForeignKey(User.id, null=False, on_delete=models.CASCADE)
    content = models.CharField(max_length=1000)

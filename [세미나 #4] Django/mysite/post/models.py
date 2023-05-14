from django.db import models

# Create your models here.


class Post(models.Model):
    # id는 자동으로 생성
    views = models.IntegerField()
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now=True)
    attatchment = models.FileField(upload_to='uploads/')
    image_attatchment = models.ImageField(upload_to='uploads/')
from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

User = get_user_model()

# Create your models here.


class Post(models.Model):

    title = models.CharField(verbose_name='제목', max_length=100)
    writer = models.ForeignKey(verbose_name='작성자', to=User, on_delete= models.CASCADE, null=True, blank=True)
    image = models.ImageField(verbose_name='사진', upload_to = 'images/', default='default.jpg')

    text = models.TextField(verbose_name='내용')
    created_at = models.DateTimeField(verbose_name='작성일', default=timezone.now)

    views = models.IntegerField(verbose_name='조회수', default=0)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    writer = models.ForeignKey(User, on_delete=models.CASCADE)

    text = models.TextField(verbose_name='내용')
    created_at = models.DateTimeField(verbose_name='작성일', default=timezone.now)

class Reply(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    writer = models.ForeignKey(User, on_delete=models.CASCADE)

    text = models.TextField(verbose_name='내용')
    created_at = models.DateTimeField(verbose_name='작성일', default=timezone.now)

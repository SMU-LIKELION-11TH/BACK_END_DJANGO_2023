from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    detail = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updates_at = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=50)
    image = models.ImageField(upload_to='uploads/')
    user = models.ForeignKey('user.User', on_delete = models.CASCADE)





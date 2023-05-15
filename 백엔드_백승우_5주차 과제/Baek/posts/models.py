from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField(null=True)
    category = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    see = models.IntegerField(null=False, default='0')
    file = models.FileField(upload_to='uploads/', null=True)
    image = models.ImageField(upload_to='uploads/', null=True)
    user = models.ForeignKey("users.User", on_delete=models.CASCADE, null=True)
from django.db import models

class User(models.Model):
    nickname = models.CharField(max_length=10, null=True)
    password = models.CharField(max_length=12, null=True)
    level = models.IntegerField(null=True)
    log_in_at = models.DateTimeField(auto_now_add=True)
    pw_change_at = models.DateTimeField(auto_now_add=True)
    email = models.CharField(max_length=30, null=True)
    sign_up_at = models.DateTimeField(auto_now=True)
    profile_image = models.ImageField(upload_to='uploads/', null=True)

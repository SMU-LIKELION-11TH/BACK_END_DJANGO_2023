from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pw_change_at = models.DateTimeField(auto_now=True)
    profile_image = models.ImageField(upload_to='uploads/', null=True)
    first_name = None
    last_name = None
    username = models.CharField(max_length=16, unique=True, null=False, default='')


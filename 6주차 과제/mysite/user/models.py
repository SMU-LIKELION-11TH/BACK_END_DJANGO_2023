from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    name = models.CharField(max_length=10)
    nickname = models.CharField(max_length=20)
    email =  models.CharField(max_length=50)
    # password = models.CharField(max_length=50)
    profile_image = models.ImageField(upload_to='uploads/')

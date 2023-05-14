from django.db import models

# Create your models here.


class User(models.Model):
    username = models.CharField(null=False, max_length=16)
    password = models.CharField(null=False, max_length=16)

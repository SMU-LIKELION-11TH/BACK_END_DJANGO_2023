# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.


class User(AbstractUser):
    email = models.EmailField(verbose_name='이메일', null=True)
    birth_date = models.DateField(verbose_name='생년월일', null=True)
    pic = models.ImageField(verbose_name='증명사진', upload_to = 'pic/', default='default.jpg')


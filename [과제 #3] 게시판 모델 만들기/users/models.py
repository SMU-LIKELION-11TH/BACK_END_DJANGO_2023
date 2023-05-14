# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractBaseUser


# Create your models here.


class User(AbstractBaseUser):
    username = models.CharField(verbose_name='아이디', max_length=10, unique=True, default="")
    email = models.EmailField(verbose_name='이메일', null=True)
    birth_date = models.DateField(verbose_name='생년월일', null=True)
    password = models.BooleanField(verbose_name='비밀번호')
    pic = models.ImageField(verbose_name='증명사진', upload_to = 'pic/', default='default.jpg')


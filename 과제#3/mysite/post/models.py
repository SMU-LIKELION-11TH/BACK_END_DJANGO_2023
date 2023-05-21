import datetime
from django.db import models

class User(models.Model):
    user = models.CharField(max_length=20)
    password = models.CharField(max_length=50)
    address = models.CharField(max_length=256)

class Orders(models.Model):
    orderer = models.CharField(max_length=20)
    ordered_food = models.CharField(max_length=100)
    number_of_food_ordered = models.IntegerField()
    ordered_from = models.CharField(max_length=256)
    additional_request = models.CharField(max_length=256)
    updated_at = models.DateTimeField(auto_now=True)

class store(models.Model):
    store_name = models.CharField(max_length=20)
    address = models.CharField(max_length=256)

class menu(models.Model):
    menu_name = models.CharField(max_length=20)
    price = models.CharField(max_length=256)

class rating(models.Model):
    store_name = models.CharField(max_length=20)
    username = models.CharField(max_length=20)
    star_rating = models.IntegerField()
    comment = models.CharField(max_length=256)


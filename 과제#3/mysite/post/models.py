from django.db import models
from django.contrib.auth.models import AbstractUser


class Users(AbstractUser):
    address = models.CharField(max_length=256)


class Orders(models.Model):
    orderer_id = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='orderer_orders')
    shipping_address = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='shipping_address_orders')
    additional_request = models.CharField(max_length=256)
    updated_at = models.DateTimeField(auto_now=True)


class Manager(models.Manager):
    pass


class Stores(models.Model):
    store_name = models.CharField(max_length=20)
    store_address = models.CharField(max_length=256)
    store_link = models.CharField(max_length=1000)
    objects = Manager()


class Menus(models.Model):
    store_name = models.ForeignKey(Stores, on_delete=models.CASCADE)
    menu_name = models.CharField(max_length=20)
    menu_price = models.CharField(max_length=256)
    objects = Manager()


class Ratings(models.Model):
    store_name = models.ForeignKey(Stores, on_delete=models.CASCADE)
    username = models.ForeignKey(Users, on_delete=models.CASCADE)
    star_rating = models.IntegerField()
    comment = models.CharField(max_length=256)


class Orders_Menus(models.Model):
    orderer = models.ForeignKey(Users, on_delete=models.CASCADE)
    ordered_menu = models.ForeignKey(Menus, on_delete=models.CASCADE)
    number_of_orders = models.IntegerField()

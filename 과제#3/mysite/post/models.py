from django.db import models

class Users(AbstractUser):
    address = models.CharField(max_length=256)

class Orders(models.Model):
    orderer_id = models.ForeignKey(Users.username, on_delete=models.CASCADE)
    shipping_address = models.ForeignKey(Users.address, on_delete=models.CASCADE)
    additional_request = models.CharField(max_length=256)
    updated_at = models.DateTimeField(auto_now=True)

#models.ManyToManyField(Store, through='Order_Store', through_fields=('ordered_menu',))
class Stores(models.Model):
    store_name = models.CharField(max_length=20)
    store_address = models.CharField(max_length=256)
    def __str__(self):
        return self.store_name

class Menus(models.Model):
    store_name = models.ForeignKey(Stores.store_name, on_delete=models.CASCADE)
    menu_name = models.CharField(max_length=20)
    menu_price = models.CharField(max_length=256)

class Ratings(models.Model):
    store_name = models.ForeignKey(Stores.store_name, on_delete=models.CASCADE)
    username = models.ForeignKey(Users.username, on_delete=models.CASCADE)
    star_rating = models.IntegerField()
    comment = models.CharField(max_length=256)

class Orders_Menus(models.Model):
    orderer = models.ForeignKey(Users.username, on_delete=models.CASCADE)
    ordered_menu = models.ForeignKey(Menus.menu_name, on_delete=models.CASCADE)
    number_of_orders = models.IntegerField()

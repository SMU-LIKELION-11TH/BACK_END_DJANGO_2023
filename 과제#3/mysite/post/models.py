import datetime
from django.db import models

class Orders(models.Model):
    orderer = models.CharField(max_length=20)
    ordered_food = models.CharField(max_length=100)
    number_of_food_ordered = models.IntegerField()
    ordered_from = models.CharField(max_length=256)
    additional_request = models.CharField(max_length=256)
    updated_at = models.DateTimeField(auto_now=True)
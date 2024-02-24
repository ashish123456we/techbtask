from django.db import models


class Laptop (models.Model):
    laptop_id = models.IntegerField(unique=True)
    model_name = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)
    ram = models.CharField(max_length=50)
    processor = models.CharField(max_length=50)
    price = models.FloatField()





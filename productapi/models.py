from django.db import models

class Brand(models.Model):
    name = models.CharField(max_length=120)
    desc = models.CharField(max_length=2400)

    class Meta:
        db_table = 'brand'

class Product(models.Model):
    title = models.CharField(max_length=120)
    imageSrc = models.CharField(max_length=400)
    price = models.FloatField()

    class Meta:
        db_table = 'product'
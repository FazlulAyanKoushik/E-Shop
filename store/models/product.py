from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    slug = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    description = models.TextField(default='')
    image = models.ImageField(upload_to='uploads/products/')

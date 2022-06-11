from django.db import models
from .category import Category


class Product(models.Model):
    name = models.CharField(max_length=100)
    slug = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    description = models.TextField(default='')
    image = models.ImageField(upload_to='uploads/products/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)

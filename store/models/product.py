from django.db import models
from .category import Category
from django.utils.text import slugify



class Product(models.Model):
    name = models.CharField(max_length=100)
    slug = models.CharField(max_length=100,unique=True, null=True, blank=True)
    price = models.IntegerField(default=0)
    description = models.TextField(default='', null=True, blank=True)
    image = models.ImageField(upload_to='uploads/products/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)
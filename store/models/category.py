from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.CharField(max_length=100)
    image = models.ImageField(upload_to='uploads/products/')

    def __str__(self):
        return self.name

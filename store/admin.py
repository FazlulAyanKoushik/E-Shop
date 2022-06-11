from django.contrib import admin
from .models.product import Product
from .models.category import Category


class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'category']


class AdminCategory(admin.ModelAdmin):
    list_display = ['name', 'slug']


# Register your models here.
admin.site.register(Product, AdminProduct)
admin.site.register(Category, AdminCategory)

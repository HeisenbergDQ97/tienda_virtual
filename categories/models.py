from django.db import models
from products.models import Product


class Category(models.Model):
    title = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    products = models.ManyToManyField(Product, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
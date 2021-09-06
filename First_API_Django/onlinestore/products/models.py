from django.db import models

# Create your models here.


class Manufacturer(models.Model):
    name = models.CharField(max_length=120)
    location = models.CharField(max_length=120)
    active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.name

# Product class


class Product(models.Model):
    manufacturer = models.ForeignKey(
        Manufacturer, on_delete=models.CASCADE, related_name="products")

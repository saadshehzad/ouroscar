from django.db import models


# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=40)
    cost = models.CharField(max_length=70)
    weight = models.CharField(max_length=60)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=30)
    image = models.ImageField(null = True)


    def __str__(self):
        return self.name
        

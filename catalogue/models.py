from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=40)
    cost = models.CharField(max_length=70)
    weight = models.CharField(max_length=60)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=30)
    image = models.ImageField(null=True)

    def __str__(self):
        return self.name


class ProductOptions(models.Model):
    name = models.CharField(max_length=30)
    size = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class ProductClass(models.Model):
    name = models.ForeignKey(max_length=30)
    weight = models.CharField(max_length=50)

    def __str__(self):
        return self.name



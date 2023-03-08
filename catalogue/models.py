from django.db import models
from partner.models import Partners

class TimeStampMixin(models.Model):
    created_at = models.DateTimeField(auto_now=True, null=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        abstract = True


class ProductClass(TimeStampMixin):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Category(TimeStampMixin):
    product_class = models.ManyToManyField(ProductClass)
    name = models.CharField(max_length=30)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


class Product(TimeStampMixin):
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="products"
    )
    partner = models.ForeignKey(Partners, on_delete=models.CASCADE, default=None, related_name="partner_products")

    name = models.CharField(max_length=40)
    cost = models.CharField(max_length=70)

    def __str__(self):
        return self.name
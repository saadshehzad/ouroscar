# Generated by Django 4.1.3 on 2023-01-28 19:20

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("catalogue", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="category",
            name="product_class",
            field=models.ManyToManyField(to="catalogue.productclass"),
        ),
    ]

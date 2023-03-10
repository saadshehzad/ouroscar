# Generated by Django 4.1.3 on 2023-01-28 19:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now=True, null=True)),
                ("updated_at", models.DateTimeField(auto_now_add=True, null=True)),
                ("name", models.CharField(max_length=30)),
                ("image", models.ImageField(null=True, upload_to="")),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="ProductClass",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now=True, null=True)),
                ("updated_at", models.DateTimeField(auto_now_add=True, null=True)),
                ("name", models.CharField(max_length=50)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now=True, null=True)),
                ("updated_at", models.DateTimeField(auto_now_add=True, null=True)),
                ("name", models.CharField(max_length=40)),
                ("cost", models.CharField(max_length=70)),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="products",
                        to="catalogue.category",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]

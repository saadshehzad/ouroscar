# Generated by Django 4.1.3 on 2023-01-28 18:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('image', models.ImageField(null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('cost', models.CharField(max_length=70)),
                ('weight', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='ProductClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.CharField(max_length=50)),
                ('name', models.ForeignKey(max_length=30, on_delete=django.db.models.deletion.CASCADE, to='catalogue.productoptions')),
            ],
        ),
    ]

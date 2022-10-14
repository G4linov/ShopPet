# Generated by Django 3.2.16 on 2022-10-14 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ProductCategory",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=64, unique=True, verbose_name="имя")),
                ("description", models.TextField(blank=True, verbose_name="описание")),
            ],
        ),
    ]

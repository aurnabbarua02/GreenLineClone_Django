# Generated by Django 5.1.6 on 2025-02-25 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0012_delete_headoffice"),
    ]

    operations = [
        migrations.CreateModel(
            name="HeadOfficeInfo",
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
                ("address", models.CharField(max_length=200)),
                ("area", models.CharField(max_length=100)),
                ("tel", models.CharField(max_length=15)),
                ("fax", models.CharField(max_length=15)),
                ("email", models.EmailField(max_length=254)),
            ],
        ),
    ]

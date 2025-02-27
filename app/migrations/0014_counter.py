# Generated by Django 5.1.6 on 2025-02-25 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0013_headofficeinfo"),
    ]

    operations = [
        migrations.CreateModel(
            name="counter",
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
                ("district", models.CharField(max_length=20)),
                ("area", models.CharField(max_length=20)),
                ("address", models.CharField(max_length=100)),
                ("detail_area", models.CharField(max_length=100)),
                ("phone1", models.CharField(max_length=15)),
                ("phone2", models.CharField(blank=True, max_length=15, null=True)),
                ("phone3", models.CharField(blank=True, max_length=15, null=True)),
            ],
        ),
    ]

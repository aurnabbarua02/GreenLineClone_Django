# Generated by Django 5.1.6 on 2025-02-25 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0003_rename__from_service_destination_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="About",
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
                ("profile", models.TextField()),
                ("mission", models.TextField()),
                ("vision", models.TextField()),
                ("founder", models.TextField()),
            ],
        ),
    ]

# Generated by Django 5.1.6 on 2025-02-25 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0010_section2"),
    ]

    operations = [
        migrations.CreateModel(
            name="GreenLine",
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
                ("description", models.TextField()),
            ],
        ),
    ]

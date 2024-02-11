# Generated by Django 5.0.1 on 2024-02-08 18:42

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Post",
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
                ("posted_date", models.DateTimeField(auto_now_add=True)),
                ("title", models.CharField(max_length=200)),
                ("tags", models.CharField(max_length=2000)),
                (
                    "rating",
                    models.CharField(
                        choices=[
                            ("S", "Safe"),
                            ("Q", "Questionable"),
                            ("E", "Explicit"),
                        ],
                        default="S",
                        max_length=1,
                    ),
                ),
                ("score", models.IntegerField(default=0, editable=False)),
                ("source", models.CharField(blank=True, default="", max_length=255)),
                ("file", models.FileField(upload_to="files/")),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]

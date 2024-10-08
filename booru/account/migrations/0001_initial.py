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
            name="UserOptions",
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
                (
                    "blacklisted_tags",
                    models.TextField(
                        blank=True,
                        help_text="Comma-separated list of blacklisted tags",
                        null=True,
                    ),
                ),
                (
                    "blacklisted_rating",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("safe", "Safe"),
                            ("questionable", "Questionable"),
                            ("explicit", "Explicit"),
                            ("s", "Safe"),
                            ("q", "Questionable"),
                            ("e", "Explicit"),
                        ],
                        max_length=12,
                        null=True,
                    ),
                ),
                (
                    "comment_threshold",
                    models.IntegerField(
                        default=0,
                        help_text="Ignore comments with a score below this threshold",
                    ),
                ),
                (
                    "post_threshold",
                    models.IntegerField(
                        default=0,
                        help_text="Ignore posts with a score below this threshold",
                    ),
                ),
                (
                    "show_nsfw_images",
                    models.BooleanField(
                        default=True, help_text="Show or hide NSFW images"
                    ),
                ),
                (
                    "theme",
                    models.CharField(
                        default="light",
                        help_text="User's preferred theme",
                        max_length=20,
                    ),
                ),
                (
                    "blacklisted_users",
                    models.ManyToManyField(
                        blank=True,
                        related_name="blacklisted_users",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]

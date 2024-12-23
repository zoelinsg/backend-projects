# Generated by Django 5.1.1 on 2024-11-16 15:53

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
            name="Book",
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
                ("title", models.CharField(max_length=255)),
                (
                    "cover",
                    models.ImageField(
                        blank=True,
                        default="covers/default_cover.jpg",
                        null=True,
                        upload_to="covers/",
                    ),
                ),
                ("author", models.CharField(max_length=255)),
                (
                    "category",
                    models.CharField(
                        choices=[
                            ("fiction", "小說"),
                            ("non-fiction", "非小說"),
                            ("biography", "傳記"),
                            ("reference", "參考書"),
                            ("other", "其他"),
                        ],
                        max_length=20,
                    ),
                ),
                ("description", models.TextField()),
                ("publication_date", models.DateField()),
                ("isbn", models.CharField(max_length=13)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("available", "Available"),
                            ("borrowed", "Borrowed"),
                            ("reserved", "Reserved"),
                        ],
                        default="available",
                        max_length=20,
                    ),
                ),
                ("borrowed_date", models.DateField(blank=True, null=True)),
                ("due_date", models.DateField(blank=True, null=True)),
                (
                    "borrowed_by",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]

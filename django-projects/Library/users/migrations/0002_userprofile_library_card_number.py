# Generated by Django 5.1.1 on 2024-11-16 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="userprofile",
            name="library_card_number",
            field=models.CharField(
                blank=True, editable=False, max_length=10, unique=True
            ),
        ),
    ]

# Generated by Django 4.2.15 on 2024-11-15 07:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='session_id',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='table',
        ),
        migrations.AddField(
            model_name='cart',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用戶'),
        ),
    ]

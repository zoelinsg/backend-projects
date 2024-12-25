# Generated by Django 4.2.15 on 2024-12-25 05:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('start_date', models.DateField()),
                ('start_time', models.TimeField()),
                ('end_date', models.DateField()),
                ('end_time', models.TimeField()),
                ('description', models.TextField()),
                ('location', models.CharField(choices=[('3F多媒體室', '3F多媒體室'), ('4F多功能室', '4F多功能室'), ('5樓大演講廳', '5樓大演講廳')], max_length=20)),
                ('speaker', models.CharField(blank=True, max_length=255, null=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_activities', to=settings.AUTH_USER_MODEL)),
                ('participants', models.ManyToManyField(related_name='participated_activities', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

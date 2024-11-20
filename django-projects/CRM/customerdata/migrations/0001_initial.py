# Generated by Django 4.2.15 on 2024-11-11 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30, verbose_name='名字')),
                ('last_name', models.CharField(max_length=30, verbose_name='姓氏')),
                ('email', models.EmailField(max_length=100, verbose_name='電子郵件')),
                ('phone', models.CharField(max_length=15, verbose_name='電話號碼')),
                ('address', models.CharField(blank=True, max_length=100, null=True, verbose_name='地址')),
                ('city', models.CharField(blank=True, max_length=50, null=True, verbose_name='城市')),
                ('company', models.CharField(blank=True, max_length=50, null=True, verbose_name='公司')),
                ('position', models.CharField(blank=True, max_length=50, null=True, verbose_name='職位')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='創建時間')),
                ('remark', models.TextField(blank=True, null=True, verbose_name='備註')),
            ],
        ),
    ]

# Generated by Django 4.1.4 on 2022-12-20 20:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_news', '0018_alter_news_cat_alter_news_create_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='create_date',
            field=models.DateField(default=datetime.datetime(2022, 12, 20, 20, 10, 58, 573023), verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='news',
            name='edit_date',
            field=models.DateField(default=datetime.datetime(2022, 12, 20, 20, 10, 58, 573065), verbose_name='Дата редактирования'),
        ),
    ]

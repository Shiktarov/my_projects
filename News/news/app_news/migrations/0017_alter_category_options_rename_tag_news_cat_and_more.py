# Generated by Django 4.1.4 on 2022-12-20 16:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_news', '0016_category_alter_comments_comment_alter_comments_user_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['id'], 'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
        migrations.RenameField(
            model_name='news',
            old_name='tag',
            new_name='cat',
        ),
        migrations.AlterField(
            model_name='news',
            name='create_date',
            field=models.DateField(default=datetime.datetime(2022, 12, 20, 16, 45, 21, 924738), verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='news',
            name='edit_date',
            field=models.DateField(default=datetime.datetime(2022, 12, 20, 16, 45, 21, 924781), verbose_name='Дата редактирования'),
        ),
    ]
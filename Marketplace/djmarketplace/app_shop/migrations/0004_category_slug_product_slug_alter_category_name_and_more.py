# Generated by Django 4.1.4 on 2023-01-26 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_shop', '0003_alter_category_options_product_available_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default=1, max_length=200, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(db_index=True, max_length=200, verbose_name='Название Магазина'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(db_index=True, max_length=100, verbose_name='Название товара'),
        ),
    ]
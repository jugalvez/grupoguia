# Generated by Django 3.1.1 on 2022-01-17 06:58

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='purchase',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='purchase',
            name='total',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(default='', verbose_name='URL for search engines'),
        ),
    ]

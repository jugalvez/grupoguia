# Generated by Django 3.1.1 on 2022-01-17 00:11

from django.db import migrations, models
import django.db.models.deletion
import django_resized.forms


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('price', models.FloatField(default=0)),
                ('image', django_resized.forms.ResizedImageField(crop=None, force_format=None, keep_meta=True, null=True, quality=0, size=[800, 600], upload_to='img')),
                ('description', models.TextField()),
                ('sku', models.CharField(max_length=30)),
                ('seo_title', models.CharField(max_length=250)),
                ('seo_meta_description', models.TextField()),
                ('slug', models.SlugField(default='', verbose_name='URL for browsers')),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField(default=0)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
            ],
        ),
    ]

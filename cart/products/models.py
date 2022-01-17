#encoding:utf-8
from django.db import models
from django.utils.text import slugify
from django_resized import ResizedImageField
from django.utils import timezone


class Product(models.Model):
  name = models.CharField(max_length = 250)
  price = models.FloatField(default = 0)
  image = ResizedImageField(size=[800, 600], upload_to = 'img', null = True)
  description = models.TextField()
  sku = models.CharField(max_length = 30)
  seo_title = models.CharField(max_length = 250)
  seo_meta_description = models.TextField()
  quantity = models.IntegerField(default = 0)
  slug = models.SlugField('URL for search engines', default = '')
  pub_date = models.DateTimeField('date published')

  def __str__(self):
    return "%s" % self.name


class Purchase(models.Model):
  product = models.ForeignKey(Product, on_delete=models.CASCADE)
  price = models.FloatField(default = 0)
  quantity = models.IntegerField(default = 0)
  total = models.FloatField(default = 0)
  date = models.DateTimeField(default = timezone.now)

  def __str__(self):
    return "%s" % self.product.name
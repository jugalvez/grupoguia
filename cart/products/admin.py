from django.contrib import admin
from .models import Product, Purchase

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
  prepopulated_fields = {'slug' : ('name',)}


admin.site.register(Product, ProductAdmin)
admin.site.register(Purchase)
from django.contrib import admin
from .models import Product

# Register your models here.

#acesso do admin para produtos
admin.site.register(Product)

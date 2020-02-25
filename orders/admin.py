from django.contrib import admin
from .models import Order

#acesso do admin para pedidos
admin.site.register(Order)

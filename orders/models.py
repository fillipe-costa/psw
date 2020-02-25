from django.db import models
from django.contrib.auth.models import User
from products.models import Product

# model de pedidos
class Order(models.Model):
     product = models.ForeignKey(Product, on_delete = models.CASCADE)
     user = models.ForeignKey(User, on_delete = models.CASCADE)
     quantity = models.IntegerField()
     total_price = models.FloatField()
     paid = models.BooleanField(default = 'False')

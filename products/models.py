from django.db import models

# Create your models here.
class Product(models.Model):
    Name = models.CharField(max_length=12)
    Description = models.TextField()
    Price = models.FloatField()
    Date = models.DateTimeField(auto_now_add = True)
    Stock = models.IntegerField()

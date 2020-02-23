from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Costumer(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, related_name = 'costumer')
    address = models.CharField(max_length = 30)

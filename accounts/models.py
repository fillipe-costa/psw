from django.db import models
from django.contrib.auth.models import User

#model para adicionar o campo de endereço a model de user.
class Costumer(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, related_name = 'costumer')
    address = models.CharField(max_length = 30)

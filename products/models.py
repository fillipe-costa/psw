from django.db import models

#model de produtos
class Product(models.Model):
    name = models.CharField(max_length=12)
    description = models.TextField()
    price = models.FloatField()
    date = models.DateTimeField(auto_now_add = True)
    stock = models.IntegerField()

    #faz aparecer o nome do produto na tela do admin
    def __str__(self):
        return self.name

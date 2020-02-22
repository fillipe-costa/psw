from rest_framework import serializers

from .models import Product

#listagem dos produtos
class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name','price', 'stock')

#mostra os detalhes do produto
class ProductDetailsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'price', 'stock', 'date')

#dados que podem ser criados ou atualizados no produto
class CreateUpdateProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ('name', 'description', 'price', 'stock')

from rest_framework import serializers
from .models import Order
from products.models import Product
from django.contrib.auth import get_user_model

#listagem e detalhes dos pedidos
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


#campos de criação de pedidos
class CreateOrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ('product', 'quantity')

    def create(self, validated_data):

        #cria o pedido
        order = Order.objects.create(
            user = self.context['request'].user,
            product = Product.objects.get(name = validated_data['product']),
            quantity = validated_data['quantity'],
            total_price = Product.objects.get(name = validated_data['product']).price * validated_data['quantity']
        )

        #atualiza o estoque
        product = Product.objects.get(id = order.product.id)
        if (product.stock < order.quantity):
            #erro
        product.stock -= order.quantity

        product.save()
        order.save()

        return order

#campos de alteração de pedidos
class UpdateOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('quantity',)

    def update(self, order, validated_data):

        #ajusta o estoque
        product = Product.objects.get(id = order.product.id)
        if product.stock < validated_data['quantity']:
            #erro
        product.stock += order.quantity
        product.stock -= validated_data['quantity']

        order.quantity = validated_data['quantity']

        product.save()
        order.save()

        return order

from django.shortcuts import render
from rest_framework import viewsets
from .serializers import OrderSerializer, CreateOrderSerializer, UpdateOrderSerializer
from .models import Order
from products.models import Product
from .permissions import IsOrderOwner

from rest_framework.permissions import IsAuthenticated

class OrderViewSet(viewsets.ModelViewSet):

    queryset = Order.objects.all().order_by('id')
    permission_classes = (IsAuthenticated, IsOrderOwner)

    #retorna um serializer diferente para cada método
    def get_serializer_class(self):
        if self.action == 'create':
            return CreateOrderSerializer
        elif self.action == 'update':
            return UpdateOrderSerializer
        else:
            return OrderSerializer

    def get_queryset(self):
        if self.action == 'list':
            return self.queryset.filter(user = self.request.user)
        return self.queryset


    def destroy(self, request, *args, **kwargs):

        order = self.get_object()

        #ajusta estoque
        product = Product.objects.get(id = order.product.id)
        product.stock += order.quantity

        product.save()

        self.perform_destroy(order)

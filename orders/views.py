from django.shortcuts import render
from rest_framework import viewsets
from .serializers import OrderSerializer, CreateOrderSerializer, UpdateOrderSerializer, CheckoutSerializer
from .models import Order
from products.models import Product
from accounts.models import Costumer
from .permissions import IsOrderOwner
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response

import io
from django.http import FileResponse
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm

class OrderViewSet(viewsets.ModelViewSet):

    queryset = Order.objects.all().order_by('id')
    permission_classes = (IsAuthenticated, IsOrderOwner)

    #retorna um serializer diferente para cada método
    def get_serializer_class(self):
        if self.action == 'create':
            return CreateOrderSerializer
        elif self.action == 'update':
            return UpdateOrderSerializer
        elif self.action == 'checkout':
            return CheckoutSerializer
        else:
            return OrderSerializer

    def get_queryset(self):
        if self.action == 'list':
            return self.queryset.filter(user = self.request.user)
        return self.queryset

    #destroi pedido
    def destroy(self, request, *args, **kwargs):

        order = self.get_object()

        #ajusta estoque
        product = Product.objects.get(id = order.product.id)
        product.stock += order.quantity

        product.save()

        self.perform_destroy(order)

    #função de pagamento de pedidos
    @action(detail = True, methods = ['put'], name = 'checkout')
    def checkout(self, request, pk):

        order = self.get_object()

        if (order.paid == True):
            return Response('already paid')

        order.paid = 'True'

        order.save()

        costumer = Costumer.objects.get(user_id = order.user.id)


        buffer = io.BytesIO()
        p = canvas.Canvas(buffer)

        #gera PDF
        textobject = p.beginText(0 * mm, 280 * mm)
        textobject.setFont('Times-Roman', 8)
        textobject.textLine(text='{ Product: ' + str(order.product)
        + ' Quantity: ' + str(order.quantity)
        + ' Price: ' + str(order.total_price)
        + ' Address: ' + costumer.address + ' }'
        )
        p.drawText(textobject)

        p.showPage()
        p.save()

        buffer.seek(io.SEEK_SET)
        return FileResponse(buffer, as_attachment=True, filename='receipt.pdf')

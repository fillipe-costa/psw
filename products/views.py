from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ProductSerializer, ProductDetailsSerializer, CreateUpdateProductSerializer
from .models import Product
from .permissions import IsOwnerOrReadOnly

class ProductViewSet(viewsets.ModelViewSet):
    
    queryset = Product.objects.all().order_by('id')
    permission_classes = (IsOwnerOrReadOnly,)

    #retorna um serializer diferente para cada método
    def get_serializer_class(self):
        if self.action == 'retrieve':
            return ProductDetailsSerializer
        elif self.action == 'create' or self.action == 'update':
            return CreateUpdateProductSerializer
        else:
            return ProductSerializer

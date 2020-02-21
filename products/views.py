from django.shortcuts import render
from .models import Product
from django.http import HttpResponse

# Create your views here.

#função index, lista todos os produtos
def get_products_list(request):
    products = Product.objects.all().values('id','name','price','stock')
    products_list = list(products)
    return HttpResponse(products_list)

#função para mostrar detalhes de um produto
def get_product(request, product_id):
    product = Product.objects.all().filter(id = product_id).values('id','name','description','price','date','stock')
    return HttpResponse(product)

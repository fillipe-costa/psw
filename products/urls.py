from django.urls import path
from . import views

urlpatterns = [

    path('', views.get_products_list), #rota GET que lista todos os produtos criados
    path('<int:product_id>/', views.get_product) #rota GET que mostra os detalhes de um produto
]

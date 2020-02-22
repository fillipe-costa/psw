administrador:
login: admin
senha: admin

rotas:

/products
-exibe uma lista com todos os produtos
-caso seja administrador permite a criação de novos produtos

/products/{id}
-exibe detalhes do produto com o id inserido
-caso seja administrador permite alterar dados como preço e estoque ou deletar o produto

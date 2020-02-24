administrador:
login: admin
senha: admin

rotas:

/products
-exibe uma lista com todos os produtos(GET)
-caso seja administrador permite a criação de novos produtos(POST)

/products/{id}
-exibe detalhes do produto com o id inserido(GET)
-caso seja administrador permite alterar dados como preço e estoque ou deletar o produto

/account/Register
-registro de novo usuário comum

/api-token-auth
-Rota POST que retorna o token do usuario(usar postman)

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

/orders
-exibe a lista de todos os pedidos do usuário logado
-permite a criação de novos pedidos

/orders/{id}
- exibe detalhes do pedido com id inserido
- permite alterar a quantidade pedida ou deletar o pedido

/orders/{id}/checkout
-Permite a alteração do campo 'paid' de false para true
-Gera um PDF contendo detalhes do pedido e endereço de entrega

/account/Register
-registro de novo usuário comum

/api-token-auth
-Rota POST que retorna o token do usuario(usar postman)

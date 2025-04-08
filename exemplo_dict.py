produto_01 = {
    "nome":"Sapato",
    "quantidade":25,
    "preco":10.38,
    "disponibiidade":True
}

produto_02 = {
    "nome":"Camiseta",
    "quantidade":58,
    "preco":5.38,
    "disponibiidade":False
}

produto_03 = {
    "nome":"calca",
    "quantidade":2,
    "preco":38.50,
    "disponibiidade":True
}

carrinho: list = []

carrinho.append(produto_01)
carrinho.append(produto_02)
carrinho.append(produto_03)

print(carrinho)
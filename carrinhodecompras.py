"""
Thales Eduardo de Castro Andrade
Trabalho final POO
Junho de 2024
"""

"""
Essa classe basicamente é responsável por criar uma lista de itens.
Ela começa vazia, e conforme o código vai rodando, eu posso tanto addItens quanto removerItens.
Além disso, ela tem uma funçãozinha para calcular preço total dos itens que estão em sua lista.
"""

class CarrinhoDeCompras:
    def __init__(self):
        self.itens = []

    def addItem(self, item):
        self.itens.append(item)

    def removerItem(self, index):
        del self.itens[index]

    def calcularTotal(self):
        total = 0
        for item in self.itens:
            total += item['preco'] * item['quantidade']
        return total

carrinho = CarrinhoDeCompras()

            
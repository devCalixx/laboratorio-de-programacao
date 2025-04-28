class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def calcular_valor_total(self):
        return self.preco * self.quantidade
    
    def atualizar_quantidade(self, nova_quantidade):
        self.quantidade = nova_quantidade

    def detalhes(self):
        print(f"Nome do produto: {self.nome}")
        print(f"Preço do produto: {self.preco}")
        print(f"Quantidade do produto: {self.quantidade}")
        print(f"Valor total: R${self.calcular_valor_total():.2f}")
        print("-" * 30)

produtos = [
    Produto("Lápis", 2.50, 3),
    Produto("Caderno", 15, 5),
    Produto("Caneta", 3.50, 4)
]

print("Dados antes da atualização:\n" + "-" * 30)
for produto in produtos:
    produto.detalhes()

produtos[0].atualizar_quantidade(10)
produtos[1].atualizar_quantidade(9)
produtos[2].atualizar_quantidade(8)

print("\nDados depois da atualização:\n" + "-" * 30)
for produto in produtos:
    produto.detalhes()
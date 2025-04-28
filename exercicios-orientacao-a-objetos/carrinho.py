class Carrinho:
    def __init__(self):
        self.qtd_produtos = 0

    def adicionar_produtos(self):
        nova_quantidade = int(input(f"Quantos produtos quer adicionar?: "))
        self.qtd_produtos += nova_quantidade
    
    def detalhes(self):
        print(f"A quantidade de produtos no seu carrinho é: {self.qtd_produtos}")

carrinho = Carrinho()

while True: 
    opcao = input(f"-" * 30 + "\nBem vindo ao E-Commerce!\nComo posso te ajudar?\n1- Visualizar seu carrinho\n2- Adicionar produtos no seu carrinho\n3- Fechar programa\nDigite sua opção: ")

    if(opcao == "1"):
        carrinho.detalhes()
    elif(opcao == "2"):
        carrinho.adicionar_produtos()
    elif(opcao == "3"):
        print("Obrigado por ter usado o E-Commerce!")
        break
    else:
        print("Opção inválida. Digite 1, 2 ou 3")

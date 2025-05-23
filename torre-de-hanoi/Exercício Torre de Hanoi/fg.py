class Disco:
    def __init__(self, nome, cor, tamanho):
        self.nome = nome
        self.cor = cor
        self.tamanho = tamanho

    def exibir_nome_disco(self):
        print(f"{self.nome}")


class Poste:
    def __init__(self, nome):
        self.nome = nome
        self.discos = []  # Renomeado para 'discos'

    def adicionar_disco(self, disco):
        self.discos.append(disco)

    def exibir_detalhes(self):
        print(f"Poste {self.nome}: ", end="")
        if self.discos:
            for disco in self.discos:
                print(f"{disco.nome} (tamanho: {disco.tamanho})", end=", ")
        else:
            print("Nenhum disco")
        print()  # Nova linha após a exibição


# Criando discos
discos = [
    Disco("n1", "", 1),
    Disco("n2", "", 2),
    Disco("n3", "", 3),
    Disco("n4", "", 4),
    Disco("n5", "", 5)
]

# Criando postes
postes = [
    Poste("A"),
    Poste("B"),
    Poste("C")
]

# Adicionando discos ao poste A
for disco in discos:
    postes[0].adicionar_disco(disco)  # Adiciona todos os discos ao poste A

# Exibindo detalhes
print("===== Torre de Hanoi =====\n")
for poste in postes:
    poste.exibir_detalhes()

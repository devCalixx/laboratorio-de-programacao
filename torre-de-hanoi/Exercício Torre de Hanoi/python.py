class Disco:
    def __init__(self, nome, cor, tamanho):
        self.nome = nome
        self.cor = cor
        self.tamanho = tamanho

class Poste:
    def __init__(self, nome):
        self.nome = nome
        self.discos = list()

    def adicionar_disco(self, disco):
        self.discos.append(disco)

    def exibir_detalhes(self):
        print(f"Poste {self.nome}: ", end=" ")
        if self.discos:
            for disco in self.discos:
                print(f" Disco {disco.tamanho}", end=", ")
        else:
            print("Nenhum disco")
        print()
    
    def mover_disco(self, poste_escolhido):
        if not self.discos:
            print(f"Não há discos para mover no poste {self.nome}")
            return False
        
        disco_para_mover = self.discos[-1]
        if poste_escolhido.discos:
            disco_no_topo_escolhido = poste_escolhido.discos[-1]
            if disco_para_mover.tamanho > disco_no_topo_escolhido.tamanho:
                print(f"Não é permitido colocar um disco maior em cima de um menor.")
                return False
            
        self.discos.pop()
        poste_escolhido.discos.append(disco_para_mover)
        print(f"Movido disco tamanho {disco_para_mover.tamanho} do poste {self.nome} para o poste {poste_escolhido.nome}.")
        return True


"""discos = [
    Disco("n1", "", 1),
    Disco("n2", "", 2),
    Disco("n3", "", 3),
    Disco("n4", "", 4),
    Disco("n5", "", 5)
]"""

n1 = Disco("n1", "", 1)
n2 = Disco("n2", "", 2)
n3 = Disco("n3", "", 3)
n4 = Disco("n4", "", 4)
n5 = Disco("n5", "", 5)

discos = [n5, n4, n3, n2, n1]

postes = [
    Poste("A"),
    Poste("B"),
    Poste("C")
] 

postes[0].adicionar_disco(n1)
postes[0].adicionar_disco(n2)
postes[0].adicionar_disco(n3)
postes[0].adicionar_disco(n4)
postes[0].adicionar_disco(n5)

while True:
    print("=====Torre de Hanoi=====\n")
    for poste in postes:
        poste.exibir_detalhes()

    poste_origem = input("De qual poste você quer mover o disco? A, B ou C?: ")
    poste_escolhido = input("Para qual poste você quer mover o disco? A, B ou C?: ")
    poste.mover_disco(poste_escolhido)
        
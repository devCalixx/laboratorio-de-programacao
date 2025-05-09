class Jogo:
    
    def __init__(self, titulo, genero, classificacao, preco, avaliacao, descricao, data, dev, id):
        self.titulo = titulo
        self.genero = genero
        self.classificacao = classificacao
        self.preco = preco
        self.avaliacao = avaliacao
        self.descricao = descricao
        self.data = data
        self.dev = dev
        self.id = id
        
    def detalhes(self):
        print(f"Nome: {self.titulo}")
        print(f"Gênero: {self.genero}")
        print(f"Classificação Indicativa: {self.classificacao}")
        print(f"Preço: {self.preco}")
        print(f"Nota: {self.avaliacao}")
        print(f"Descrição: {self.descricao}")
        print(f"Desenvolvedor/a: {self.dev}")
        print(f"ID: {self.id}")
        print(f"-" * 30)    
    
jogos = [
    Jogo(
        "Dark Souls Remastered",
        "Souls-Like",
        "+18",
        80,
        9.5,
        "JOGO FODA!!!",
        "20/03/2014",
        "Fromsoftware",
        1
    ),
    Jogo(
        "Brawhalla",
        "Luta-Plataforma",
        "+10",
        0,
        7.3,
        "jogo MERDA!!!",
        "05/07/2012",
        "Ubisoft",
        2
    )
]
for jogo in jogos: 
    jogo.detalhes()

class Jogador:
    def __init__ (self, nickname, id_jogador, biblioteca_de_jogos, saldo_carteira, conquistas, nivel, grupo):
        self.nickname = nickname
        self.id_jogador = id_jogador
        self.biblioteca_de_jogos = biblioteca_de_jogos
        self.saldo_carteira = saldo_carteira
        self.conquistas = conquistas
        self.nivel = nivel
        self.grupo = grupo
        
    def exibir_perfil(self):
        print(f"Nickname: {self.nickname}")
        print(f"ID do jogador: {self.id_jogador}")
        print(f"Biblioteca de jogos do jogador: \n {self.biblioteca_de_jogos}")
        print(f"Saldo na carteira: {self.saldo_carteira}")
        print(f"Conquistas: \n {self.conquistas}")
        print(f"Nível: {self.nivel}")
        print(f"Grupo: {self.grupo}")
        print(f"-" * 30)              

    def adicionar_jogo_biblioteca(self, jogo_procurado):
        jogo_procurado = input("Qual jogo você quer adicionar?: ")
        for Jogo in jogos:
            if(jogo_procurado in jogos):
                print(f"Preço do jogo: {self.preco}")
                def debitar_saldo(self):
                    if self.preco <= self.saldo_carteira:
                        print(True)
                        self.saldo_carteira -= self.preco
                        print(f"Novo saldo: {self.saldo_carteira}")
                        self.biblioteca_de_jogos.append(jogo_procurado)
                    else:
                        print(False)
                        print(f"Valor insuficiente para compra.")
        
    def adicionar_saldo(self, valor):
        self.saldo_carteira += valor
        

jogadores = [
    Jogador(
        "juliaememo", 
        "#1234", 
        [""], 
        0.0, 
        [""], 
        10, 
        "Ememo"),
    Jogador(
        "hama",
        "#4321",
        [""],
        0.0,
        [""],
        20,
        "Slovers"
    )
]

print(f"Seja bem-vindo à cAXcAX.\nDigite seu nickname para prosseguir dentro da sua conta.")
usuario = input("Usuário: ")
for Jogador in jogadores:
    if (usuario in jogadores):
        while True:
            opcao = input(f"O que você deseja fazer?\nExibir perfil: 1\nVer catálogo de jogos: 2\nComprar jogo: 3\nVer perfil de outro jogador: 4")
            if (opcao = 1):
                Jogador.detalhes()
            elif (opcao = 2):
            elif (opcao = 3):
            elif (opcao = 4):
            else:
                print(f"Opção não encontrada. Escolha outra opção")
    else:
        print(f"Jogador não encontrado.")


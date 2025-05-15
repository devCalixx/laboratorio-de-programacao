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

    def adicionar_jogo_biblioteca(self, jogo_procurado, biblioteca_de_jogos):
        jogo_procurado = input("Qual jogo você quer adicionar?: ")
        for Jogo in jogos:
            if(jogo_procurado in jogos):
                if(jogo_procurado in biblioteca_de_jogos):
                    print(f"Você já possui esse jogo.")
                else:
                    print(f"Preço do jogo: {self.preco}")
                    verificar_compra = input(f"Realizar compra?\n----------\nDigite 1 para SIM\nDigite 2 para NÃO")
                    if verificar_compra == 1:
                        def debitar_saldo(self):
                            if self.preco <= self.saldo_carteira:
                                print(True)
                                self.saldo_carteira -= self.preco
                                print(f"Novo saldo: {self.saldo_carteira}")
                                self.biblioteca_de_jogos.append(jogo_procurado)
                                print(f"Novo jogo: {self.titulo}")
                            else:
                                print(False)
                                print(f"Valor insuficiente para compra.")
                    elif verificar_compra == 2:
                        break
                    else:
                        print(f"Opção inválida")
        
    def adicionar_saldo(self, dinheiro):
        self.dinheiro = dinheiro
        print(f"Saldo anterior: {self.saldo_carteira}")
        self.saldo_carteira += dinheiro
        print(f"Novo saldo: {self.saldo_carteira}")
        

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

class Plataforma:

    def __init__(self, nome, catalogo_de_jogos, jogadores_cadastrados):
        self.nome = nome
        self.catalogo_de_jogos = catalogo_de_jogos
        self.jogadores_cadastrados = jogadores_cadastrados

    def adicionar_jogo(self, jogo):
        self.catalogo_de_jogos.append(jogo)

    def adicionar_jogador(self, jogador):
        self.jogadores_cadastrados.append(jogador)

    def buscar_jogo_por_nome(self, nome_jogo, catalogo_de_jogos):
        nome_jogo = input(f"Digite o nome do jogo: ")
        for jogo in catalogo_de_jogos:
            if(jogo.titulo.lower() == nome_jogo.lower()): 
                return jogo
        return None

    def buscar_jogador_por_id(self, id_jogador, jogadores_cadastrados):
        nome_jogo = input(f"Digite o ID do usuário: ")
        for jogador in jogadores_cadastrados:
            if(jogador.id == id_jogador):
                return jogador
        return None

    def listar_catalogo(self):
        print(f"Seja bem-vindo ao catálogo de jogos de cAXcAX!\n")
        for idx, jogo in enumerate(self.catalogo_de_jogos, start=1):
            print(f"[{idx}]")
            jogo.detalhes()
            
    catalogo = [
        
    ]



print(f"Seja bem-vindo à cAXcAX.\nDigite seu nickname para prosseguir dentro da sua conta.")
usuario = input("Usuário: ")
for Jogador in jogadores:
    if usuario == Jogador.nickname:
        while True:
            opcao = input(f"O que você deseja fazer?\n----------------------\nExibir perfil: 1\nVer biblioteca de jogos: 2\nComprar jogo: 3\nVer perfil de outro jogador: 4\nVer catálogo de jogos da plataforma: 5\nAdicionar saldo na carteira: 6\n-------------------\nDigite sua opção: ")
            if opcao == "1":
                print(f"Seu perfil\n" + "-" *30)
                Jogador.exibir_perfil()
            elif opcao == "2":
                print(f"Sua biblioteca de jogos" + "-" *30)
                Jogador.biblioteca_de_jogos()
            elif opcao == "3":
                Jogador.adicionar_jogo_biblioteca()
            elif opcao == "4":
                id_ou_nome = input(f"Busca por ID ou nome?\n1: ID\n2: nome")
                if id_ou_nome == "1":
                    Plataforma.buscar_jogador_por_id
                elif id_ou_nome == "2":
                    Plataforma.buscar_jogo_por_nome
                else:
                    print(f"Opção inválida")
            elif opcao == "5":
                Plataforma.listar_catalogo()
            elif opcao == "6":
                valor = float(input("Quanto quer adicionar?: "))
                Jogador.adicionar_saldo(valor)
            else:
                print(f"Opção não encontrada. Escolha outra opção")
    else:
        print(f"Jogador não encontrado.")


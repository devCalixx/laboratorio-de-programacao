class Jogo:
    
    def __init__(self, titulo, genero, classificacao, preco, avaliacao, descricao, data, dev, id):
        self.titulo = titulo
        self.genero = genero
        self.classificacao = classificacao
        self.preco = preco
        self.avaliacao = avaliacao
        self.total_avaliacoes = 0
        self.soma_avaliacoes = 0
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

class Plataforma:

    def __init__(self, nome, catalogo_de_jogos, jogadores_cadastrados):
        self.nome = nome
        self.catalogo_de_jogos = catalogo_de_jogos
        self.jogadores_cadastrados = jogadores_cadastrados

    def adicionar_jogo(self, jogo):
        self.catalogo_de_jogos.append(jogo)

    def adicionar_jogador(self, jogador):
        self.jogadores_cadastrados.append(jogador)

    def buscar_jogo_por_nome(self, nome_jogo):
        for jogo in self.catalogo_de_jogos:
            if jogo.titulo.lower() == nome_jogo.lower(): 
                return jogo
        return None

    def buscar_jogador_por_nome(self, nick_jogador, jogadores_cadastrados):
        for jogador in jogadores_cadastrados:
            if(jogador.nickname == nick_jogador):
                return jogador
        return None

    def buscar_jogador_por_id(self, id_jogador, jogadores_cadastrados):
        for jogador in jogadores_cadastrados:
            if jogador.id_jogador == id_jogador:
                return jogador
        return None

    def listar_catalogo(self):
        print(f"Seja bem-vindo ao catálogo de jogos de cAXcAX!\n")
        for idx, jogo in enumerate(self.catalogo_de_jogos, start=1):
            print(f"[{idx}]")
            jogo.detalhes()

    def avaliar_jogo(self):
        nome_jogo = input("Qual jogo deseja avaliar?: ")
        jogo = self.buscar_jogo_por_nome(nome_jogo)
        if jogo:
            try:
                nova_avaliacao = float(input(f"Avalie o jogo '{jogo.titulo}' de 0 a 10: "))
                if 0 <= nova_avaliacao <= 10:
                    jogo.total_avaliacoes += 1
                    jogo.soma_avaliacoes += nova_avaliacao
                    jogo.avaliacao = jogo.soma_avaliacoes / jogo.total_avaliacoes
                    print(f"Obrigada por avaliar o jogo {jogo.titulo}. A nova avaliação do jogo é: {jogo.avaliacao:.2f}")
                else:
                    print("A validação deve estar entre 0 e 10.")
            except ValueError:
                print("Por favor, digite um número válido.")
        else:
            print("Jogo não encontrado no catálogo.")
            
class Jogador:
    def __init__ (self, nickname, id_jogador, biblioteca_de_jogos, saldo_carteira, nivel, grupo):
        self.nickname = nickname
        self.id_jogador = id_jogador
        self.biblioteca_de_jogos = biblioteca_de_jogos
        self.saldo_carteira = saldo_carteira
        self.nivel = nivel
        self.grupo = grupo
        
    def exibir_perfil(self):
        print(f"Nickname: {self.nickname}")
        print(f"ID do jogador: {self.id_jogador}")
        print(f"Biblioteca de jogos do jogador: ")
        if not self.biblioteca_de_jogos:
            print("Nenhum jogo na biblioteca.")
        else:
            for jogo in self.biblioteca_de_jogos:
                if isinstance(jogo, Jogo):
                    print(f"- {jogo.titulo}")
                else:
                    print(f"- {jogo}")
        print(f"Saldo na carteira: {self.saldo_carteira}")
        print(f"Nível: {self.nivel}")
        print(f"Grupo: {self.grupo}")
        print(f"-" * 30)

    def debitar_saldo(self, valor):
        if valor <= self.saldo_carteira:
            self.saldo_carteira -= valor
            return True
        else:
            return False             

    def adicionar_jogo_biblioteca(self, plataforma):
        nome_jogo = input("Qual jogo você quer comprar?: ")

        jogo_encontrado = None
        for jogo in plataforma.catalogo_de_jogos:
            if jogo.titulo.lower() == nome_jogo.lower():
                jogo_encontrado = jogo
                break
        if not jogo_encontrado:
            print("Jogo não encontrado no catálogo.")
            return
        if jogo_encontrado in self.biblioteca_de_jogos:
            print("Você já possui esse jogo.")
            return
        print(f"Preço do jogo: R${jogo_encontrado.preco:.2f}")
        print(f"Saldo na carteira: R${jogador_logado.saldo_carteira}")
        verificar_compra = input(f"Realizar compra?\n----------\nDigite 1 para SIM\nDigite 2 para NÃO\nOpção: ")
        if verificar_compra == "1":
            if self.debitar_saldo(jogo_encontrado.preco):
                self.biblioteca_de_jogos.append(jogo_encontrado)
                print(f"Compra realizada com sucesso! {jogo_encontrado.titulo} adicionado à sua biblioteca.")
                print(f"Novo saldo: R${self.saldo_carteira:.2f}")
            else:
                print(f"Valor insuficiente para compra.")
        elif verificar_compra == 2:
            print("Compra cancelada.")
        else:
            print(f"Opção inválida")
        
    def adicionar_saldo(self, valor):
        self.valor = valor
        print(f"Saldo anterior: {self.saldo_carteira}")
        self.saldo_carteira += valor
        print(f"Novo saldo: {self.saldo_carteira}")

    def exibir_biblioteca(self):
        print(f"Biblioteca de jogos de {self.nickname}:")
        if not self.biblioteca_de_jogos or self.biblioteca_de_jogos == [""]:
            print("Nenhum jogo na biblioteca.")
        else:
            for jogo in self.biblioteca_de_jogos:
                if isinstance(jogo, Jogo):
                    print(f"\nNome: {jogo.titulo}")
                else:
                    print(jogo)  # fallback, caso esteja só o nome
        print("-" * 30)

    def presentear_jogador(self, plataforma):
        nome_jogo = input("Digite o nome do jogo que deseja presentear: ")
        jogo_encontrado = None
        for jogo in self.biblioteca_de_jogos:
            if isinstance(jogo, Jogo) and jogo.titulo.lower() == nome_jogo.lower():
                jogo_encontrado = jogo
                break
        
        if not jogo_encontrado:
            print("Você não possui esse jogo na sua biblioteca. Portanto, não pode presentear.")
            return
        
        nickname_presenteado = input("Digite o nome de usuário do jogador que deseja presentear: ")
        jogador_presenteado = plataforma.buscar_jogador_por_nome(nickname_presenteado, plataforma.jogadores_cadastrados)

        if not jogador_presenteado:
            print("Jogador não encontrado.")
            return
        
        if jogo_encontrado in jogador_presenteado.biblioteca_de_jogos:
            print("O jogador já possui esse jogo.")
            return
        
        jogador_presenteado.biblioteca_de_jogos.append(jogo_encontrado)
        self.biblioteca_de_jogos.remove(jogo_encontrado)
        print(f"Presente enviado com sucesso! {jogo_encontrado.titulo} foi adicionado à biblioteca de {jogador_presenteado.nickname}.")
        

jogadores = [
    Jogador(
        "juliaememo", 
        "1234", 
        [], 
        0.0,
        10, 
        "Ememo"),
    Jogador(
        "hama",
        "4321",
        [],
        0.0,
        20,
        "Slovers"
    )
]

jogos = [
    Jogo(
        "Dark Souls Remastered",
        "Souls-Like",
        "+18",
        80,
        0,
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
        0,
        "jogo MERDA!!!",
        "05/07/2012",
        "Ubisoft",
        2
    )
]

def encontrar_jogador_por_nickname(nickname):
    for jogador in jogadores:
        if jogador.nickname == nickname:
            return jogador
    return None

def gerar_id_jogador():
    return f"#{1000 + len(jogadores) + 1}"

def gerar_id_jogo():
    return f"#{len(jogos) + 1}"

plataforma = Plataforma("cAXcAX", catalogo_de_jogos=[], jogadores_cadastrados=[])
for jogo in jogos:
    plataforma.adicionar_jogo(jogo)
for jogador in jogadores:
    plataforma.adicionar_jogador(jogador)

    cadastro_entrada = input(f"Seja bem-vindo à cAXcAX!\nCadastre-se ou entre na sua conta.\n------------\nDigite 1 para se cadastrar\nDigite 2 para entrar na sua conta.\nOpção: ")
    jogador_logado = None
    
    if cadastro_entrada == "1":
        nickname_novo = input("Digite seu nickname para cadastro: ")
        if encontrar_jogador_por_nickname(nickname_novo):
            print("Esse nickname já está em uso. Tente entrar na conta ou use outro nickname")
        else:
            novo_id = gerar_id_jogador()
            novo_jogador = Jogador(nickname_novo, novo_id, [], 0.0, 1, "Novato")
            jogadores.append(novo_jogador)
            plataforma.adicionar_jogador(novo_jogador)
            jogador_logado = novo_jogador
            print(f"Cadastro realizado com sucesso! Seja bem-vindo {nickname_novo}, seu ID é {novo_id}.\n")
    elif cadastro_entrada == "2":
        nickname_entrada = input(f"Digite seu nickname para entrar: ")
        jogador_logado = encontrar_jogador_por_nickname(nickname_entrada)
        if not jogador_logado:
            print("Jogador não encontrado. Tente se cadastrar.")
    else:
        print("Opção inválida. Reinicie o programa.")

    if jogador_logado:
        print(f"\nOlá, {jogador_logado.nickname}! Você está logado.\n")
        while True:
            opcao = input(f"O que você deseja fazer?\n----------------------\nExibir perfil: 1\nVer biblioteca de jogos: 2\nComprar jogo: 3\nVer perfil de outro jogador: 4\nVer catálogo de jogos da plataforma: 5\nAdicionar saldo na carteira: 6\nAvaliar um jogo na plataforma: 7\nAdicionar um jogo à plataforma: 8\nPresentear outro jogador: 9\nSair da plataforma: 0\n-------------------\nDigite sua opção: ")
            if opcao == "1":
                print(f"Seu perfil\n" + "-" *30)
                jogador_logado.exibir_perfil()
            elif opcao == "2":
                print(f"Sua biblioteca de jogos\n" + "-" *30)
                jogador_logado.exibir_biblioteca()
            elif opcao == "3":
                jogador_logado.adicionar_jogo_biblioteca(plataforma)
            elif opcao == "4":
                id_ou_nome = input(f"Busca por ID ou nome?\n1: ID\n2: nome\nOpção: ")
                if id_ou_nome == "1":
                    id_busca = input("Digite o ID do jogador: ")
                    jogador_encontrado = plataforma.buscar_jogador_por_id(id_busca, jogadores)
                    if jogador_encontrado:
                        print(f"Perfil do jogador:\n")
                        jogador_encontrado.exibir_perfil()
                    else:
                        print("Jogador não encontrado")
                elif id_ou_nome == "2":
                    nome_busca = input("Digite o nome de usuário do jogador: ")
                    jogador_encontrado = plataforma.buscar_jogador_por_nome(nome_busca, jogadores)
                    if jogador_encontrado:
                        print(f"Perfil do jogador:\n")
                        jogador_encontrado.exibir_perfil()
                    else:
                        print("Jogador não encontrado")
                else:
                    print(f"Opção inválida")
            elif opcao == "5":
                plataforma.listar_catalogo()
            elif opcao == "6":
                valor = float(input("Quanto quer adicionar?: "))
                jogador_logado.adicionar_saldo(valor)
            elif opcao == "7":
                plataforma.avaliar_jogo()
            elif opcao == "8":
                nome_jogo_novo = input(f"Seja bem-vindo, desenvolvedor.\nTítulo do jogo: ")
                if plataforma.buscar_jogo_por_nome(nome_jogo_novo):
                    print("Esse jogo já foi cadastrado. Tente novamente.")
                else:
                    genero_novo = input("Gênero do jogo: ")
                    classificacao_nova = input("Classificação indicativa do jogo: ")
                    preco_novo = float(input(f"Preço do jogo: R$"))
                    avaliacao_nova = 0
                    descricao_nova = input("Descrição do jogo: ")
                    data_nova = input("Data de lançamento: ")
                    dev_novo = input("Desenvolvedor do jogo: ")
                    novo_id_jogo = gerar_id_jogo()
                    jogo_novo = Jogo(nome_jogo_novo, genero_novo, classificacao_nova, preco_novo, avaliacao_nova, descricao_nova, data_nova, dev_novo, novo_id_jogo)
                    jogos.append(jogo_novo)
                    plataforma.adicionar_jogo(jogo_novo)
                    print("\nJogo cadastrado com sucesso!\nDetalhes do jogo: ")
                    jogo_novo.detalhes()
            elif opcao == "9":
                jogador_logado.presentear_jogador(plataforma)
            elif opcao == "0":
                print("Até a próxima!")
                break
            else:
                print(f"Opção não encontrada. Escolha outra opção")
    else:
        print(f"Jogador não encontrado.")
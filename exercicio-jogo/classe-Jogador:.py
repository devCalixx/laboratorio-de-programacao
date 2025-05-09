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

    def adicionar_jogo_biblioteca(self, jogo_comprado):
        self.biblioteca_de_jogos.append(jogo_comprado)
        
    def adicionar_saldo(self, valor):
        self.saldo_carteira += valor
        
    def debitar_saldo(self, valor):
        if valor <= self.saldo_carteira:
            self.saldo_carteira -= valor
        else:
            print("Valor insuficiente para débito")

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

for Jogador in jogadores:
    Jogador.exibir_perfil()
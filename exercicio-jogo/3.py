class Jogo:
    
    def __init__(self, titulo, genero, classificacao, preco, avaliacao, descricao, data, dev):
        self.titulo = titulo
        self.genero = genero
        self.classificacao = classificacao
        self.preco = preco
        self.avaliacao = avaliacao
        self.descricao = descricao
        self.data = data
        self.dev = dev
    def detalhes(self):
        print(f"Nome: {self.titulo}")
        print(f"Gênero: {self.genero}")
        print(f"Classificação Indicativa: {self.classificacao}")
        print(f"Preço: {self.preco}")
        print(f"Nota: {self.avaliacao}")
        print(f"Descrição: {self.descricao}")
        print(f"Desenvolvedor/a: {self.dev}")
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
        "Fromsoftware"
    ),
    Jogo(
        "Brawhalla",
        "Luta-Plataforma",
        "+10",
                0,
        7.3,
        "jogo MERDA!!!",
        "05/07/2012",
        "Ubisoft"
    )
]
for jogo in jogos:  # It's a good practice to use lowercase for variable names
    jogo.detalhes()

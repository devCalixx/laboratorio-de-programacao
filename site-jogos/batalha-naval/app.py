from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)

# ==========================
# CLASSES DO JOGO
# ==========================

class Navio:
    def __init__(self, tamanho, coordenadas):
        self.tamanho = tamanho
        self.coordenadas = coordenadas
        self.acertos = set()

    def foi_afundado(self):
        return len(self.acertos) == self.tamanho

    def verificar_tiro(self, tiro):
        if tiro in self.coordenadas:
            self.acertos.add(tiro)
            return True
        return False

class Tabuleiro:
    def __init__(self, tamanho=10):
        self.tamanho = tamanho
        self.grid = [['~' for _ in range(tamanho)] for _ in range(tamanho)]
        self.navios = []

    def pode_posicionar(self, coordenadas):
        for (x, y) in coordenadas:
            if not (0 <= x < self.tamanho and 0 <= y < self.tamanho):
                return False
            if self.grid[x][y] == 'N':
                return False
        return True

    def posicionar_navio(self, navio):
        self.navios.append(navio)
        for (x, y) in navio.coordenadas:
            self.grid[x][y] = 'N'

    def receber_tiro(self, x, y):
        if self.grid[x][y] in ['X', 'O']:
            return "Esse local já foi atingido."
        for navio in self.navios:
            if navio.verificar_tiro((x, y)):
                self.grid[x][y] = 'X'
                if navio.foi_afundado():
                    return "Afundou um navio!"
                else:
                    return "Acertou!"
        self.grid[x][y] = 'O'
        return "Água!"

    def todos_afundados(self):
        return all(navio.foi_afundado() for navio in self.navios)

    def exibir_web(self, revelar_navios=False):
        html = '<table class="grid">'
        for i in range(self.tamanho):
            html += '<tr>'
            for j in range(self.tamanho):
                celula = self.grid[i][j]
                if celula == 'N' and not revelar_navios:
                    celula = '&nbsp;'
                elif celula == '~':
                    celula = '&nbsp;'
                html += f'<td>{celula}</td>'
            html += '</tr>'
        html += '</table>'
        return html

def posicionar_navios_automatico(tabuleiro, informacoes_navios):
    for tamanho in informacoes_navios.values():
        while True:
            horizontal = random.choice([True, False])
            if horizontal:
                x = random.randint(0, tabuleiro.tamanho - 1)
                y = random.randint(0, tabuleiro.tamanho - tamanho)
                coordenadas = [(x, y + i) for i in range(tamanho)]
            else:
                x = random.randint(0, tabuleiro.tamanho - tamanho)
                y = random.randint(0, tabuleiro.tamanho - 1)
                coordenadas = [(x + i, y) for i in range(tamanho)]
            if tabuleiro.pode_posicionar(coordenadas):
                navio = Navio(tamanho, coordenadas)
                tabuleiro.posicionar_navio(navio)
                break

# ==========================
# CONFIGURAÇÃO DO JOGO
# ==========================

informacoes_navios = {
    "destroier": 2,
    "cruzador": 3,
    "submarino": 3,
    "encouraçado": 4,
    "porta-aviões": 5
}

# inicializa o jogo
tabuleiro_jogador = Tabuleiro()
tabuleiro_computador = Tabuleiro()
mensagem = "Bem-vindo ao Batalha Naval Flask!"
posicionar_navios_automatico(tabuleiro_jogador, informacoes_navios)
posicionar_navios_automatico(tabuleiro_computador, informacoes_navios)

# ==========================
# ROTAS FLASK
# ==========================

@app.route("/")
def index():
    return render_template("index.html",
                           jogador_grid=tabuleiro_jogador.exibir_web(revelar_navios=True),
                           computador_grid=tabuleiro_computador.exibir_web(revelar_navios=False),
                           mensagem=mensagem)

@app.route("/atacar", methods=["POST"])
def atacar():
    global mensagem
    try:
        x = int(request.form.get("linha"))
        y = int(request.form.get("coluna"))
    except (TypeError, ValueError):
        mensagem = "Coordenadas inválidas!"
        return redirect(url_for("index"))

    if not (0 <= x < 10 and 0 <= y < 10):
        mensagem = "Coordenadas fora do tabuleiro!"
        return redirect(url_for("index"))

    resultado = tabuleiro_computador.receber_tiro(x, y)
    mensagem = resultado

    if tabuleiro_computador.todos_afundados():
        mensagem += " 🎉 Você venceu!"

    return redirect(url_for("index"))

@app.route("/reiniciar")
def reiniciar():
    global tabuleiro_jogador, tabuleiro_computador, mensagem
    tabuleiro_jogador = Tabuleiro()
    tabuleiro_computador = Tabuleiro()
    posicionar_navios_automatico(tabuleiro_jogador, informacoes_navios)
    posicionar_navios_automatico(tabuleiro_computador, informacoes_navios)
    mensagem = "Novo jogo iniciado!"
    return redirect(url_for("index"))

# ==========================
# EXECUTAR FLASK
# ==========================

if __name__ == "__main__":
    app.run(debug=True)

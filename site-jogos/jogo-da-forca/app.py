from flask import Flask, render_template, request, redirect, url_for, session
import random

app = Flask(__name__)
app.secret_key = 'secreta'

class Palavra:
    def __init__(self, nome, tema):
        self.nome = nome.lower()
        self.tema = tema
        self.letras_descobertas = ['_' for _ in self.nome]
    
    def verificar_letra(self, letra_escolhida):
        acertou = False
        for i, letra in enumerate(self.nome):
            if letra == letra_escolhida:
                self.letras_descobertas[i] = letra
                acertou = True
        return acertou
    
    def palavra_completa(self):
        return ''.join(self.letras_descobertas)

    def terminou(self):
        return '_' not in self.letras_descobertas

palavras = [
    {"nome": "curupira", "tema": "Folclore Brasileiro"},
    {"nome": "uirapuru", "tema": "Folclore Brasileiro"},
    {"nome": "lasanha", "tema": "Comida"},
    {"nome": "bacalhau", "tema": "Comida"},
    {"nome": "cebolinha", "tema": "Personagem"},
    {"nome": "magali", "tema": "Personagem"},
    {"nome": "ornitorrinco", "tema": "Animal"},
    {"nome": "guepardo", "tema": "Animal"},
    {"nome": "espanha", "tema": "País"},
    {"nome": "alemanha", "tema": "País"}
]

def nova_palavra(jogadas):
    disponiveis = [p for p in palavras if p["nome"] not in jogadas]
    if disponiveis:
        escolha = random.choice(disponiveis)
        return Palavra(escolha["nome"], escolha["tema"])
    return None

@app.route('/', methods=['GET', 'POST'])
def index():
    # Inicializa sessão
    if 'palavra' not in session or 'tentativas_restantes' not in session:
        session['palavras_jogadas'] = []
        palavra_obj = nova_palavra(session['palavras_jogadas'])
        if palavra_obj is None:
            return render_template('fim.html')
        session['palavra'] = palavra_obj.nome
        session['tema'] = palavra_obj.tema
        session['letras_descobertas'] = palavra_obj.letras_descobertas
        session['tentativas_restantes'] = 6
        session['letras_erradas'] = []
        session['mensagem'] = ''
        session.modified = True

    palavra_obj = Palavra(session['palavra'], session['tema'])
    palavra_obj.letras_descobertas = session['letras_descobertas']
    tentativas_restantes = session['tentativas_restantes']
    letras_erradas = session['letras_erradas']
    mensagem = session.get('mensagem', '')

    if request.method == 'POST':
        letra = request.form.get('letra', '').lower().strip()

        if letra == '':
            session['mensagem'] = 'Digite uma letra!'
        elif len(letra) != 1 or not letra.isalpha():
            session['mensagem'] = 'Digite apenas uma única letra válida!'
        elif letra in palavra_obj.letras_descobertas or letra in letras_erradas:
            session['mensagem'] = 'Você já tentou essa letra!'
        else:
            if palavra_obj.verificar_letra(letra):
                session['mensagem'] = 'Esta letra está presente na palavra!'
            else:
                session['mensagem'] = 'Esta letra NÃO está presente na palavra!'
                letras_erradas.append(letra)
                tentativas_restantes -= 1

        # Atualiza a sessão
        session['letras_descobertas'] = palavra_obj.letras_descobertas
        session['tentativas_restantes'] = tentativas_restantes
        session['letras_erradas'] = letras_erradas
        session.modified = True

        # Verifica se terminou
    vitoria = False
    derrota = False

    if palavra_obj.terminou():
        session['mensagem'] = f"🎉 Parabéns! Você acertou a palavra: {palavra_obj.nome.upper()}."
        session['palavras_jogadas'].append(palavra_obj.nome)
        vitoria = True
        session.pop('palavra')
    elif tentativas_restantes <= 0:
        session['mensagem'] = f"☠️ Fim de jogo! A palavra era: {palavra_obj.nome.upper()}."
        session['palavras_jogadas'].append(palavra_obj.nome)
        derrota = True
        session.pop('palavra')

    return render_template('jogo-da-forca.html',
                        palavra_mascarada=' '.join(session['letras_descobertas']),
                        tema=session['tema'],
                        letras_erradas=letras_erradas,
                        tentativas_restantes=tentativas_restantes,
                        mensagem=mensagem,
                        vitoria=vitoria,
                        derrota=derrota)


@app.route('/reiniciar')
def reiniciar():
    session.clear()
    return redirect(url_for('index'))

@app.route('/fim')
def fim():
    return render_template('fim.html')

if __name__ == '__main__':
    app.run(debug=True)

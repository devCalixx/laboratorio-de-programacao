from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

class Pergunta:
    def __init__(self, pergunta, resposta, alternativas):
        self.pergunta = pergunta
        self.resposta = resposta
        self.alternativas = alternativas
    
    def embaralhar_alternativas(self):
        alternativas_embaralhadas = self.alternativas[:]
        random.shuffle(alternativas_embaralhadas)
        return alternativas_embaralhadas

# Lista de perguntas
perguntas = [
    Pergunta("Qual o nome da terra governada por Odisseu?", "Ítaca", ["Tróia", "Grécia", "Ítaca", "Roma"]),
    Pergunta("Quantos anos Odisseu ficou na Guerra de Tróia?", "10", ["10", "4", "7", "15"]),
    Pergunta("Quem abriu a bolsa de vento dada por Éolo?", "Euríloco", ["Polites", "Menelau", "Euríloco", "Odisseu"]),
    Pergunta("Qual deusa era mentora de Odisseu?", "Atena", ["Hera", "Atena", "Deméter", "Ártemis"]),
    Pergunta("Qual o desafio que Penélope propôs?", "Atirar em um alvo através de 12 machados.", [
        "Crochetar uma manta com fios de ouro.",
        "Lutar vendado com três guerreiros.",
        "Fazer um quadro realista.",
        "Atirar em um alvo através de 12 machados."
    ]),
    Pergunta("6- Qual o nome do monstro que devora exatamente seis homens de Odisseu?", "Scylla", ["Polifêmo", "Charybids", "Cérbero", "Scylla"]),
    Pergunta("7- Qual o maior inimigo de Odisseu?", "Poseidon", ["Hermes", "Zeus", "Poseidon", "Ares"]),
    Pergunta("8- Em que criatura Circe transforma os homens de Odisseu quando os captura?", "Porcos", ["Porcos", "Galinhas", "Sapos", "Vacas"]),
    Pergunta("9- Onde está o profeta que Odisseu precisa encontrar para voltar para casa?", "Submundo", ["Ítaca", "Olimpo", "Tróia", "Submundo"]),
    Pergunta("10- Qual o desafio que Penélope propõe à Odisseu para provar que ele ainda é seu marido?", "Ela diz para ele mover a cama dos dois, que foi entalhada na árvore em que eles se conheceram.", ["Ela pede para Odisseu esticar seu arco, que só ele consegue esticar.", "Ela traz amigos de Odisseu para reconhecê-lo e fazer perguntas sobre sua vida.", "Ela diz para ele mover a cama dos dois, que foi entalhada na árvore em que eles se conheceram.", "Ela não propõe nenhum desafio."])
]

@app.route("/")
def index():
    return render_template("quiz.html", pergunta_atual=perguntas[0])

@app.route("/pergunta/<int:num>")
def get_pergunta(num):
    if num < len(perguntas):
        pergunta = perguntas[num]
        alternativas = pergunta.embaralhar_alternativas()
        return jsonify({
            "texto": pergunta.pergunta,
            "alternativas": alternativas
        })
    else:
        return jsonify({"fim": True})

@app.route("/verificar", methods=["POST"])
def verificar():
    data = request.json
    num = data.get("num")
    resposta = data.get("resposta")
    correta = perguntas[num].resposta
    acerto = resposta == correta
    return jsonify({
        "correta": correta,
        "acertou": acerto
    })

if __name__ == "__main__":
    app.run(debug=True)

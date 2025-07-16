from flask import Flask, render_template, request, jsonify, session
import random

app = Flask(__name__)
app.secret_key = 'segredo'

pontuacao = {
    'jogador': 0,
    'computador': 0
}

opcoes = ['pedra', 'papel', 'tesoura']

@app.route('/')
def index():
    if "pontuacao_jogador" not in session:
        session['pontuacao_jogador'] = 0
        session['pontuacao_computador'] = 0
    return render_template('jokenpo.html')

@app.route('/jogar', methods=['POST'])
def jogar():
    dados = request.get_json()
    escolha_jogador = dados.get('escolha')
    computador = random.choice(opcoes)

    pontuacao_jogador = session.get('pontuacao_jogador', 0)
    pontuacao_computador = session.get('pontuacao_computador', 0)

    if escolha_jogador == computador:
        resultado = 'Empate! Ambos escolheram {}.'.format(escolha_jogador)
    elif(
        (escolha_jogador == "tesoura" and computador == "papel") or
        (escolha_jogador == "papel" and computador == "pedra") or
        (escolha_jogador == "pedra" and computador == "tesoura")
    ):
        pontuacao_jogador += 1
        resultado = 'Você venceu! {} vence de {}.'.format(escolha_jogador, computador)
    else:
        pontuacao_computador += 1
        resultado = 'Computador venceu! {} perde para {}.'.format(escolha_jogador, computador)

    session['pontuacao_jogador'] = pontuacao_jogador
    session['pontuacao_computador'] = pontuacao_computador

    return jsonify({
        'resultado': resultado,
        'escolha_jogador': escolha_jogador,
        'escolha_computador': computador,
        'pontuacao_jogador': pontuacao_jogador,
        'pontuacao_computador': pontuacao_computador
    })

@app.route('/resetar', methods=['POST'])
def resetar():
    session['pontuacao_jogador'] = 0
    session['pontuacao_computador'] = 0
    return jsonify({'mensagem': 'Pontuação resetada com sucesso!'})

if __name__ == '__main__':
    app.run(debug=True)
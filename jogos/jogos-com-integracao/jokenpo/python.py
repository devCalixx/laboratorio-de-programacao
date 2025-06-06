from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)

pontuacao_jogador = 0
pontuacao_computador = 0


opcoes = ["pedra", "papel", "tesoura"]
escolha_computador = random.choice(opcoes)

@app.route('/jokenpo', methods=['GET', 'POST'])

def index():
    global pontuacao_computador, pontuacao_jogador
    resultado = None
    escolha_jogador = None
    escolha_computador = None
    
    if request.method == 'POST':
        escolha_jogador = request.form.get('escolha')
        if escolha_jogador not in opcoes:
            resultado = "Escolha inválida, por favor, selecione pedra, papel ou tesoura"
        else:
            escolha_computador = random.choice(opcoes)

            if escolha_jogador == escolha_computador:
                resultado = "Empate! Ambos escolheram {escolha_jogador}."
            elif (escolha_jogador == "tesoura" and escolha_computador == "papel") or \
                (escolha_jogador == "papel" and escolha_computador == "pedra") or \
                (escolha_jogador == "pedra" and escolha_computador == "tesoura"):
                pontuacao_jogador += 1
                resultado = "Você venceu! {escolha_jogador.capitalize()} vence {escolha_computador.capitalize()}"
            else:
                pontuacao_computador += 1
                resultado = "Computador venceu! {escolha_computador.capitalize()} vence {escolha_jogador.capitalize()}"
                
    return render_template('jokenpo.html',
                           resultado = resultado,
                           pontuacao_jogador = pontuacao_jogador,
                           pontuacao_computador = pontuacao_computador,
                           escolha_jogador = escolha_jogador,
                           escolha_computador = escolha_computador)

if __name__ == '__main__':
    app.run(debug=True)

    
    '''if pontuacao_jogador == partidas:
            print(f"------------------\nParabéns, jogador! Você venceu com {pontuacao_jogador} e seu oponente perdeu com {pontuacao_computador}")
        elif pontuacao_computador == partidas:
            print(f"------------------\nQue droga! Você perdeu com {pontuacao_jogador} e seu oponente venceu com {pontuacao_computador}")
        novamente = input("------------------\nQuer jogar de novo? SIM ou NÃO? ")
        if novamente != "sim":
            print("Até a próxima!") 
            break
        else:
            pontuacao_computador = 0
            pontuacao_jogador = 0

    elif tipo_jogo == 2:
        while True:
            escolha = input("------------------\nFaça sua escolha. Pedra, papel ou tesoura? ").lower()
            if escolha not in opcoes:
                print("Escolha inválida. Tente novamente.")
                continue

            computador = random.choice(opcoes)

            print(f"------------------\nVocê escolheu {escolha}.")
            print(f"Seu oponente escolheu {computador}.")

            if escolha == computador:
                print(f"------------------\nEmpate! Ambos escolheram {escolha}.")
            elif (escolha == "tesoura" and computador == "papel") or (escolha == "papel" and computador == "pedra") or (escolha == "pedra" and computador == "tesoura"):
                print(f"------------------\nVocê venceu, já que escolheu {escolha} e seu oponente escolheu {computador}.")
            else:
                print(f"------------------\nSeu oponente venceu, já que ele escolheu {computador} e você escolheu {escolha}.")

            novamente = input("------------------\nQuer jogar de novo? SIM ou NÃO? ")
            if novamente != "sim":
                print("Até a próxima!") 
                break
            else:
                pontuacao_computador = 0
                pontuacao_jogador = 0'''
from flask import Flask, render_template, request, redirect, url_for
import random
app = Flask(__name__)
# Variáveis globais para armazenar o número e tentativas
acerto = random.randint(1, 100)
tentativas = 0
@app.route('/adivinhe-o-numero', methods=['GET', 'POST'])
def index():
    global acerto, tentativas
    if request.method == 'POST':
        palpite = int(request.form['guess-input'])
        tentativas += 1
        if palpite == acerto:
            resultado = f"Parabéns, você acertou! O número era: {acerto}. Tentativas: {tentativas}."
            acerto = random.randint(1, 100)  # Reinicia o jogo
            tentativas = 0
        elif palpite < acerto:
            resultado = f"Quase lá! O número {palpite} é menor."
        else:
            resultado = f"Quase lá! O número {palpite} é maior."
        return render_template('adivinhe-o-numero.html', resultado=resultado)
    return render_template('adivinhe-o-numero.html')
if __name__ == '__main__':
    app.run(debug=True)

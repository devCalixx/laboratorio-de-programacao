from flask import Flask, render_template, request, session, jsonify
import random

app = Flask(__name__)
app.secret_key = 'segredo'

NUM_MIN = 1
NUM_MAX = 100

@app.route('/')
def index():
    if 'numero' not in session:
        session['numero'] = random.randint(NUM_MIN, NUM_MAX)
        session['tentativas'] = 0
    return render_template('adivinhe-o-numero.html')

@app.route('/chutar', methods=['POST'])
def chutar():
    palpite = request.json.get('palpite')
    if palpite is None:
        return jsonify({'erro': 'Palpite não informado'}), 400
    
    try:
        palpite = int(palpite)
    except ValueError:
        return jsonify({'erro': 'Palpite inválido'}), 400

    if palpite < NUM_MIN or palpite > NUM_MAX:
        return jsonify({'erro': f'Palpite deve estar entre {NUM_MIN} e {NUM_MAX}'}), 400

    session['tentativas'] = session.get('tentativas', 0) + 1
    numero = session.get('numero')

    if palpite == numero:
        msg = f"Parabéns, você acertou! O número era: {numero}. Número de tentativas: {session['tentativas']}"
        session.pop('numero')
        session.pop('tentativas')
        return jsonify({'resultado': 'acertou', 'mensagem': msg})
    elif palpite < numero:
        return jsonify({'resultado': 'menor', 'mensagem': f"O número {palpite} é menor que o número a ser adivinhado.", 'tentativas': session['tentativas']})
    else:
        return jsonify({'resultado': 'maior', 'mensagem': f"O número {palpite} é maior que o número a ser adivinhado.", 'tentativas': session['tentativas']})

if __name__ == '__main__':
    app.run(debug=True)
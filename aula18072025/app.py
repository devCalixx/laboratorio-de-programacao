from flask import Flask, render_template

app = Flask(__name__)

app.secret_key = 'segredo'

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

@app.route('/conteudo')
def conteudo():
    return render_template('conteudo.html')

@app.route('/servicos')
def servicos():
    return render_template('servicos.html')

@app.route('/contato')
def contato():
    return render_template('contato.html')

if __name__ == '__main__':
    app.run(debug = True)
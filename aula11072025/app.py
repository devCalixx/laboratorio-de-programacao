from flask import Flask, render_template, request, redirect, url_for, make_response, session
import json

app = Flask(__name__)

app.secret_key = 'secreto'
USUARIO_CADASTRADO = 'admin'
SENHA_CADASTRADA = '123'

@app.route('/', methods=['GET', 'POST'])
def login():
    mensagem = ""
    tema = request.cookies.get('tema', 'padrao')

    if request.method == "POST":
        usuario = request.form['username']
        senha = request.form['password']

        if usuario == USUARIO_CADASTRADO and senha == SENHA_CADASTRADA:
            session['username'] = usuario
            session['contador'] = session.get('contador', 0) + 1
            return redirect(url_for('bemvindo'))
        else:
            mensagem = "Usuário ou senha inválidos"

    return render_template('login.html', tema=tema, mensagem=mensagem)

@app.route('/bemvindo', methods=['GET', 'POST'])
def bemvindo():
   
    if 'username' not in session:
        return redirect(url_for('login'))
    
    username = session['username']
    contador = session.get('contador', 0)

    tema = request.cookies.get('tema', 'padrao')

    if request.method == "POST":
        tema = request.form.get('tema', 'padrao')
        response = make_response(render_template('bemvindo.html', username=username, tema=tema, contador=contador))
        response.set_cookie("tema", tema, max_age=1800)
        return response
   
    return render_template('bemvindo.html', username=username, tema=tema, contador=contador)    

@app.route('/noticias', methods=['GET', 'POST'])
def noticias():
    if 'username' not in session:
        return redirect(url_for('login'))
    
    username=session['username']
    contador = session.get('contador', 0)

    tema = request.cookies.get('tema', 'padrao')

@app.route('/mudartema', methods=['POST'])
def mudar_tema():
    tema = request.form.get('tema')
    response = make_response(redirect(url_for('bemvindo')))
    response.set_cookie('tema', tema, max_age=1800)
    return response

@app.route('/logout')
def logout():
    session.clear()
    response = make_response(redirect(url_for('login')))
    response.set_cookie('tema', '', expires=0) 
    return response

if __name__ == '__main__':
    app.run(debug = True)

#diferença entre sessão e cookie: a sessão, quando você sai do site, você perde aquelas informações. já o cookie, mesmo quando você sai, ela continua gravada.
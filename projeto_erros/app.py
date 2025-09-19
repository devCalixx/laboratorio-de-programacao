from flask import Flask, render_template, abort, request, flash, redirect, url_for

app = Flask(__name__)

# SECRET KEY NECESSÁRIA PARA USAR FLASH MESSAGES

app.config['SECRET_KEY'] = "chave-secreta-segura"

# ROTA PRINCIPAL

@app.route("/")

def index():
    return render_template("index.html")

# ROTA PARA O FORMULÁRIO

@app.route("/formulario", methods=['GET', 'POST'])
def formulario():
    if request.method == 'POST':
        # EM UMA APLICAÇÃO REAL, AQUI OCORRERIA A VALIDAÇÃO DO BACK-END
        nome = request.form.get('nome')
        email = request.form.get('email')
        print(f'Dados recebidos do formulário: Nome = {nome}, Email = {email}')
        # SIMULA UMA MENSAGEM DE SUCESSO
        flash(f"Obrigado por se cadastrar, {nome}!", "sucess")
        return redirect(url_for('formulario'))
    return render_template('formulario.html')

# PARA DEMONSTRAR O ERRO 401, VAMOS CRIAR UMA ROTA QUE EXIGE UM LOGIN (SIMULADO)

@app.route("/area-restrita")
def area_restrita():
    # EM UMA APLICAÇÃO REAL, AQUI VOCÊ VERIFICARIA SE O USUÁRIO ESTÁ LOGADO
    # COMO NÃO TEMOS UM SISTEMA DE LOGIN, VAMOS FORÇAR O ERRO 401 COM O ABORT()
    print("Tentativa de acesso à area restrita sem autenticação.")
    abort(401)

# PARA DEMONSTRAR O ERRO 403, UMA ROTA DE ADMIN (SIMULADO)

@app.route("/painel-admin")
def painel_admin():
    # AQUI, VERIFICARIA SE O USUÁRIO LOGADO É UM ADMINISTRADOR
    # VAMOS SIMULAR QUE O USUÁRIO NÃO É ADMIN E FORÇAR O ERRO 403
    print("Tentativa de acesso ao painel de admin sem permissão")
    abort(403)

# MANIPULADORES DE ERRO (ERROR HANDLERS)

@app.errorhandler(404)
def pagina_nao_encontrada(error):
    # A FUNÇÃO RECEBE O OBJETO DE ERRO COMO ARGUMENTO
    # RETORNAMOS A RENDERIZAÇÃO DO NOSSO TEMPLATE E O CÓDIGO DE STATUS 404
    return render_template("404.html"), 404

@app.errorhandler(401)
def nao_autorizado(error):
    return render_template("401.html"), 401

@app.errorhandler(403)
def acesso_proibido(error):
    return render_template("403.html"), 403

if __name__ == '__main__':
    app.run(debug=True)
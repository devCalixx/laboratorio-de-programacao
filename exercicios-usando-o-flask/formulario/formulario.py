from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'your_secret_key_here' 

@app.route("/", methods=["GET"])
def form():
    return render_template("index.html")

@app.route("/confirmacao", methods=["POST"])  # This should match the action in the form
def confirm():
    nome = request.form.get("nome", "").strip()
    email = request.form.get("email", "").strip()
    datanascimento = request.form.get("datanascimento", "").strip()  # Change to "datanascimento"
    session['form_data'] = {"nome": nome, "email": email, "datanascimento": datanascimento}
    return render_template("confirma.html", nome=nome, email=email, datanascimento=datanascimento)  # Change "data-nascimento" to "datanascimento"

@app.route("/final", methods=["POST"])  # This should match the action in the confirmation form
def finalize():
    confirmacao = request.form.get("confirmacao")
    if confirmacao == "yes":
        session.pop('form_data', None)
        return render_template("final.html")
    else:
        return redirect(url_for("form"))
    
if __name__ == "__main__":
    app.run(debug=True)
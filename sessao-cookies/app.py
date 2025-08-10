from flask import Flask, render_template, request, redirect, url_for, make_response, session, jsonify

app = Flask(__name__)

app.secret_key = 'secreto'
USUARIO_CADASTRADO = 'admin'
SENHA_CADASTRADA = '123'

NOTICIAS = [
        {
            "id": 1,
            "assunto": "politica",
            "classe": "noticia-politica",
            "titulo": "Show interrompido pela Prefeitura de SP, polêmica no Lolla e nome diferentão: conheça a banda Sophia Chablau e Uma Enorme Perda de Tempo",
            "resumo": "Banda teve show interrompido na noite de sexta-feira (11) pela Prefeitura de São Paulo. Segundo a gestão, o telão e o som foram reduzidos 'após falas e projeções que feriram cláusulas contratuais, com ofensas direcionadas a terceiros'. O caso gerou grande repercussão nas redes sociais, com fãs e artistas se manifestando contra o que chamaram de censura artística. A banda, conhecida por suas letras provocativas e humor ácido, afirmou que vai recorrer da decisão e já planeja novos shows na capital.",
            "imagem": "sophia-chablau.avif"
        },
        {
            "id": 2,
            "assunto": "entretenimento",
            "classe": "noticia-entretenimento",
            "titulo": "Emmy Awards 2025: Ayo Edebiri se torna 1ª mulher negra indicada como diretora e atriz no mesmo ano",
            "resumo": "Ayo Edebiri, estrela de ‘O Urso’, fez história ao se tornar a primeira mulher negra indicada simultaneamente para as categorias de melhor atriz e melhor direção no Emmy Awards. A artista agradeceu em suas redes sociais e reforçou a importância de mais diversidade na indústria audiovisual. Sua atuação e visão criativa foram elogiadas pela crítica, que aponta a série como uma das favoritas para levar os principais prêmios deste ano.",
            "imagem": "ayo.jpg"
        },
        {
            "id": 3,
            "assunto": "ciencia",
            "classe": "noticia-ciencia",
            "titulo": "Pela 1ª vez, cientistas flagram nascimento de sistema planetário fora do Sistema Solar; veja IMAGEM",
            "resumo": "Astrônomos anunciaram uma descoberta histórica: o flagrante do nascimento de um sistema planetário fora do Sistema Solar. O fenômeno foi registrado através de imagens de alta resolução capturadas pelo telescópio ALMA.  Os explicam que o processo observado é muito semelhante ao que teria dado origem aos planetas que orbitam o Sol há bilhões de anos.",
            "imagem": "estrela.avif"
        },
        {
            "id": 4,
            "assunto": "esportes",
            "classe": "noticia-esportes",
            "titulo": "Mundial de Clubes: veja quantas vagas o Brasil pode ter em 2029",
            "resumo": "Com a expansão do Mundial de Clubes para 32 times em 2029, o Brasil pode garantir até 3 vagas na competição dependendo do desempenho dos clubes nas próximas Libertadores. A CBF também manifestou interesse em sediar o evento, alegando ter a infraestrutura necessária para receber as principais equipes do mundo.",
            "imagem": "copa.webp"
        },
        {
            "id": 5,
            "assunto": "entretenimento",
            "classe": "noticia-entretenimento",
            "titulo": "Apresentado por Ana Maria Braga, 'Chef de Alto Nível' estreia e divide opiniões",
            "resumo": "A estreia do reality 'Chef de Alto Nível' dividiu opiniões do público e críticos. Ana Maria Braga assumiu a apresentação do programa, que promete revelar novos talentos da gastronomia brasileira. Enquanto alguns espectadores elogiaram o carisma da apresentadora e o formato inovador, outros compararam a produção com realities culinários já consolidados.",
            "imagem": "masterchef.webp"
        },
        {
            "id": 6,
            "assunto": "entretenimento",
            "classe": "noticia-entretenimento",
            "titulo": "Bilheteria de Superman registra o melhor desempenho para uma terça-feira em 2025",
            "resumo": "O novo filme do Superman superou expectativas de bilheteria em sua estreia, arrecadando cifras recordes para uma terça-feira em 2025. Críticos destacam que a produção consegue agradar tanto aos fãs clássicos do herói quanto ao público mais jovem, graças a um roteiro equilibrado e efeitos visuais impressionantes.",
            "imagem": "superman.jpg"
        },
        {
            "id": 7,
            "assunto": "esportes",
            "classe": "noticia-esportes",
            "titulo": "Conmebol promove mudança no VAR em Libertadores e Sul-Americana; entenda",
            "resumo": "A Conmebol anunciou novas diretrizes para o uso do VAR nas competições continentais. Entre as medidas está a publicação em tempo real dos áudios entre árbitro de campo e árbitros de vídeo, como forma de garantir mais transparência e reduzir as críticas sobre imparcialidade nas decisões tomadas durante os jogos.",
            "imagem": "var.webp"
        },
        {
            "id": 8,
            "assunto": "ciencia",
            "classe": "noticia-ciencia",
            "titulo": "Asteroides “invisíveis” próximos de Vênus podem ameaçar a Terra no futuro",
            "resumo": "Pesquisadores alertam para asteroides localizados próximos à órbita de Vênus que são difíceis de detectar com os atuais sistemas de monitoramento. As simulações mostram que esses corpos celestes podem, no futuro, representar risco para a Terra caso suas órbitas sejam alteradas por forças gravitacionais.",
            "imagem": "venus.webp"
        },
        {
            "id": 9,
            "assunto": "esportes",
            "classe": "noticia-esportes",
            "titulo": "Brasil vence Argentina e se aproxima da classificação na Liga das Nações de Vôlei (VNL) masculino 2025",
            "resumo": "A seleção masculina de vôlei do Brasil derrotou a Argentina por 3 sets a 1 na última rodada da fase classificatória da VNL 2025. Com o resultado, o time brasileiro fica mais próximo de garantir vaga nas finais da competição, que acontecerão em Paris no próximo mês.",
            "imagem": "volei.jpg"
        },
        {
            "id": 10,
            "assunto": "ciencia",
            "classe": "noticia-ciencia",
            "titulo": "Xbox vai substituir 200 funcionários da King por ferramentas IA",
            "resumo": "A Microsoft anunciou a substituição de 200 funcionários da King, responsável pelo jogo Candy Crush, por sistemas baseados em inteligência artificial. A medida visa reduzir custos e aumentar a eficiência operacional, mas sindicatos criticam a decisão alegando impacto negativo sobre os trabalhadores.",
            "imagem": "microsoft.jpg"
        }
    ]


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

    return render_template('login.html', tema=tema, mensagem=mensagem, sem_header=True)

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
    assunto_cookie = request.cookies.get('ultimo_assunto')
    contador = session.get('contador', 0)
    recomendadas = []

    if assunto_cookie:
        recomendadas = [n for n in NOTICIAS if n['assunto'] == assunto_cookie]

    tema = request.cookies.get('tema', 'padrao')

    if request.method == "POST":
        tema = request.form.get('tema', 'padrao')
        response = make_response(render_template('noticias.html', username=username, tema=tema, contador=contador))
        response.set_cookie("tema", tema, max_age=1800)
        return response
   
    return render_template('noticias.html', username=username, tema=tema, contador=contador, noticias=NOTICIAS, recomendadas=recomendadas, assunto_cookie=assunto_cookie) 

@app.route('/noticia/<int:noticia_id>')
def noticia(noticia_id):
    if 'username' not in session:
        return redirect(url_for('login'))

    noticia = next((n for n in NOTICIAS if n['id'] == noticia_id), None)
    if not noticia:
        return jsonify({'erro': 'Notícia não encontrada'}), 404

    recomendadas = [n for n in NOTICIAS if n['assunto'] == noticia['assunto'] and n['id'] != noticia_id]

    response = make_response(render_template('noticias.html', noticia=noticia, recomendadas=recomendadas))
    response.set_cookie('ultimo_assunto', noticia['assunto'], max_age=3600)
    return jsonify(noticia)

@app.route('/mudartema', methods=['POST'])
def mudar_tema():
    tema = request.form.get('tema', 'padrao')
    response = make_response(redirect(url_for('bemvindo')))
    response.set_cookie('tema', tema, max_age=1800)
    return response

@app.route('/logout')
def logout():
    session.clear()
    response = make_response(redirect(url_for('login')))
    response.set_cookie('tema', '', expires=0) 
    response.set_cookie('ultimo_assunto', '', expires=0)
    return response

if __name__ == '__main__':
    app.run(debug = True)

#diferença entre sessão e cookie: a sessão, quando você sai do site, você perde aquelas informações. já o cookie, mesmo quando você sai, ela continua gravada.
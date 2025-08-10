function abrirModal(id) {
    fetch('/noticia/' + id)
        .then(response => response.json())
        .then(data => {
            if (data.erro) {
                alert('Notícia não encontrada!');
                return;
            }
            document.getElementById('modal-titulo').innerText = data.titulo;
            document.getElementById('modal-resumo').innerText = data.resumo;
            document.getElementById('modal-imagem').src = '/static/img/' + data.imagem;
            document.getElementById('modal').style.display = "block";
        })
        .catch(err => console.error(err));
}

function fecharModal() {
    document.getElementById('modal').style.display = "none";
}


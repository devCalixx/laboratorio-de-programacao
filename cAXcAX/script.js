let trocou = false
const imagem = document.getElementById('yoshi');

imagem.addEventListener('click', function () {
    imagem.src = 'yoshi-bailando-pixel.gif';
    if (trocou) {
        imagem.src = 'grandao.gif'
        trocou = false
    } else {
        imagem.src="yoshi-bailando-pixel.gif"
        trocou = true
    }
});

const topico = document.getElementById('topico')

const elementoGatilho = document.getElementById('topico');
const tela = document.getElementById('tela-para-abrir');

elementoGatilho.addEventListener('mouseover', () => {
    tela.classList.remove('escondida'); // Remove a classe escondida
    tela.classList.add('visivel');     // Adiciona a classe visivel
});

elementoGatilho.addEventListener('mouseout', () => {
    tela.classList.remove('visivel');  // Remove a classe visivel
    tela.classList.add('escondida');   // Adiciona a classe escondida
});
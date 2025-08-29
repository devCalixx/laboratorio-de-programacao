let trocou = false
const imagem = document.getElementById('yoshi');

imagem.addEventListener('click', function () {
    imagem.src = 'static/yoshi-bailando-pixel.gif';
    if (trocou) {
        imagem.src = 'static/grandao.gif'
        trocou = false
    } else {
        imagem.src="static/yoshi-bailando-pixel.gif"
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

const topico2 = document.getElementById('topico2')

const elementoGatilho2 = document.getElementById('topico2');
const tela2 = document.getElementById('tela-para-abrir2');

elementoGatilho2.addEventListener('mouseover', () => {
    tela2.classList.remove('escondida'); // Remove a classe escondida
    tela2.classList.add('visivel');     // Adiciona a classe visivel
});

elementoGatilho2.addEventListener('mouseout', () => {
    tela2.classList.remove('visivel');  // Remove a classe visivel
    tela2.classList.add('escondida');   // Adiciona a classe escondida
});

const topico3 = document.getElementById('topico3')

const elementoGatilho3 = document.getElementById('topico3');
const tela3 = document.getElementById('tela-para-abrir3');

elementoGatilho3.addEventListener('mouseover', () => {
    tela3.classList.remove('escondida'); // Remove a classe escondida
    tela3.classList.add('visivel');     // Adiciona a classe visivel
});

elementoGatilho3.addEventListener('mouseout', () => {
    tela3.classList.remove('visivel');  // Remove a classe visivel
    tela3.classList.add('escondida');   // Adiciona a classe escondida
});
/*const readyModal = document.getElementById('ready-modal');
    const mainContent = document.getElementById('main-content');
    const startBtn = document.getElementById('start-btn');
    const notNowBtn = document.getElementById('not-now-btn');
    const modalElement = readyModal.querySelector('.modal');

    function trapFocus(element) {
      const focusable = element.querySelectorAll('button, [href], input, select, textarea, [tabindex]:not([tabindex="-1"])');
      if (!focusable.length) return;
      const firstFocusable = focusable[0];
      const lastFocusable = focusable[focusable.length - 1];
      element.addEventListener('keydown', (e) => {
        if (e.key === 'Tab') {
          if (e.shiftKey) { // shift + tab
            if (document.activeElement === firstFocusable) {
              e.preventDefault();
              lastFocusable.focus();
            }
          } else {
            if (document.activeElement === lastFocusable) {
              e.preventDefault();
              firstFocusable.focus();
            }
          }
        }
        if (e.key === 'Escape') {
          e.preventDefault(); 
        }
      });
    }
    trapFocus(modalElement);

    mainContent.classList.add('blurred');
    startBtn.focus();

    startBtn.addEventListener('click', () => {
      readyModal.style.display = 'none';
      mainContent.classList.remove('blurred');
      mainContent.focus();
    });

    notNowBtn.addEventListener('click', () => {
      startBtn.focus();
    });*/

    let pontuacao = 0;
let perguntaAtual = 0;

document.getElementById('start-btn').addEventListener('click', () => {
    document.getElementById('ready-modal').style.display = 'none';
    carregarPergunta();
});

function carregarPergunta() {
    fetch(`/pergunta/${perguntaAtual}`)
        .then(response => response.json())
        .then(data => {
            if (data.fim) {
                alert(`🎉 Fim do quiz! Sua pontuação final foi ${pontuacao}.`);
                return;
            }
            document.getElementById('question-text').textContent = data.texto;
            const choices = document.querySelector('.choices');
            choices.innerHTML = '';
            data.alternativas.forEach(alternativa => {
                const btn = document.createElement('button');
                btn.className = 'choice-button';
                btn.textContent = alternativa;
                btn.onclick = () => responder(btn);
                choices.appendChild(btn);
            });
            document.getElementById('pergunta-atual').textContent = perguntaAtual + 1;
        });
}

function responder(button) {
    const resposta = button.textContent;
    fetch('/verificar', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ num: perguntaAtual, resposta })
    })
    .then(response => response.json())
    .then(data => {
        if (data.acertou) {
            pontuacao++;
            alert('✅ Certa resposta!');
        } else {
            alert(`❌ Errado! Resposta correta: ${data.correta}`);
        }
        document.getElementById('pontuacao').textContent = pontuacao;
        perguntaAtual++;
        carregarPergunta();
    });
}

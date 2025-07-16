const input = document.getElementById('guess-input');
const button = document.querySelector('.btn-submit');
const resultadoMsg = document.getElementById('resultado-msg');

input.addEventListener('input', () => {
  const val = input.value;
  if(val !== '' && !isNaN(val) && Number(val) >= 1 && Number(val) <= 100) {
    button.disabled = false;
  } else {
    button.disabled = true;
  }
});

document.getElementById('guess-form').addEventListener('submit', async (e) => {
  e.preventDefault();
  button.disabled = true;
  resultadoMsg.textContent = 'Processando...';

  const palpite = Number(input.value);

  try {
    const response = await fetch('/chutar', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ palpite })
    });

    const data = await response.json();

    if (!response.ok) {
      resultadoMsg.textContent = data.erro || 'Erro inesperado.';
      button.disabled = false;
      return;
    }

    resultadoMsg.textContent = data.mensagem;

    if (data.resultado === 'acertou') {
      button.disabled = true;
      input.value = '';
      input.disabled = true;
      // Perguntar se quer jogar de novo
      if (confirm("Você acertou! Quer jogar novamente?")) {
        // Recarregar a página para resetar o jogo
        window.location.reload();
      }
    } else {
      button.disabled = false;
      input.value = '';
      input.focus();
    }
  } catch (error) {
    resultadoMsg.textContent = 'Erro na comunicação com o servidor.';
    button.disabled = false;
  }
});
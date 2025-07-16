document.addEventListener("DOMContentLoaded", () => {
  const buttons = document.querySelectorAll(".choice");
  const resultScreen = document.getElementById("result-screen");
  const scoreJogador = document.getElementById("score-jogador");
  const scoreComputador = document.getElementById("score-computador");
  const resetButton = document.getElementById("reset-button");

  const startModal = document.getElementById("start-modal");
  const modoIlimitadoBtn = document.getElementById("modo-ilimitado");
  const modoDefinidoBtn = document.getElementById("modo-definido");
  const numPartidasInput = document.getElementById("num-partidas");

  let totalRodadas = Infinity;
  let rodadasJogadas = 0;

  // Função para iniciar o jogo com configuração
  function iniciarJogo(rodadas) {
    totalRodadas = rodadas;
    rodadasJogadas = 0;
    startModal.style.display = "none";
  }

  modoIlimitadoBtn.addEventListener("click", () => iniciarJogo(Infinity));

  modoDefinidoBtn.addEventListener("click", () => {
    const num = parseInt(numPartidasInput.value, 10);
    if (num && num > 0) {
      iniciarJogo(num);
    } else {
      alert("Digite um número válido de rodadas!");
    }
  });

  buttons.forEach(button => {
    button.addEventListener("click", () => {
      if (rodadasJogadas >= totalRodadas) return; // Evita jogar depois do fim

      const escolha = button.dataset.move;
      fetch("/jogar", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ escolha: escolha })
      })
      .then(response => response.json())
      .then(data => {
        resultScreen.style.display = "block";
        resultScreen.innerHTML = `
          Você escolheu <b>${data.escolha_jogador}</b>.<br>
          O computador escolheu <b>${data.escolha_computador}</b>.<br>
          <strong>${data.resultado}</strong>
        `;
        scoreJogador.textContent = data.pontuacao_jogador;
        scoreComputador.textContent = data.pontuacao_computador;

        rodadasJogadas++;
        if (rodadasJogadas >= totalRodadas) {
          mostrarVencedorFinal();
        }
      });
    });
  });

  function mostrarVencedorFinal() {
    let vencedor;
    const pj = parseInt(scoreJogador.textContent, 10);
    const pc = parseInt(scoreComputador.textContent, 10);
    if (pj > pc) {
      vencedor = "🎉 Você venceu o jogo!";
    } else if (pc > pj) {
      vencedor = "😢 O computador venceu o jogo!";
    } else {
      vencedor = "🤝 Empate!";
    }
    setTimeout(() => {
      alert(vencedor);
    }, 500);
  }

  resetButton.addEventListener("click", () => {
    fetch("/resetar", { method: "POST" })
      .then(response => response.json())
      .then(data => {
        resultScreen.innerHTML = "<strong>" + data.mensagem + "</strong>";
        resultScreen.style.display = "block";
        scoreJogador.textContent = "0";
        scoreComputador.textContent = "0";
        startModal.style.display = "flex"; // Reabre configuração
      });
  });
});

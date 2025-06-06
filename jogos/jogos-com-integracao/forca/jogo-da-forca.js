const letterInput = document.getElementById('letter-input');
const submitBtn = document.getElementById('submit-letter');

letterInput.addEventListener('input', () => {
  const val = letterInput.value.trim();
  submitBtn.disabled = !(val.length === 1 && /^[A-Za-zÀ-Ÿ]$/.test(val));
  letterInput.value = val.toUpperCase();
});

submitBtn.addEventListener('click', () => {
  letterInput.value = '';
  submitBtn.disabled = true;
  letterInput.focus();
});

letterInput.focus();
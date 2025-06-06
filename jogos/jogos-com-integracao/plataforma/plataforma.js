(function() {
  const track = document.querySelector('.carousel-track');
  const slides = Array.from(track.children);
  const prevButton = document.querySelector('.carousel-button.prev');
  const nextButton = document.querySelector('.carousel-button.next');
  const indicators = document.querySelectorAll('.indicator-dot');
  let currentIndex = 0;
  const slideCount = slides.length;

  function updateCarousel(index) {
    if (index < 0) index = slideCount - 1;
    if (index >= slideCount) index = 0;
    track.style.transform = `translateX(-${index * 100}%)`;
    currentIndex = index;
    updateIndicators();
  }

  function updateIndicators() {
    indicators.forEach((dot, idx) => {
      if (idx === currentIndex) {
        dot.classList.add('active');
        dot.setAttribute('aria-selected', 'true');
        dot.focus();
      } else {
        dot.classList.remove('active');
        dot.setAttribute('aria-selected', 'false');
      }
    });
  }

  prevButton.addEventListener('click', () => {
    updateCarousel(currentIndex - 1);
  });

  nextButton.addEventListener('click', () => {
    updateCarousel(currentIndex + 1);
  });

  indicators.forEach(dot => {
    dot.addEventListener('click', (e) => {
      const index = parseInt(e.target.getAttribute('data-slide-to'));
      updateCarousel(index);
    });
  });

  let autoplayInterval = setInterval(() => {
    updateCarousel(currentIndex + 1);
  }, 5000);

  document.querySelector('.carousel').addEventListener('mouseenter', () => {
    clearInterval(autoplayInterval);
  });

  document.querySelector('.carousel').addEventListener('mouseleave', () => {
    autoplayInterval = setInterval(() => {
      updateCarousel(currentIndex + 1);
    }, 5000);
  });

  updateCarousel(0);
})();

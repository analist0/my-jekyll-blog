/**
 * 🎨 Modern Blog Animations - 2025 Edition
 * Advanced JavaScript animations for ultra-professional blog experience
 */

// ========================================
// 1. SCROLL-TRIGGERED ANIMATIONS
// ========================================

// Intersection Observer for scroll animations
const observerOptions = {
  threshold: 0.1,
  rootMargin: '0px 0px -100px 0px'
};

const animateOnScroll = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('animated');
      // Optional: unobserve after animation
      // animateOnScroll.unobserve(entry.target);
    }
  });
}, observerOptions);

// Animate all articles, widgets, and posts
document.addEventListener('DOMContentLoaded', () => {
  const animatedElements = document.querySelectorAll('article, .widget, .post-title, .post-content p, .post-content img');
  animatedElements.forEach(el => {
    el.classList.add('animate-on-scroll');
    animateOnScroll.observe(el);
  });
});

// ========================================
// 2. CUSTOM CURSOR WITH TRAIL
// ========================================

let cursor = null;
let cursorDot = null;
let mouseX = 0, mouseY = 0;
let cursorX = 0, cursorY = 0;
let dotX = 0, dotY = 0;

function initCustomCursor() {
  // Create cursor elements
  cursor = document.createElement('div');
  cursor.className = 'custom-cursor';

  cursorDot = document.createElement('div');
  cursorDot.className = 'custom-cursor-dot';

  document.body.appendChild(cursor);
  document.body.appendChild(cursorDot);

  // Track mouse movement
  document.addEventListener('mousemove', (e) => {
    mouseX = e.clientX;
    mouseY = e.clientY;
  });

  // Smooth cursor animation
  function animateCursor() {
    // Smooth follow with easing
    cursorX += (mouseX - cursorX) * 0.15;
    cursorY += (mouseY - cursorY) * 0.15;

    dotX += (mouseX - dotX) * 0.3;
    dotY += (mouseY - dotY) * 0.3;

    cursor.style.left = cursorX + 'px';
    cursor.style.top = cursorY + 'px';

    cursorDot.style.left = dotX + 'px';
    cursorDot.style.top = dotY + 'px';

    requestAnimationFrame(animateCursor);
  }

  animateCursor();

  // Cursor interactions
  const interactiveElements = document.querySelectorAll('a, button, .button, .social-icon, .nav a');

  interactiveElements.forEach(el => {
    el.addEventListener('mouseenter', () => {
      cursor.classList.add('cursor-hover');
      cursorDot.classList.add('cursor-hover');
    });

    el.addEventListener('mouseleave', () => {
      cursor.classList.remove('cursor-hover');
      cursorDot.classList.remove('cursor-hover');
    });
  });
}

// ========================================
// 3. PARTICLE BACKGROUND
// ========================================

function createParticleBackground() {
  const canvas = document.createElement('canvas');
  canvas.id = 'particle-canvas';
  canvas.style.position = 'fixed';
  canvas.style.top = '0';
  canvas.style.left = '0';
  canvas.style.width = '100%';
  canvas.style.height = '100%';
  canvas.style.pointerEvents = 'none';
  canvas.style.zIndex = '-1';
  canvas.style.opacity = '0.3';

  document.body.prepend(canvas);

  const ctx = canvas.getContext('2d');
  let particles = [];
  let particleCount = 50;

  // Resize canvas
  function resizeCanvas() {
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
  }

  resizeCanvas();
  window.addEventListener('resize', resizeCanvas);

  // Particle class
  class Particle {
    constructor() {
      this.x = Math.random() * canvas.width;
      this.y = Math.random() * canvas.height;
      this.size = Math.random() * 3 + 1;
      this.speedX = Math.random() * 0.5 - 0.25;
      this.speedY = Math.random() * 0.5 - 0.25;
      this.opacity = Math.random() * 0.5 + 0.2;
    }

    update() {
      this.x += this.speedX;
      this.y += this.speedY;

      // Wrap around edges
      if (this.x > canvas.width) this.x = 0;
      if (this.x < 0) this.x = canvas.width;
      if (this.y > canvas.height) this.y = 0;
      if (this.y < 0) this.y = canvas.height;
    }

    draw() {
      ctx.fillStyle = `rgba(59, 130, 246, ${this.opacity})`;
      ctx.beginPath();
      ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
      ctx.fill();
    }
  }

  // Create particles
  for (let i = 0; i < particleCount; i++) {
    particles.push(new Particle());
  }

  // Animation loop
  function animateParticles() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    particles.forEach(particle => {
      particle.update();
      particle.draw();
    });

    // Draw connections
    particles.forEach((p1, i) => {
      particles.slice(i + 1).forEach(p2 => {
        const dx = p1.x - p2.x;
        const dy = p1.y - p2.y;
        const distance = Math.sqrt(dx * dx + dy * dy);

        if (distance < 150) {
          ctx.strokeStyle = `rgba(59, 130, 246, ${0.2 * (1 - distance / 150)})`;
          ctx.lineWidth = 0.5;
          ctx.beginPath();
          ctx.moveTo(p1.x, p1.y);
          ctx.lineTo(p2.x, p2.y);
          ctx.stroke();
        }
      });
    });

    requestAnimationFrame(animateParticles);
  }

  animateParticles();
}

// ========================================
// 4. PARALLAX SCROLLING
// ========================================

function initParallax() {
  const header = document.querySelector('header');
  const nav = document.querySelector('.nav');

  window.addEventListener('scroll', () => {
    const scrolled = window.pageYOffset;

    // Header parallax
    if (header) {
      header.style.transform = `translateY(${scrolled * 0.5}px)`;
      header.style.opacity = 1 - (scrolled / 500);
    }

    // Nav sticky effect with blur
    if (nav) {
      if (scrolled > 100) {
        nav.classList.add('nav-scrolled');
      } else {
        nav.classList.remove('nav-scrolled');
      }
    }
  });
}

// ========================================
// 5. SMOOTH SCROLL
// ========================================

function initSmoothScroll() {
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
      const href = this.getAttribute('href');
      if (href !== '#') {
        e.preventDefault();
        const target = document.querySelector(href);
        if (target) {
          target.scrollIntoView({
            behavior: 'smooth',
            block: 'start'
          });
        }
      }
    });
  });
}

// ========================================
// 6. IMAGE LAZY LOADING WITH ANIMATION
// ========================================

function initLazyImages() {
  const imageObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const img = entry.target;
        img.src = img.dataset.src;
        img.classList.add('loaded');
        imageObserver.unobserve(img);
      }
    });
  });

  document.querySelectorAll('img[data-src]').forEach(img => {
    imageObserver.observe(img);
  });
}

// ========================================
// 7. READING PROGRESS BAR
// ========================================

function initReadingProgress() {
  const progressBar = document.createElement('div');
  progressBar.className = 'reading-progress';
  document.body.appendChild(progressBar);

  window.addEventListener('scroll', () => {
    const windowHeight = window.innerHeight;
    const documentHeight = document.documentElement.scrollHeight - windowHeight;
    const scrolled = (window.pageYOffset / documentHeight) * 100;

    progressBar.style.width = scrolled + '%';
  });
}

// ========================================
// 8. TYPEWRITER EFFECT FOR HEADERS
// ========================================

function typewriterEffect(element, text, speed = 50) {
  let i = 0;
  element.textContent = '';

  function type() {
    if (i < text.length) {
      element.textContent += text.charAt(i);
      i++;
      setTimeout(type, speed);
    }
  }

  type();
}

// ========================================
// 9. FLOATING ELEMENTS
// ========================================

function initFloatingElements() {
  const floatingElements = document.querySelectorAll('.widget');

  floatingElements.forEach((el, index) => {
    // Random floating animation
    const duration = 3 + Math.random() * 2;
    const delay = index * 0.2;

    el.style.animation = `float ${duration}s ease-in-out ${delay}s infinite`;
  });
}

// ========================================
// 10. GRADIENT ANIMATION ON SCROLL
// ========================================

function initGradientScroll() {
  const body = document.body;

  window.addEventListener('scroll', () => {
    const scrollPercent = (window.pageYOffset / (document.documentElement.scrollHeight - window.innerHeight)) * 100;

    // Change gradient based on scroll position
    const hue1 = 210 + (scrollPercent * 0.5);
    const hue2 = 260 + (scrollPercent * 0.3);

    body.style.background = `linear-gradient(135deg, hsl(${hue1}, 100%, 97%), hsl(${hue2}, 100%, 97%))`;
    body.style.backgroundAttachment = 'fixed';
  });
}

// ========================================
// INITIALIZE ALL
// ========================================

document.addEventListener('DOMContentLoaded', () => {
  // Only on desktop for performance
  if (window.innerWidth > 768) {
    initCustomCursor();
    createParticleBackground();
  }

  initParallax();
  initSmoothScroll();
  initLazyImages();
  initReadingProgress();
  initFloatingElements();
  initGradientScroll();

  // Optional: Typewriter effect for site title
  const siteTitle = document.querySelector('.site-title');
  if (siteTitle) {
    const originalText = siteTitle.textContent;
    // Uncomment to enable typewriter effect
    // typewriterEffect(siteTitle, originalText, 100);
  }

  console.log('🎨 Modern animations initialized!');
});

// ========================================
// PERFORMANCE OPTIMIZATION
// ========================================

// Debounce function for scroll events
function debounce(func, wait) {
  let timeout;
  return function executedFunction(...args) {
    const later = () => {
      clearTimeout(timeout);
      func(...args);
    };
    clearTimeout(timeout);
    timeout = setTimeout(later, wait);
  };
}

// Reduce motion for users who prefer it
if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
  document.documentElement.style.setProperty('--transition-base', 'none');
  document.documentElement.style.setProperty('--transition-fast', 'none');
  document.documentElement.style.setProperty('--transition-slow', 'none');
}

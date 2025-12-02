/**
 * OBER Theme - Advanced JavaScript
 * Features: Dark Mode, Smooth Scroll, Parallax, Animations
 * RTL Support
 */

(function() {
  'use strict';

  // ================================
  // Dark/Light Mode Toggle
  // ================================

  const themeToggle = () => {
    const themeBtn = document.getElementById('theme-toggle');
    const themeIcon = document.getElementById('theme-icon');
    const htmlElement = document.documentElement;

    // Load saved theme
    const savedTheme = localStorage.getItem('theme') || 'light';
    htmlElement.setAttribute('data-theme', savedTheme);
    updateThemeIcon(savedTheme);

    // Toggle theme
    if (themeBtn) {
      themeBtn.addEventListener('click', () => {
        const currentTheme = htmlElement.getAttribute('data-theme');
        const newTheme = currentTheme === 'dark' ? 'light' : 'dark';

        htmlElement.setAttribute('data-theme', newTheme);
        localStorage.setItem('theme', newTheme);
        updateThemeIcon(newTheme);

        // Add smooth transition effect
        document.body.style.transition = 'all 0.3s ease';
      });
    }

    function updateThemeIcon(theme) {
      if (themeIcon) {
        themeIcon.textContent = theme === 'dark' ? '☀️' : '🌙';
      }
    }
  };

  // ================================
  // Smooth Scroll
  // ================================

  const smoothScroll = () => {
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
      anchor.addEventListener('click', function(e) {
        const href = this.getAttribute('href');
        if (href === '#') return;

        e.preventDefault();
        const target = document.querySelector(href);

        if (target) {
          target.scrollIntoView({
            behavior: 'smooth',
            block: 'start'
          });
        }
      });
    });
  };

  // ================================
  // Scroll Header Effect
  // ================================

  const scrollHeader = () => {
    const header = document.querySelector('.site-header');
    let lastScroll = 0;

    window.addEventListener('scroll', () => {
      const currentScroll = window.pageYOffset;

      if (currentScroll > 100) {
        header.classList.add('scrolled');
      } else {
        header.classList.remove('scrolled');
      }

      // Hide header on scroll down, show on scroll up
      if (currentScroll > lastScroll && currentScroll > 500) {
        header.style.transform = 'translateY(-100%)';
      } else {
        header.style.transform = 'translateY(0)';
      }

      lastScroll = currentScroll;
    });
  };

  // ================================
  // Parallax Effect
  // ================================

  const parallaxEffect = () => {
    const parallaxElements = document.querySelectorAll('[data-parallax]');

    window.addEventListener('scroll', () => {
      const scrolled = window.pageYOffset;

      parallaxElements.forEach(element => {
        const speed = element.getAttribute('data-parallax') || 0.5;
        const yPos = -(scrolled * speed);
        element.style.transform = `translateY(${yPos}px)`;
      });
    });
  };

  // ================================
  // Scroll Reveal Animation
  // ================================

  const scrollReveal = () => {
    const reveals = document.querySelectorAll('.reveal');

    const revealOnScroll = () => {
      reveals.forEach(element => {
        const elementTop = element.getBoundingClientRect().top;
        const windowHeight = window.innerHeight;
        const revealPoint = 150;

        if (elementTop < windowHeight - revealPoint) {
          element.classList.add('active');
        }
      });
    };

    window.addEventListener('scroll', revealOnScroll);
    revealOnScroll(); // Run on load
  };

  // ================================
  // Animated Counter
  // ================================

  const animateCounter = () => {
    const counters = document.querySelectorAll('[data-count]');

    counters.forEach(counter => {
      const target = parseInt(counter.getAttribute('data-count'));
      const duration = 2000;
      const increment = target / (duration / 16);
      let current = 0;

      const updateCounter = () => {
        current += increment;
        if (current < target) {
          counter.textContent = Math.floor(current);
          requestAnimationFrame(updateCounter);
        } else {
          counter.textContent = target;
        }
      };

      // Trigger when element is visible
      const observer = new IntersectionObserver((entries) => {
        if (entries[0].isIntersecting) {
          updateCounter();
          observer.disconnect();
        }
      });

      observer.observe(counter);
    });
  };

  // ================================
  // Typing Effect
  // ================================

  const typingEffect = () => {
    const typingElements = document.querySelectorAll('[data-typing]');

    typingElements.forEach(element => {
      const text = element.getAttribute('data-typing');
      const speed = parseInt(element.getAttribute('data-speed')) || 100;
      let index = 0;

      element.textContent = '';

      const type = () => {
        if (index < text.length) {
          element.textContent += text.charAt(index);
          index++;
          setTimeout(type, speed);
        }
      };

      // Start typing when element is visible
      const observer = new IntersectionObserver((entries) => {
        if (entries[0].isIntersecting) {
          type();
          observer.disconnect();
        }
      });

      observer.observe(element);
    });
  };

  // ================================
  // Mobile Menu Toggle
  // ================================

  const mobileMenu = () => {
    const menuToggle = document.getElementById('mobile-menu-toggle');
    const mainNav = document.querySelector('.main-nav');

    if (menuToggle && mainNav) {
      menuToggle.addEventListener('click', () => {
        mainNav.classList.toggle('active');
        menuToggle.classList.toggle('active');
      });

      // Close menu on link click
      mainNav.querySelectorAll('a').forEach(link => {
        link.addEventListener('click', () => {
          mainNav.classList.remove('active');
          menuToggle.classList.remove('active');
        });
      });
    }
  };

  // ================================
  // Lazy Loading Images
  // ================================

  const lazyLoadImages = () => {
    const images = document.querySelectorAll('img[data-src]');

    const imageObserver = new IntersectionObserver((entries, observer) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          const img = entry.target;
          img.src = img.getAttribute('data-src');
          img.removeAttribute('data-src');
          observer.unobserve(img);
        }
      });
    });

    images.forEach(img => imageObserver.observe(img));
  };

  // ================================
  // Reading Progress Bar
  // ================================

  const readingProgress = () => {
    const progressBar = document.getElementById('reading-progress');

    if (progressBar) {
      window.addEventListener('scroll', () => {
        const windowHeight = window.innerHeight;
        const documentHeight = document.documentElement.scrollHeight;
        const scrollTop = window.pageYOffset;
        const progress = (scrollTop / (documentHeight - windowHeight)) * 100;

        progressBar.style.width = `${progress}%`;
      });
    }
  };

  // ================================
  // Copy Code Button
  // ================================

  const copyCodeButtons = () => {
    const codeBlocks = document.querySelectorAll('pre code');

    codeBlocks.forEach(code => {
      const button = document.createElement('button');
      button.className = 'copy-code-btn';
      button.textContent = 'העתק';
      button.setAttribute('aria-label', 'העתק קוד');

      const pre = code.parentElement;
      pre.style.position = 'relative';
      pre.appendChild(button);

      button.addEventListener('click', () => {
        navigator.clipboard.writeText(code.textContent).then(() => {
          button.textContent = '✓ הועתק!';
          setTimeout(() => {
            button.textContent = 'העתק';
          }, 2000);
        });
      });
    });
  };

  // ================================
  // Particle Background Effect
  // ================================

  const particleBackground = () => {
    const canvas = document.getElementById('particles');
    if (!canvas) return;

    const ctx = canvas.getContext('2d');
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;

    const particles = [];
    const particleCount = 50;

    class Particle {
      constructor() {
        this.x = Math.random() * canvas.width;
        this.y = Math.random() * canvas.height;
        this.size = Math.random() * 3 + 1;
        this.speedX = Math.random() * 2 - 1;
        this.speedY = Math.random() * 2 - 1;
      }

      update() {
        this.x += this.speedX;
        this.y += this.speedY;

        if (this.x > canvas.width || this.x < 0) this.speedX *= -1;
        if (this.y > canvas.height || this.y < 0) this.speedY *= -1;
      }

      draw() {
        ctx.fillStyle = 'rgba(99, 102, 241, 0.5)';
        ctx.beginPath();
        ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
        ctx.fill();
      }
    }

    for (let i = 0; i < particleCount; i++) {
      particles.push(new Particle());
    }

    function animate() {
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      particles.forEach(particle => {
        particle.update();
        particle.draw();
      });
      requestAnimationFrame(animate);
    }

    animate();

    window.addEventListener('resize', () => {
      canvas.width = window.innerWidth;
      canvas.height = window.innerHeight;
    });
  };

  // ================================
  // Initialize All
  // ================================

  const init = () => {
    themeToggle();
    smoothScroll();
    scrollHeader();
    parallaxEffect();
    scrollReveal();
    animateCounter();
    typingEffect();
    mobileMenu();
    lazyLoadImages();
    readingProgress();
    copyCodeButtons();
    particleBackground();

    // Add loading animation
    document.body.classList.add('loaded');
  };

  // Run when DOM is ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }

})();

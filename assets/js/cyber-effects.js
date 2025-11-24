/**
 * 🔥 CYBER-TECH EFFECTS
 * Advanced JavaScript for elite developer blog
 * Matrix effects, glitch, terminal, and more
 */

// ========================================
// 1. MATRIX RAIN EFFECT
// ========================================

function initMatrixRain() {
  const canvas = document.createElement('canvas');
  canvas.id = 'matrix-canvas';
  document.body.prepend(canvas);

  const ctx = canvas.getContext('2d');

  canvas.width = window.innerWidth;
  canvas.height = window.innerHeight;

  const matrixChars = 'アイウエオカキクケコサシスセソタチツテトナニヌネノハヒフヘホマミムメモヤユヨラリルレロワヲン01';
  const charArray = matrixChars.split('');

  const fontSize = 16;
  const columns = canvas.width / fontSize;
  const drops = [];

  // Initialize drops
  for (let i = 0; i < columns; i++) {
    drops[i] = Math.random() * -100;
  }

  function draw() {
    // Semi-transparent black to create trail effect
    ctx.fillStyle = 'rgba(10, 14, 39, 0.05)';
    ctx.fillRect(0, 0, canvas.width, canvas.height);

    // Set text style
    ctx.fillStyle = '#00FFB3'; // Neon green
    ctx.font = fontSize + 'px monospace';

    for (let i = 0; i < drops.length; i++) {
      const text = charArray[Math.floor(Math.random() * charArray.length)];
      const x = i * fontSize;
      const y = drops[i] * fontSize;

      ctx.fillText(text, x, y);

      // Reset drop randomly
      if (y > canvas.height && Math.random() > 0.975) {
        drops[i] = 0;
      }

      drops[i]++;
    }
  }

  setInterval(draw, 35);

  // Resize canvas on window resize
  window.addEventListener('resize', () => {
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
  });
}

// ========================================
// 2. TERMINAL TYPING EFFECT
// ========================================

function initTerminalTyping() {
  const title = document.querySelector('.site-title');
  if (!title) return;

  const originalText = title.textContent;
  title.textContent = '';

  let charIndex = 0;

  function typeChar() {
    if (charIndex < originalText.length) {
      title.textContent += originalText.charAt(charIndex);
      charIndex++;
      setTimeout(typeChar, 100);
    }
  }

  setTimeout(typeChar, 500);
}

// ========================================
// 3. GLITCH TEXT EFFECT
// ========================================

function addGlitchEffect() {
  const headings = document.querySelectorAll('h1, h2');

  headings.forEach(heading => {
    if (!heading.classList.contains('site-title')) {
      const text = heading.textContent;
      heading.setAttribute('data-text', text);
      heading.classList.add('glitch');

      // Random glitch trigger
      setInterval(() => {
        if (Math.random() > 0.95) {
          heading.style.animation = 'glitch-anim 0.3s';
          setTimeout(() => {
            heading.style.animation = '';
          }, 300);
        }
      }, 2000);
    }
  });
}

// ========================================
// 4. TECH STATS COUNTER
// ========================================

function createTechStats() {
  const stats = [
    { number: 500, label: 'Lines of Code', suffix: '+' },
    { number: 50, label: 'Projects', suffix: '+' },
    { number: 100, label: 'Commits', suffix: '+' },
    { number: 99, label: 'Uptime', suffix: '%' }
  ];

  const statsContainer = document.createElement('div');
  statsContainer.className = 'tech-stats';

  stats.forEach(stat => {
    const card = document.createElement('div');
    card.className = 'stat-card';
    card.innerHTML = `
      <div class="stat-number" data-target="${stat.number}">${stat.suffix === '%' ? 0 : 0}${stat.suffix}</div>
      <div class="stat-label">${stat.label}</div>
    `;
    statsContainer.appendChild(card);
  });

  // Insert after header
  const header = document.querySelector('header');
  if (header) {
    header.after(statsContainer);
  }

  // Animate counters
  animateCounters();
}

function animateCounters() {
  const counters = document.querySelectorAll('.stat-number');

  counters.forEach(counter => {
    const target = parseInt(counter.getAttribute('data-target'));
    const suffix = counter.textContent.match(/[+%]/)?.[0] || '';
    let current = 0;
    const increment = target / 50;
    const duration = 2000;
    const stepTime = duration / 50;

    const timer = setInterval(() => {
      current += increment;
      if (current >= target) {
        counter.textContent = target + suffix;
        clearInterval(timer);
      } else {
        counter.textContent = Math.floor(current) + suffix;
      }
    }, stepTime);
  });
}

// ========================================
// 5. CODE PLAYGROUND COMPONENT
// ========================================

function createCodePlayground() {
  const playground = document.createElement('div');
  playground.className = 'code-playground cyber-border';
  playground.innerHTML = `
    <div class="playground-header" style="
      background: rgba(10, 14, 39, 0.9);
      padding: 1rem;
      border-bottom: 2px solid #0abdc6;
      display: flex;
      gap: 1rem;
      align-items: center;
    ">
      <span style="color: #00FFB3; font-family: 'Fira Code', monospace; font-weight: bold;">
        💻 Live Code Editor
      </span>
      <button class="cyber-button" style="padding: 0.5rem 1rem; font-size: 0.8rem;" onclick="runPlaygroundCode()">
        ▶ Run
      </button>
    </div>
    <div class="playground-body" style="
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 0;
      background: #05070f;
    ">
      <textarea id="code-input" style="
        background: #0a0e27;
        color: #00FFB3;
        border: none;
        padding: 1.5rem;
        font-family: 'Fira Code', monospace;
        font-size: 14px;
        resize: none;
        min-height: 300px;
        border-right: 2px solid #0abdc6;
      " placeholder="// Write your JavaScript code here...
console.log('Hello, Cyber World!');">// Example code
const greeting = 'Welcome to Cyber Blog!';
console.log(greeting);

// Try editing and clicking Run!</textarea>
      <div id="code-output" style="
        background: #05070f;
        color: #0abdc6;
        padding: 1.5rem;
        font-family: 'Fira Code', monospace;
        font-size: 14px;
        min-height: 300px;
        overflow-y: auto;
        white-space: pre-wrap;
      "></div>
    </div>
  `;

  // Insert into page
  const firstArticle = document.querySelector('article');
  if (firstArticle) {
    firstArticle.before(playground);
  }
}

// Run code function (global scope)
window.runPlaygroundCode = function() {
  const input = document.getElementById('code-input');
  const output = document.getElementById('code-output');

  if (!input || !output) return;

  const code = input.value;
  output.textContent = ''; // Clear previous output

  // Capture console.log
  const originalLog = console.log;
  const logs = [];

  console.log = function(...args) {
    logs.push(args.join(' '));
    originalLog.apply(console, args);
  };

  try {
    eval(code);
    output.textContent = logs.length > 0 ? '✓ Output:\n' + logs.join('\n') : '✓ Code executed successfully (no output)';
    output.style.color = '#00FFB3'; // Success color
  } catch (error) {
    output.textContent = '✗ Error:\n' + error.message;
    output.style.color = '#ff0080'; // Error color
  }

  // Restore console.log
  console.log = originalLog;
};

// ========================================
// 6. COMMAND PALETTE
// ========================================

let commandPaletteOpen = false;

function createCommandPalette() {
  const palette = document.createElement('div');
  palette.id = 'command-palette';
  palette.style.cssText = `
    position: fixed;
    top: 20%;
    left: 50%;
    transform: translate(-50%, -50%) scale(0.9);
    width: 90%;
    max-width: 600px;
    background: rgba(10, 14, 39, 0.98);
    border: 2px solid #0abdc6;
    border-radius: 12px;
    box-shadow: 0 20px 60px rgba(0, 0, 0, 0.8);
    z-index: 10000;
    opacity: 0;
    pointer-events: none;
    transition: all 0.3s ease;
  `;

  palette.innerHTML = `
    <div style="padding: 1.5rem; border-bottom: 2px solid #ff0080;">
      <input
        type="text"
        id="command-input"
        placeholder="Type a command... (Ctrl+K to close)"
        style="
          width: 100%;
          background: #05070f;
          border: 1px solid #0abdc6;
          color: #00FFB3;
          padding: 1rem;
          font-family: 'Fira Code', monospace;
          font-size: 1rem;
          border-radius: 6px;
        "
      />
    </div>
    <div id="command-list" style="
      max-height: 300px;
      overflow-y: auto;
      padding: 1rem;
    ">
      <div class="command-item" data-action="home" style="padding: 0.8rem; cursor: pointer; color: #0abdc6; font-family: 'Fira Code', monospace; border-left: 3px solid transparent;">
        🏠 Go to Home
      </div>
      <div class="command-item" data-action="demo" style="padding: 0.8rem; cursor: pointer; color: #0abdc6; font-family: 'Fira Code', monospace; border-left: 3px solid transparent;">
        🎨 View Animations Demo
      </div>
      <div class="command-item" data-action="about" style="padding: 0.8rem; cursor: pointer; color: #0abdc6; font-family: 'Fira Code', monospace; border-left: 3px solid transparent;">
        📖 About
      </div>
      <div class="command-item" data-action="archive" style="padding: 0.8rem; cursor: pointer; color: #0abdc6; font-family: 'Fira Code', monospace; border-left: 3px solid transparent;">
        📁 Archive
      </div>
    </div>
  `;

  document.body.appendChild(palette);

  // Keyboard shortcut (Ctrl/Cmd + K)
  document.addEventListener('keydown', (e) => {
    if ((e.ctrlKey || e.metaKey) && e.key === 'k') {
      e.preventDefault();
      toggleCommandPalette();
    }
  });

  // Command item hover effect
  const items = palette.querySelectorAll('.command-item');
  items.forEach(item => {
    item.addEventListener('mouseenter', () => {
      item.style.borderLeftColor = '#ff0080';
      item.style.background = 'rgba(255, 0, 128, 0.1)';
    });
    item.addEventListener('mouseleave', () => {
      item.style.borderLeftColor = 'transparent';
      item.style.background = 'transparent';
    });
    item.addEventListener('click', () => {
      const action = item.getAttribute('data-action');
      executeCommand(action);
    });
  });
}

function toggleCommandPalette() {
  const palette = document.getElementById('command-palette');
  if (!palette) return;

  commandPaletteOpen = !commandPaletteOpen;

  if (commandPaletteOpen) {
    palette.style.opacity = '1';
    palette.style.transform = 'translate(-50%, 0)';
    palette.style.pointerEvents = 'all';
    document.getElementById('command-input')?.focus();
  } else {
    palette.style.opacity = '0';
    palette.style.transform = 'translate(-50%, -50%) scale(0.9)';
    palette.style.pointerEvents = 'none';
  }
}

function executeCommand(action) {
  const routes = {
    home: '/',
    demo: '/animations-demo/',
    about: '/about/',
    archive: '/archive/'
  };

  if (routes[action]) {
    window.location.href = routes[action];
  }
}

// ========================================
// 7. NEON CURSOR TRAIL
// ========================================

function createNeonCursorTrail() {
  const trail = [];
  const maxTrail = 20;

  document.addEventListener('mousemove', (e) => {
    const dot = document.createElement('div');
    dot.style.cssText = `
      position: fixed;
      width: 6px;
      height: 6px;
      background: #ff0080;
      border-radius: 50%;
      pointer-events: none;
      z-index: 9999;
      box-shadow: 0 0 10px #ff0080;
      left: ${e.clientX}px;
      top: ${e.clientY}px;
      transition: opacity 0.5s ease;
    `;

    document.body.appendChild(dot);
    trail.push(dot);

    setTimeout(() => {
      dot.style.opacity = '0';
      setTimeout(() => dot.remove(), 500);
    }, 50);

    // Remove old dots
    if (trail.length > maxTrail) {
      trail.shift().remove();
    }
  });
}

// ========================================
// 8. CYBER NOTIFICATIONS
// ========================================

function showCyberNotification(message, type = 'info') {
  const notification = document.createElement('div');
  notification.style.cssText = `
    position: fixed;
    top: 20px;
    right: 20px;
    background: rgba(10, 14, 39, 0.95);
    border: 2px solid ${type === 'success' ? '#00FFB3' : '#ff0080'};
    color: ${type === 'success' ? '#00FFB3' : '#ff0080'};
    padding: 1rem 1.5rem;
    border-radius: 8px;
    font-family: 'Fira Code', monospace;
    box-shadow: 0 0 20px ${type === 'success' ? 'rgba(0, 255, 179, 0.5)' : 'rgba(255, 0, 128, 0.5)'};
    z-index: 10001;
    animation: slideInRight 0.3s ease;
  `;
  notification.textContent = message;

  document.body.appendChild(notification);

  setTimeout(() => {
    notification.style.animation = 'slideOutRight 0.3s ease';
    setTimeout(() => notification.remove(), 300);
  }, 3000);
}

// Add CSS animations
const style = document.createElement('style');
style.textContent = `
  @keyframes slideInRight {
    from { transform: translateX(400px); opacity: 0; }
    to { transform: translateX(0); opacity: 1; }
  }
  @keyframes slideOutRight {
    from { transform: translateX(0); opacity: 1; }
    to { transform: translateX(400px); opacity: 0; }
  }
`;
document.head.appendChild(style);

// ========================================
// 9. KONAMI CODE EASTER EGG
// ========================================

let konamiCode = [];
const konamiSequence = ['ArrowUp', 'ArrowUp', 'ArrowDown', 'ArrowDown', 'ArrowLeft', 'ArrowRight', 'ArrowLeft', 'ArrowRight', 'b', 'a'];

function initKonamiCode() {
  document.addEventListener('keydown', (e) => {
    konamiCode.push(e.key);
    konamiCode = konamiCode.slice(-10);

    if (konamiCode.join(',') === konamiSequence.join(',')) {
      activateSecretMode();
      konamiCode = [];
    }
  });
}

function activateSecretMode() {
  showCyberNotification('🎮 KONAMI CODE ACTIVATED! Ultra Cyber Mode ON!', 'success');

  // Add rainbow effect to everything
  document.body.style.animation = 'rainbow-bg 3s linear infinite';

  const rainbowStyle = document.createElement('style');
  rainbowStyle.textContent = `
    @keyframes rainbow-bg {
      0% { filter: hue-rotate(0deg); }
      100% { filter: hue-rotate(360deg); }
    }
  `;
  document.head.appendChild(rainbowStyle);
}

// ========================================
// 10. INITIALIZE ALL CYBER EFFECTS
// ========================================

document.addEventListener('DOMContentLoaded', () => {
  console.log('%c🔥 CYBER BLOG INITIALIZED', 'color: #00FFB3; font-size: 20px; font-weight: bold; text-shadow: 0 0 10px #00FFB3;');
  console.log('%c> System Status: ONLINE', 'color: #0abdc6; font-family: monospace;');
  console.log('%c> Mode: ELITE DEVELOPER', 'color: #ff0080; font-family: monospace;');

  // Desktop only effects
  if (window.innerWidth > 768) {
    initMatrixRain();
    createNeonCursorTrail();
  }

  // All devices
  initTerminalTyping();
  addGlitchEffect();
  createTechStats();
  createCodePlayground();
  createCommandPalette();
  initKonamiCode();

  // Welcome notification
  setTimeout(() => {
    showCyberNotification('⚡ Welcome to Cyber Blog! Press Ctrl+K for commands', 'success');
  }, 1000);
});

// Export for debugging
window.CyberBlog = {
  showNotification: showCyberNotification,
  togglePalette: toggleCommandPalette,
  version: '2.0 CYBER'
};

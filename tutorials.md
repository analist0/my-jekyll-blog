---
layout: default
title: מדריכים
---

<section class="hero" style="min-height: 60vh;">
  <div class="hero-background"></div>
  <div class="container">
    <div class="hero-content">
      <h1 class="hero-title" style="font-size: clamp(2.5rem, 6vw, 4rem);">
        📚 מדריכים נדירים
      </h1>
      <p class="hero-subtitle">
        מדריכים מעמיקים וייחודיים שילמדו אתכם כל מה שצריך לדעת
      </p>
    </div>
  </div>
</section>

<section class="section reveal">
  <div class="container">
    <!-- Difficulty Filter -->
    <div style="display: flex; justify-content: center; gap: 1rem; margin-bottom: 3rem; flex-wrap: wrap;">
      <button class="filter-btn active" data-level="all">
        הכל
      </button>
      <button class="filter-btn" data-level="beginner">
        🟢 מתחילים
      </button>
      <button class="filter-btn" data-level="intermediate">
        🟡 בינוני
      </button>
      <button class="filter-btn" data-level="advanced">
        🔴 מתקדמים
      </button>
    </div>

    <div class="posts-grid">
      <!-- Tutorial 1 -->
      <div class="post-card" data-level="intermediate">
        <div class="post-image" style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); display: flex; align-items: center; justify-content: center; font-size: 4rem;">
          🎨
        </div>
        <div class="post-content">
          <div class="post-meta">
            <span>🟡 בינוני</span>
            <span>45 דקות</span>
          </div>
          <h3 class="post-title">בניית בלוג עם Jekyll</h3>
          <p class="post-excerpt">
            מדריך מלא ליצירת בלוג מתקדם עם Jekyll, GitHub Pages, עיצוב מודרני ותמיכה בעברית.
          </p>
          <div style="display: flex; gap: 0.5rem; margin: 1rem 0; flex-wrap: wrap;">
            <span style="font-size: 0.75rem; padding: 0.25rem 0.5rem; background: var(--bg-secondary); border-radius: 4px;">#Jekyll</span>
            <span style="font-size: 0.75rem; padding: 0.25rem 0.5rem; background: var(--bg-secondary); border-radius: 4px;">#GitHubPages</span>
            <span style="font-size: 0.75rem; padding: 0.25rem 0.5rem; background: var(--bg-secondary); border-radius: 4px;">#RTL</span>
          </div>
          <a href="#" class="btn btn-primary" style="width: 100%;">
            התחל ללמוד →
          </a>
        </div>
      </div>

      <!-- Tutorial 2 -->
      <div class="post-card" data-level="advanced">
        <div class="post-image" style="background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%); display: flex; align-items: center; justify-content: center; font-size: 4rem;">
          🔗
        </div>
        <div class="post-content">
          <div class="post-meta">
            <span>🔴 מתקדם</span>
            <span>90 דקות</span>
          </div>
          <h3 class="post-title">פיתוח MCP Servers</h3>
          <p class="post-excerpt">
            למד לבנות MCP Servers מותאמים אישית עם Python, API integrations ו-Claude Code.
          </p>
          <div style="display: flex; gap: 0.5rem; margin: 1rem 0; flex-wrap: wrap;">
            <span style="font-size: 0.75rem; padding: 0.25rem 0.5rem; background: var(--bg-secondary); border-radius: 4px;">#Python</span>
            <span style="font-size: 0.75rem; padding: 0.25rem 0.5rem; background: var(--bg-secondary); border-radius: 4px;">#MCP</span>
            <span style="font-size: 0.75rem; padding: 0.25rem 0.5rem; background: var(--bg-secondary); border-radius: 4px;">#API</span>
          </div>
          <a href="#" class="btn btn-primary" style="width: 100%;">
            התחל ללמוד →
          </a>
        </div>
      </div>

      <!-- Tutorial 3 -->
      <div class="post-card" data-level="beginner">
        <div class="post-image" style="background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%); display: flex; align-items: center; justify-content: center; font-size: 4rem;">
          💻
        </div>
        <div class="post-content">
          <div class="post-meta">
            <span>🟢 מתחילים</span>
            <span>30 דקות</span>
          </div>
          <h3 class="post-title">התחלה עם Git ו-GitHub</h3>
          <p class="post-excerpt">
            מדריך למתחילים לשליטה ב-Git, ניהול repositories ופרסום פרויקטים ב-GitHub.
          </p>
          <div style="display: flex; gap: 0.5rem; margin: 1rem 0; flex-wrap: wrap;">
            <span style="font-size: 0.75rem; padding: 0.25rem 0.5rem; background: var(--bg-secondary); border-radius: 4px;">#Git</span>
            <span style="font-size: 0.75rem; padding: 0.25rem 0.5rem; background: var(--bg-secondary); border-radius: 4px;">#GitHub</span>
            <span style="font-size: 0.75rem; padding: 0.25rem 0.5rem; background: var(--bg-secondary); border-radius: 4px;">#VersionControl</span>
          </div>
          <a href="#" class="btn btn-primary" style="width: 100%;">
            התחל ללמוד →
          </a>
        </div>
      </div>

      <!-- Tutorial 4 -->
      <div class="post-card" data-level="intermediate">
        <div class="post-image" style="background: linear-gradient(135deg, #fa709a 0%, #fee140 100%); display: flex; align-items: center; justify-content: center; font-size: 4rem;">
          🤖
        </div>
        <div class="post-content">
          <div class="post-meta">
            <span>🟡 בינוני</span>
            <span>60 דקות</span>
          </div>
          <h3 class="post-title">אוטומציה עם n8n</h3>
          <p class="post-excerpt">
            בנה workflows אוטומטיים מתקדמים עם n8n, כולל RSS, Telegram ו-API integrations.
          </p>
          <div style="display: flex; gap: 0.5rem; margin: 1rem 0; flex-wrap: wrap;">
            <span style="font-size: 0.75rem; padding: 0.25rem 0.5rem; background: var(--bg-secondary); border-radius: 4px;">#n8n</span>
            <span style="font-size: 0.75rem; padding: 0.25rem 0.5rem; background: var(--bg-secondary); border-radius: 4px;">#Automation</span>
            <span style="font-size: 0.75rem; padding: 0.25rem 0.5rem; background: var(--bg-secondary); border-radius: 4px;">#NoCode</span>
          </div>
          <a href="#" class="btn btn-primary" style="width: 100%;">
            התחל ללמוד →
          </a>
        </div>
      </div>

      <!-- Tutorial 5 -->
      <div class="post-card" data-level="advanced">
        <div class="post-image" style="background: linear-gradient(135deg, #30cfd0 0%, #330867 100%); display: flex; align-items: center; justify-content: center; font-size: 4rem;">
          🧠
        </div>
        <div class="post-content">
          <div class="post-meta">
            <span>🔴 מתקדם</span>
            <span>120 דקות</span>
          </div>
          <h3 class="post-title">AI Agents עם Ollama</h3>
          <p class="post-excerpt">
            פתח סוכני AI אוטונומיים עם Ollama, Python ו-LLM models מקומיים.
          </p>
          <div style="display: flex; gap: 0.5rem; margin: 1rem 0; flex-wrap: wrap;">
            <span style="font-size: 0.75rem; padding: 0.25rem 0.5rem; background: var(--bg-secondary); border-radius: 4px;">#AI</span>
            <span style="font-size: 0.75rem; padding: 0.25rem 0.5rem; background: var(--bg-secondary); border-radius: 4px;">#Ollama</span>
            <span style="font-size: 0.75rem; padding: 0.25rem 0.5rem; background: var(--bg-secondary); border-radius: 4px;">#LLM</span>
          </div>
          <a href="#" class="btn btn-primary" style="width: 100%;">
            התחל ללמוד →
          </a>
        </div>
      </div>

      <!-- Tutorial 6 -->
      <div class="post-card" data-level="beginner">
        <div class="post-image" style="background: linear-gradient(135deg, #a8edea 0%, #fed6e3 100%); display: flex; align-items: center; justify-content: center; font-size: 4rem;">
          🎯
        </div>
        <div class="post-content">
          <div class="post-meta">
            <span>🟢 מתחילים</span>
            <span>20 דקות</span>
          </div>
          <h3 class="post-title">CSS Grid ו-Flexbox</h3>
          <p class="post-excerpt">
            למד לעצב layouts מודרניים עם CSS Grid ו-Flexbox, כולל דוגמאות מעשיות.
          </p>
          <div style="display: flex; gap: 0.5rem; margin: 1rem 0; flex-wrap: wrap;">
            <span style="font-size: 0.75rem; padding: 0.25rem 0.5rem; background: var(--bg-secondary); border-radius: 4px;">#CSS</span>
            <span style="font-size: 0.75rem; padding: 0.25rem 0.5rem; background: var(--bg-secondary); border-radius: 4px;">#Grid</span>
            <span style="font-size: 0.75rem; padding: 0.25rem 0.5rem; background: var(--bg-secondary); border-radius: 4px;">#Flexbox</span>
          </div>
          <a href="#" class="btn btn-primary" style="width: 100%;">
            התחל ללמוד →
          </a>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- Learning Path Section -->
<section class="section reveal" style="background: var(--bg-secondary);">
  <div class="container">
    <h2 class="section-title">מסלולי למידה מומלצים</h2>

    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 2rem; margin-top: 3rem;">
      <div style="padding: 2rem; background: var(--bg-primary); border-radius: 20px; border: 1px solid var(--border);">
        <div style="font-size: 3rem; margin-bottom: 1rem;">🚀</div>
        <h3 style="margin-bottom: 1rem;">מסלול המתחילים</h3>
        <ul style="list-style: none; padding: 0; color: var(--text-secondary);">
          <li style="padding: 0.5rem 0;">✓ Git ו-GitHub</li>
          <li style="padding: 0.5rem 0;">✓ CSS Grid & Flexbox</li>
          <li style="padding: 0.5rem 0;">✓ Jekyll Basics</li>
          <li style="padding: 0.5rem 0;">✓ פרסום ב-GitHub Pages</li>
        </ul>
      </div>

      <div style="padding: 2rem; background: var(--bg-primary); border-radius: 20px; border: 1px solid var(--border);">
        <div style="font-size: 3rem; margin-bottom: 1rem;">⚡</div>
        <h3 style="margin-bottom: 1rem;">מסלול המתקדמים</h3>
        <ul style="list-style: none; padding: 0; color: var(--text-secondary);">
          <li style="padding: 0.5rem 0;">✓ Jekyll Advanced</li>
          <li style="padding: 0.5rem 0;">✓ n8n Automation</li>
          <li style="padding: 0.5rem 0;">✓ MCP Servers</li>
          <li style="padding: 0.5rem 0;">✓ AI Agents</li>
        </ul>
      </div>

      <div style="padding: 2rem; background: var(--bg-primary); border-radius: 20px; border: 1px solid var(--border);">
        <div style="font-size: 3rem; margin-bottom: 1rem;">🎯</div>
        <h3 style="margin-bottom: 1rem;">מסלול האינטגרציה</h3>
        <ul style="list-style: none; padding: 0; color: var(--text-secondary);">
          <li style="padding: 0.5rem 0;">✓ API Integration</li>
          <li style="padding: 0.5rem 0;">✓ Database Design</li>
          <li style="padding: 0.5rem 0;">✓ Cloud Services</li>
          <li style="padding: 0.5rem 0;">✓ פרויקט מלא</li>
        </ul>
      </div>
    </div>
  </div>
</section>

<script>
// Level Filter
document.addEventListener('DOMContentLoaded', function() {
  const filterButtons = document.querySelectorAll('[data-level]');
  const tutorials = document.querySelectorAll('.post-card[data-level]');

  filterButtons.forEach(button => {
    button.addEventListener('click', function() {
      const level = this.getAttribute('data-level');

      filterButtons.forEach(btn => btn.classList.remove('active'));
      this.classList.add('active');

      tutorials.forEach(tutorial => {
        const tutorialLevel = tutorial.getAttribute('data-level');

        if (level === 'all' || tutorialLevel === level) {
          tutorial.style.display = 'block';
        } else {
          tutorial.style.display = 'none';
        }
      });
    });
  });
});
</script>

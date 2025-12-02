---
layout: default
title: בית
---

<!-- Hero Section with Parallax -->
<section class="hero" data-parallax="0.5">
  <div class="hero-background"></div>
  <div class="container">
    <div class="hero-content">
      <h1 class="hero-title">
        יוצרים את העתיד של הטכנולוגיה
      </h1>
      <p class="hero-subtitle">
        בלוג מתקדם עם עיצוב מודרני | מדריכים נדירים | פורטפוליו מרשים | תוכן איכותי
      </p>
      <div class="hero-cta">
        <a href="#posts" class="btn btn-primary">גלו את התוכן</a>
        <a href="{{ '/portfolio' | relative_url }}" class="btn btn-secondary">הפורטפוליו שלנו</a>
      </div>
    </div>
  </div>
</section>

<!-- Features Section -->
<section class="section reveal">
  <div class="container">
    <h2 class="section-title">מה תמצאו כאן?</h2>

    <div class="posts-grid">
      <div class="post-card">
        <div class="post-content">
          <div style="font-size: 3rem; margin-bottom: 1rem;">🎨</div>
          <h3 class="post-title">עיצוב מתקדם</h3>
          <p class="post-excerpt">
            תבניות ועיצובים נדירים עם אנימציות מתקדמות, Parallax effects, ו-Dark Mode חלק.
          </p>
          <a href="{{ '/portfolio' | relative_url }}" class="read-more">
            צפו בפרויקטים →
          </a>
        </div>
      </div>

      <div class="post-card">
        <div class="post-content">
          <div style="font-size: 3rem; margin-bottom: 1rem;">📚</div>
          <h3 class="post-title">מדריכים נדירים</h3>
          <p class="post-excerpt">
            מדריכים מעמיקים וייחודיים בנושאים מתקדמים שלא תמצאו במקומות אחרים.
          </p>
          <a href="{{ '/tutorials' | relative_url }}" class="read-more">
            לכל המדריכים →
          </a>
        </div>
      </div>

      <div class="post-card">
        <div class="post-content">
          <div style="font-size: 3rem; margin-bottom: 1rem;">💻</div>
          <h3 class="post-title">פיתוח מתקדם</h3>
          <p class="post-excerpt">
            קוד נקי, ארכיטקטורה מתקדמת, ופתרונות יצירתיים לבעיות מורכבות.
          </p>
          <a href="{{ '/blog' | relative_url }}" class="read-more">
            קראו את הבלוג →
          </a>
        </div>
      </div>

      <div class="post-card">
        <div class="post-content">
          <div style="font-size: 3rem; margin-bottom: 1rem;">🚀</div>
          <h3 class="post-title">טכנולוגיות חדשות</h3>
          <p class="post-excerpt">
            עדכונים על הטכנולוגיות העדכניות ביותר והכלים המתקדמים ביותר בתחום.
          </p>
          <a href="{{ '/blog' | relative_url }}" class="read-more">
            גלו עוד →
          </a>
        </div>
      </div>

      <div class="post-card">
        <div class="post-content">
          <div style="font-size: 3rem; margin-bottom: 1rem;">🎯</div>
          <h3 class="post-title">פרויקטים אמיתיים</h3>
          <p class="post-excerpt">
            תיקי עבודות מלאים עם מקורות קוד, הסברים מפורטים, ותהליך הפיתוח.
          </p>
          <a href="{{ '/portfolio' | relative_url }}" class="read-more">
            לפרויקטים →
          </a>
        </div>
      </div>

      <div class="post-card">
        <div class="post-content">
          <div style="font-size: 3rem; margin-bottom: 1rem;">🌟</div>
          <h3 class="post-title">קוד פתוח</h3>
          <p class="post-excerpt">
            כל הקוד זמין ב-GitHub, עם תיעוד מלא והסברים מפורטים לכל חלק.
          </p>
          <a href="https://github.com/analist0" target="_blank" class="read-more">
            ל-GitHub →
          </a>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- Latest Posts Section -->
<section id="posts" class="section reveal">
  <div class="container">
    <h2 class="section-title">פוסטים אחרונים</h2>

    {% if site.posts.size > 0 %}
    <div class="posts-grid">
      {% for post in site.posts limit:6 %}
      <article class="post-card">
        {% if post.image %}
        <img src="{{ post.image | relative_url }}" alt="{{ post.title }}" class="post-image" loading="lazy">
        {% else %}
        <div class="post-image" style="background: linear-gradient(135deg, #6366f1 0%, #8b5cf6 100%); display: flex; align-items: center; justify-content: center; font-size: 4rem;">
          📝
        </div>
        {% endif %}

        <div class="post-content">
          <div class="post-meta">
            <span>{{ post.date | date: "%d.%m.%Y" }}</span>
            {% if post.categories %}
            <span>{{ post.categories | first }}</span>
            {% endif %}
          </div>

          <h3 class="post-title">
            <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
          </h3>

          {% if post.excerpt %}
          <p class="post-excerpt">
            {{ post.excerpt | strip_html | truncate: 150 }}
          </p>
          {% endif %}

          <a href="{{ post.url | relative_url }}" class="read-more">
            קרא עוד →
          </a>
        </div>
      </article>
      {% endfor %}
    </div>

    <div class="text-center mt-4">
      <a href="{{ '/blog' | relative_url }}" class="btn btn-primary">כל הפוסטים</a>
    </div>

    {% else %}
    <div class="text-center">
      <p style="font-size: 1.2rem; color: var(--text-secondary); margin: 3rem 0;">
        🚀 הבלוג בבנייה! פוסטים חדשים יגיעו בקרוב...
      </p>
    </div>
    {% endif %}
  </div>
</section>

<!-- Stats Section -->
<section class="section reveal" style="background: var(--bg-secondary); padding: 4rem 0;">
  <div class="container">
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 3rem; text-align: center;">
      <div>
        <div style="font-size: 3rem; font-weight: 900; color: var(--accent); margin-bottom: 0.5rem;" data-count="50">0</div>
        <div style="color: var(--text-secondary);">פרויקטים</div>
      </div>
      <div>
        <div style="font-size: 3rem; font-weight: 900; color: var(--accent); margin-bottom: 0.5rem;" data-count="100">0</div>
        <div style="color: var(--text-secondary);">מדריכים</div>
      </div>
      <div>
        <div style="font-size: 3rem; font-weight: 900; color: var(--accent); margin-bottom: 0.5rem;" data-count="1000">0</div>
        <div style="color: var(--text-secondary);">קוראים</div>
      </div>
      <div>
        <div style="font-size: 3rem; font-weight: 900; color: var(--accent); margin-bottom: 0.5rem;" data-count="5">0</div>
        <div style="color: var(--text-secondary);">שנות ניסיון</div>
      </div>
    </div>
  </div>
</section>

<!-- CTA Section -->
<section class="section reveal">
  <div class="container text-center">
    <h2 style="font-size: clamp(2rem, 5vw, 3rem); margin-bottom: 1.5rem;">
      מוכנים להתחיל?
    </h2>
    <p style="font-size: 1.2rem; color: var(--text-secondary); margin-bottom: 2rem; max-width: 600px; margin-left: auto; margin-right: auto;">
      הצטרפו אלינו במסע לחקר הטכנולוגיות המתקדמות ביותר. בואו נבנה משהו מדהים ביחד!
    </p>
    <div style="display: flex; gap: 1rem; justify-content: center; flex-wrap: wrap;">
      <a href="{{ '/about' | relative_url }}" class="btn btn-primary">קראו עלינו</a>
      <a href="mailto:contact@example.com" class="btn btn-secondary">צרו קשר</a>
    </div>
  </div>
</section>

<style>
/* Mobile Menu Styles */
.mobile-menu-toggle {
  display: none;
  flex-direction: column;
  gap: 5px;
  background: none;
  border: none;
  cursor: pointer;
  padding: 0.5rem;
}

.mobile-menu-toggle span {
  width: 25px;
  height: 3px;
  background: var(--text-primary);
  transition: all 0.3s ease;
  border-radius: 3px;
}

@media (max-width: 768px) {
  .mobile-menu-toggle {
    display: flex;
  }

  .main-nav {
    position: fixed;
    top: 80px;
    left: 0;
    right: 0;
    background: var(--bg-primary);
    border-bottom: 1px solid var(--border);
    padding: 2rem;
    transform: translateY(-100%);
    opacity: 0;
    transition: all 0.3s ease;
    z-index: 999;
  }

  .main-nav.active {
    transform: translateY(0);
    opacity: 1;
  }

  .main-nav ul {
    flex-direction: column;
    gap: 1.5rem;
  }
}
</style>

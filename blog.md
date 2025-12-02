---
layout: default
title: בלוג
---

<section class="section">
  <div class="container">
    <h1 class="section-title" style="font-size: clamp(2.5rem, 5vw, 4rem); margin-bottom: 1rem;">
      📝 הבלוג שלנו
    </h1>
    <p style="text-align: center; color: var(--text-secondary); font-size: 1.2rem; max-width: 700px; margin: 0 auto 3rem;">
      מדריכים, מאמרים וכתבות טכנולוגיות מעמיקות על פיתוח, עיצוב וטכנולוגיות מתקדמות
    </p>

    <!-- Category Filter -->
    <div style="display: flex; justify-content: center; gap: 1rem; margin-bottom: 3rem; flex-wrap: wrap;">
      <button class="filter-btn active" data-filter="all">
        הכל
      </button>
      <button class="filter-btn" data-filter="technology">
        טכנולוגיה
      </button>
      <button class="filter-btn" data-filter="design">
        עיצוב
      </button>
      <button class="filter-btn" data-filter="tutorials">
        מדריכים
      </button>
      <button class="filter-btn" data-filter="development">
        פיתוח
      </button>
    </div>

    <!-- Posts Grid -->
    {% if site.posts.size > 0 %}
    <div class="posts-grid" id="posts-container">
      {% for post in site.posts %}
      <article class="post-card reveal" data-category="{{ post.categories | first | default: 'technology' }}">
        {% if post.image %}
        <img src="{{ post.image | relative_url }}" alt="{{ post.title }}" class="post-image" loading="lazy">
        {% else %}
        <div class="post-image" style="background: linear-gradient(135deg, #6366f1 0%, #8b5cf6 100%); display: flex; align-items: center; justify-content: center; font-size: 4rem;">
          {% if post.categories contains 'design' %}
            🎨
          {% elsif post.categories contains 'tutorials' %}
            📚
          {% elsif post.categories contains 'development' %}
            💻
          {% else %}
            📝
          {% endif %}
        </div>
        {% endif %}

        <div class="post-content">
          <div class="post-meta">
            <span>{{ post.date | date: "%d.%m.%Y" }}</span>
            {% if post.categories %}
            <span class="category-badge">{{ post.categories | first }}</span>
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

          <div style="display: flex; justify-content: space-between; align-items: center; margin-top: 1rem;">
            <a href="{{ post.url | relative_url }}" class="read-more">
              קרא עוד →
            </a>
            {% if post.tags %}
            <div style="display: flex; gap: 0.5rem; flex-wrap: wrap;">
              {% for tag in post.tags limit:2 %}
              <span style="font-size: 0.75rem; padding: 0.25rem 0.5rem; background: var(--bg-secondary); border-radius: 4px; color: var(--text-secondary);">
                #{{ tag }}
              </span>
              {% endfor %}
            </div>
            {% endif %}
          </div>
        </div>
      </article>
      {% endfor %}
    </div>

    <!-- No Posts Message -->
    <div id="no-posts" style="display: none; text-align: center; padding: 3rem;">
      <p style="font-size: 1.2rem; color: var(--text-secondary);">
        😕 לא נמצאו פוסטים בקטגוריה זו
      </p>
    </div>

    {% else %}
    <div class="text-center" style="padding: 5rem 0;">
      <div style="font-size: 5rem; margin-bottom: 1rem;">📝</div>
      <h2>עדיין אין פוסטים</h2>
      <p style="color: var(--text-secondary); margin-top: 1rem;">
        התוכן בדרך! בקרו שוב בקרוב.
      </p>
    </div>
    {% endif %}
  </div>
</section>

<!-- Newsletter Section -->
<section class="section reveal" style="background: var(--bg-secondary);">
  <div class="container text-center">
    <h2 style="margin-bottom: 1rem;">📬 הישארו מעודכנים</h2>
    <p style="color: var(--text-secondary); margin-bottom: 2rem; max-width: 500px; margin-left: auto; margin-right: auto;">
      קבלו עדכונים על פוסטים חדשים, מדריכים ותוכן בלעדי ישירות למייל
    </p>
    <form style="display: flex; gap: 1rem; max-width: 500px; margin: 0 auto; flex-wrap: wrap; justify-content: center;">
      <input
        type="email"
        placeholder="כתובת המייל שלך"
        required
        style="flex: 1; min-width: 250px; padding: 1rem; border: 1px solid var(--border); border-radius: 50px; background: var(--bg-primary); color: var(--text-primary); font-size: 1rem;"
      >
      <button type="submit" class="btn btn-primary">
        הרשמה
      </button>
    </form>
  </div>
</section>

<style>
/* Filter Buttons */
.filter-btn {
  padding: 0.75rem 1.5rem;
  border: 2px solid var(--border);
  background: transparent;
  color: var(--text-primary);
  border-radius: 50px;
  cursor: pointer;
  font-weight: 600;
  transition: all 0.3s ease;
}

.filter-btn:hover {
  border-color: var(--accent);
  color: var(--accent);
  transform: translateY(-2px);
}

.filter-btn.active {
  background: var(--accent);
  color: white;
  border-color: var(--accent);
}

/* Category Badge */
.category-badge {
  background: var(--accent);
  color: white;
  padding: 0.25rem 0.75rem;
  border-radius: 20px;
  font-size: 0.875rem;
  font-weight: 600;
}

/* Mobile Optimizations */
@media (max-width: 768px) {
  .filter-btn {
    padding: 0.5rem 1rem;
    font-size: 0.875rem;
  }

  .posts-grid {
    grid-template-columns: 1fr !important;
  }
}
</style>

<script>
// Category Filter
document.addEventListener('DOMContentLoaded', function() {
  const filterButtons = document.querySelectorAll('.filter-btn');
  const posts = document.querySelectorAll('.post-card');
  const noPosts = document.getElementById('no-posts');

  filterButtons.forEach(button => {
    button.addEventListener('click', function() {
      const filter = this.getAttribute('data-filter');

      // Update active button
      filterButtons.forEach(btn => btn.classList.remove('active'));
      this.classList.add('active');

      // Filter posts
      let visibleCount = 0;
      posts.forEach(post => {
        const category = post.getAttribute('data-category');

        if (filter === 'all' || category === filter) {
          post.style.display = 'block';
          visibleCount++;
        } else {
          post.style.display = 'none';
        }
      });

      // Show/hide no posts message
      if (noPosts) {
        noPosts.style.display = visibleCount === 0 ? 'block' : 'none';
      }
    });
  });
});
</script>

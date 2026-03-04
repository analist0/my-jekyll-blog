---
layout: default
title: כל השיעורים
---

<div style="padding-top: 80px;"></div>

<section style="padding: 2rem 0 5rem;">
  <div class="container">

    <!-- Header -->
    <div class="section-header reveal" style="margin-bottom: 3rem;">
      <span class="section-label">ארכיון שיעורים</span>
      <h1 class="section-title">כל השיעורים</h1>
      <div class="section-divider"></div>
      <p style="color: var(--text-muted); margin-top: 1rem;">{{ site.posts | size }} שיעורים ומאמרים לכבוד ה׳</p>
    </div>

    <!-- Filter Buttons -->
    <div style="display: flex; gap: 0.75rem; flex-wrap: wrap; justify-content: center; margin-bottom: 3rem;" class="reveal">
      <button onclick="filterPosts('all')" class="filter-torah active" id="f-all">כל הנושאים</button>
      <button onclick="filterPosts('video')" class="filter-torah" id="f-video">🎬 וידאו</button>
      <button onclick="filterPosts('audio')" class="filter-torah" id="f-audio">🎧 שמע</button>
      <button onclick="filterPosts('slides')" class="filter-torah" id="f-slides">📊 מצגות</button>
      <button onclick="filterPosts('text')" class="filter-torah" id="f-text">📖 מאמרים</button>
    </div>

    <!-- Posts Grid -->
    {% if site.posts.size > 0 %}
    <div class="posts-grid" id="postsGrid">
      {% for post in site.posts %}
      <article class="post-card reveal" data-media="{{ post.media_type | default: 'text' }}">

        <div class="card-thumb
          {% if post.media_type == 'video' %}card-thumb-video
          {% elsif post.media_type == 'audio' %}card-thumb-audio
          {% elsif post.media_type == 'slides' %}card-thumb-slides
          {% else %}card-thumb-torah{% endif %}">
          <span>{% if post.media_type == 'video' %}🎬{% elsif post.media_type == 'audio' %}🎧{% elsif post.media_type == 'slides' %}📊{% else %}📖{% endif %}</span>
          <div class="card-thumb-overlay"></div>
        </div>

        <div class="card-body">
          <div class="card-meta">
            <span class="card-date">📅 {{ post.date | date: "%d.%m.%Y" }}</span>
            {% if post.category %}<span class="card-category">{{ post.category }}</span>{% endif %}
            {% if post.media_type %}
            <span class="media-badge {{ post.media_type }}">
              {% if post.media_type == 'video' %}🎬 וידאו
              {% elsif post.media_type == 'audio' %}🎧 שמע
              {% elsif post.media_type == 'slides' %}📊 מצגת
              {% else %}📖 מאמר{% endif %}
            </span>
            {% endif %}
          </div>

          <h2 class="card-title">
            <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
          </h2>

          <p class="card-excerpt">{{ post.excerpt | strip_html | truncate: 140 }}</p>

          <div class="card-footer">
            <a href="{{ post.url | relative_url }}" class="read-more">המשך קריאה ←</a>
            {% if post.duration %}
            <span class="duration-badge">⏱ {{ post.duration }}</span>
            {% else %}
            <span class="duration-badge">⏱ {{ post.content | number_of_words | divided_by: 180 | at_least: 1 }} דק׳</span>
            {% endif %}
          </div>
        </div>
      </article>
      {% endfor %}
    </div>

    {% else %}
    <div style="text-align: center; padding: 5rem 0;">
      <div style="font-size: 5rem; margin-bottom: 1rem;">📖</div>
      <h2 style="font-family: var(--font-torah); color: var(--text-primary);">שיעורים בדרך</h2>
      <p style="color: var(--text-muted);">חזרו בקרוב לשיעורי תורה מרתקים</p>
    </div>
    {% endif %}

  </div>
</section>

<!-- Newsletter -->
<section class="newsletter-section">
  <div class="container reveal">
    <div style="font-size: 2.5rem; margin-bottom: 1rem;">✉️</div>
    <h2 class="newsletter-title">קבל שיעורים למייל</h2>
    <p class="newsletter-desc">הירשם ותקבל שיעורי תורה שבועיים ישירות</p>
    <form class="newsletter-form" onsubmit="return false;">
      <input type="email" class="newsletter-input" placeholder="כתובת המייל שלך" required>
      <button type="submit" class="newsletter-btn">הרשמה</button>
    </form>
  </div>
</section>

<style>
.filter-torah {
  padding: 0.6rem 1.25rem;
  border: 1.5px solid rgba(201,168,76,0.3);
  background: transparent;
  color: var(--text-muted);
  border-radius: 50px;
  cursor: pointer;
  font-family: var(--font-body);
  font-size: 0.9rem;
  font-weight: 500;
  transition: all 0.3s;
}
.filter-torah:hover,
.filter-torah.active {
  border-color: var(--gold);
  color: var(--gold);
  background: rgba(201,168,76,0.08);
}
</style>

<script>
function filterPosts(type) {
  document.querySelectorAll('.post-card').forEach(card => {
    if (type === 'all' || card.dataset.media === type) {
      card.style.display = '';
    } else {
      card.style.display = 'none';
    }
  });
  document.querySelectorAll('.filter-torah').forEach(btn => btn.classList.remove('active'));
  const active = document.getElementById('f-' + type);
  if (active) active.classList.add('active');
}
</script>

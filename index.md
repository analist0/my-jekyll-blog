---
layout: default
title: בית
---

<div class="hero">
  <h1>ברוכים הבאים לבלוג שלי</h1>
  <p class="lead">
    בלוג טכנולוגי מקצועי עם מערכות עיצוב מתקדמות
  </p>
</div>

<div class="divider"></div>

## 🎨 נושאי עיצוב זמינים

בחר את נושא העיצוב המתאים לך:

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 2rem; margin: 3rem 0;">

<article class="card-lime">
  <h3>🌑 Subduxion Style</h3>
  <p>עיצוב מינימליסטי מודרני עם נושא כהה והדגשי ליים ירוק. בהשראת Subduxion.com - מקצועי, נקי, ומהיר.</p>
  <div style="margin-top: 1.5rem;">
    <a href="{{ '/subduxion-demo/' | relative_url }}" class="button button-lime">צפה בדמו</a>
  </div>
</article>

<article class="card">
  <h3>🏢 Enterprise</h3>
  <p>עיצוב ארגוני מקצועי ברמה עסקית. נקי, אמין, ועוקב אחר סטנדרטים של IBM, Microsoft ו-Stripe.</p>
  <div style="margin-top: 1.5rem;">
    <a href="{{ '/enterprise-demo/' | relative_url }}" class="button button-ghost">צפה בדמו</a>
  </div>
</article>

<article class="card">
  <h3>🔥 Cyber-Tech</h3>
  <p>עיצוב סייבר-פאנק עם אפקטי ניאון, Matrix rain, ורכיבים אינטראקטיביים. לחובבי האסתטיקה הטכנולוגית.</p>
  <div style="margin-top: 1.5rem;">
    <a href="{{ '/cyber-demo/' | relative_url }}" class="button button-ghost">צפה בדמו</a>
  </div>
</article>

</div>

<div class="divider"></div>

## 📝 פוסטים אחרונים

{% for post in site.posts limit:5 %}
<article style="margin-bottom: 2rem;">
  <h3><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h3>
  <p class="text-muted">{{ post.date | date: "%d.%m.%Y" }}</p>
  {% if post.excerpt %}
  <p>{{ post.excerpt | strip_html | truncate: 200 }}</p>
  {% endif %}
</article>
{% endfor %}

{% if site.posts.size == 0 %}
<p class="text-muted">עדיין אין פוסטים בבלוג. בקרוב...</p>
{% endif %}

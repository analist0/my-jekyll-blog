---
layout: default
title: ארכיון
---

# ארכיון פוסטים

{% for post in site.posts %}
  {% capture current_year %}{{ post.date | date: "%Y" }}{% endcapture %}
  {% if current_year != previous_year %}
    <h2>{{ current_year }}</h2>
    {% assign previous_year = current_year %}
  {% endif %}
  <div style="margin-bottom: 0.5rem;">
    <a href="{{ post.url | relative_url }}">{{ post.title }}</a> - <span style="color: #777;">{{ post.date | date: "%B %d" }}</span>
  </div>
{% endfor %}
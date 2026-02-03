---
layout: default
title: אודות | יוסף אלישר - מפתח Full-Stack
description: יוסף אלישר - מפתח Full-Stack, מומחה AI ואוטומציה. בניית מערכות מתקדמות, פיתוח בינה מלאכותית וכלים טכנולוגיים חדשניים.
---

<section class="hero about-hero" style="min-height: 80vh; position: relative; overflow: hidden;">
  <div class="hero-background breathing-bg"></div>
  <div class="floating-shapes">
    <div class="shape shape-1"></div>
    <div class="shape shape-2"></div>
    <div class="shape shape-3"></div>
  </div>
  <div class="container">
    <div class="hero-content" style="position: relative; z-index: 2;">
      <div class="profile-avatar breathing-glow">
        <span style="font-size: 5rem;">👨‍💻</span>
      </div>
      <h1 class="hero-title gradient-text" style="font-size: clamp(2.5rem, 6vw, 4rem);">
        יוסף אלישר
      </h1>
      <p class="hero-subtitle" style="max-width: 700px; margin: 0 auto 2rem;">
        מפתח Full-Stack | מומחה AI & Automation | יוצר תוכן טכנולוגי
      </p>
      <div class="hero-cta">
        <a href="mailto:Jelyashar@gmail.com" class="btn btn-primary pulse-btn">📧 צור קשר</a>
        <a href="https://github.com/analist0" class="btn btn-secondary" target="_blank">🐙 GitHub</a>
      </div>
    </div>
  </div>
</section>

<section class="section reveal">
  <div class="container">
    <div class="about-grid">

      <div class="about-card glass-card breathing-border">
        <div class="card-icon">🎯</div>
        <h2>קצת עלי</h2>
        <p>
          מפתח תוכנה עם ניסיון של שנים בפיתוח Full-Stack, בינה מלאכותית, אוטומציה ו-DevOps.
          מתמחה בבניית מערכות מורכבות, אינטגרציות API וכלים מבוססי AI.
          אוהב ללמוד טכנולוגיות חדשות ולשתף ידע עם הקהילה.
        </p>
      </div>

      <div class="about-card glass-card breathing-border">
        <div class="card-icon">💻</div>
        <h2>טכנולוגיות</h2>
        <div class="skills-grid">
          <span class="skill-badge skill-python">Python</span>
          <span class="skill-badge skill-js">JavaScript</span>
          <span class="skill-badge skill-node">Node.js</span>
          <span class="skill-badge skill-react">React</span>
          <span class="skill-badge skill-ai">AI/ML</span>
          <span class="skill-badge skill-docker">Docker</span>
          <span class="skill-badge skill-git">Git</span>
          <span class="skill-badge skill-api">REST APIs</span>
          <span class="skill-badge skill-db">PostgreSQL</span>
          <span class="skill-badge skill-cloud">Cloud</span>
        </div>
      </div>

      <div class="about-card glass-card breathing-border">
        <div class="card-icon">🚀</div>
        <h2>התמחויות</h2>
        <ul class="expertise-list">
          <li><span class="emoji">🤖</span> פיתוח מערכות AI ואוטומציה</li>
          <li><span class="emoji">🌐</span> Full-Stack Web Development</li>
          <li><span class="emoji">📊</span> Data Engineering & Analytics</li>
          <li><span class="emoji">⚙️</span> DevOps & CI/CD Pipelines</li>
          <li><span class="emoji">📱</span> Mobile & Responsive Design</li>
        </ul>
      </div>

      <div class="about-card contact-card glass-card breathing-border">
        <div class="card-icon">📞</div>
        <h2>צור קשר</h2>
        <div class="contact-info">
          <a href="mailto:Jelyashar@gmail.com" class="contact-item">
            <span class="contact-icon">📧</span>
            <span>Jelyashar@gmail.com</span>
          </a>
          <a href="tel:+972584423342" class="contact-item">
            <span class="contact-icon">📱</span>
            <span dir="ltr">058-4423342</span>
          </a>
          <a href="https://github.com/analist0" target="_blank" class="contact-item">
            <span class="contact-icon">🐙</span>
            <span>github.com/analist0</span>
          </a>
          <a href="https://twitter.com/analist0" target="_blank" class="contact-item">
            <span class="contact-icon">🐦</span>
            <span>@analist0</span>
          </a>
        </div>
      </div>

    </div>
  </div>
</section>

<section class="section cta-section reveal">
  <div class="container">
    <div class="cta-box glass-card breathing-glow">
      <h2>💡 רוצה לשתף פעולה?</h2>
      <p>אני תמיד פתוח לפרויקטים מעניינים, שיתופי פעולה והזדמנויות חדשות.</p>
      <a href="mailto:Jelyashar@gmail.com" class="btn btn-primary btn-large pulse-btn">
        בואו נדבר! 🚀
      </a>
    </div>
  </div>
</section>

<style>
/* Breathing Animations */
@keyframes breathe {
  0%, 100% { transform: scale(1); opacity: 0.8; }
  50% { transform: scale(1.02); opacity: 1; }
}

@keyframes breathe-glow {
  0%, 100% { box-shadow: 0 0 20px rgba(99, 102, 241, 0.3); }
  50% { box-shadow: 0 0 40px rgba(99, 102, 241, 0.6); }
}

@keyframes breathe-border {
  0%, 100% { border-color: rgba(99, 102, 241, 0.3); }
  50% { border-color: rgba(99, 102, 241, 0.7); }
}

@keyframes float {
  0%, 100% { transform: translateY(0) rotate(0deg); }
  50% { transform: translateY(-20px) rotate(5deg); }
}

@keyframes pulse {
  0%, 100% { transform: scale(1); }
  50% { transform: scale(1.05); }
}

@keyframes gradient-shift {
  0% { background-position: 0% 50%; }
  50% { background-position: 100% 50%; }
  100% { background-position: 0% 50%; }
}

.breathing-bg {
  animation: breathe 4s ease-in-out infinite;
}

.breathing-glow {
  animation: breathe-glow 3s ease-in-out infinite;
}

.breathing-border {
  border: 2px solid rgba(99, 102, 241, 0.3);
  animation: breathe-border 3s ease-in-out infinite;
}

.pulse-btn {
  animation: pulse 2s ease-in-out infinite;
}

.pulse-btn:hover {
  animation: none;
  transform: scale(1.1);
}

/* Gradient Text */
.gradient-text {
  background: linear-gradient(135deg, var(--accent), #8b5cf6, #ec4899);
  background-size: 200% 200%;
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  animation: gradient-shift 3s ease infinite;
}

/* Floating Shapes */
.floating-shapes {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  overflow: hidden;
  pointer-events: none;
}

.shape {
  position: absolute;
  border-radius: 50%;
  background: linear-gradient(135deg, rgba(99, 102, 241, 0.2), rgba(139, 92, 246, 0.2));
  animation: float 6s ease-in-out infinite;
}

.shape-1 {
  width: 200px;
  height: 200px;
  top: 10%;
  left: 10%;
  animation-delay: 0s;
}

.shape-2 {
  width: 150px;
  height: 150px;
  top: 60%;
  right: 10%;
  animation-delay: 2s;
}

.shape-3 {
  width: 100px;
  height: 100px;
  bottom: 20%;
  left: 30%;
  animation-delay: 4s;
}

/* Profile Avatar */
.profile-avatar {
  width: 150px;
  height: 150px;
  margin: 0 auto 2rem;
  border-radius: 50%;
  background: linear-gradient(135deg, var(--accent), #8b5cf6);
  display: flex;
  align-items: center;
  justify-content: center;
}

/* Glass Card */
.glass-card {
  background: rgba(255, 255, 255, 0.05);
  backdrop-filter: blur(10px);
  border-radius: 20px;
  padding: 2rem;
  transition: all 0.3s ease;
}

[data-theme="light"] .glass-card {
  background: rgba(255, 255, 255, 0.8);
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
}

.glass-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 20px 40px rgba(99, 102, 241, 0.2);
}

/* About Grid */
.about-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 2rem;
}

.about-card {
  text-align: center;
}

.card-icon {
  font-size: 3rem;
  margin-bottom: 1rem;
}

.about-card h2 {
  margin-bottom: 1rem;
  color: var(--text-primary);
}

.about-card p {
  color: var(--text-secondary);
  line-height: 1.8;
}

/* Skills Grid */
.skills-grid {
  display: flex;
  flex-wrap: wrap;
  gap: 0.75rem;
  justify-content: center;
}

.skill-badge {
  padding: 0.5rem 1rem;
  border-radius: 20px;
  font-size: 0.875rem;
  font-weight: 600;
  color: white;
  transition: all 0.3s ease;
}

.skill-badge:hover {
  transform: scale(1.1);
}

.skill-python { background: linear-gradient(135deg, #3776AB, #FFD43B); }
.skill-js { background: linear-gradient(135deg, #F7DF1E, #323330); color: #323330; }
.skill-node { background: linear-gradient(135deg, #339933, #68A063); }
.skill-react { background: linear-gradient(135deg, #61DAFB, #282C34); }
.skill-ai { background: linear-gradient(135deg, #FF6F61, #6B5B95); }
.skill-docker { background: linear-gradient(135deg, #2496ED, #003f8c); }
.skill-git { background: linear-gradient(135deg, #F05032, #6e5494); }
.skill-api { background: linear-gradient(135deg, #00D4AA, #0066CC); }
.skill-db { background: linear-gradient(135deg, #336791, #0064a5); }
.skill-cloud { background: linear-gradient(135deg, #FF9900, #232F3E); }

/* Expertise List */
.expertise-list {
  list-style: none;
  padding: 0;
  text-align: right;
}

.expertise-list li {
  padding: 0.75rem 0;
  border-bottom: 1px solid rgba(99, 102, 241, 0.2);
  display: flex;
  align-items: center;
  gap: 0.75rem;
  color: var(--text-secondary);
}

.expertise-list li:last-child {
  border-bottom: none;
}

.expertise-list .emoji {
  font-size: 1.25rem;
}

/* Contact Card */
.contact-info {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.contact-item {
  display: flex;
  align-items: center;
  gap: 1rem;
  padding: 1rem;
  background: rgba(99, 102, 241, 0.1);
  border-radius: 12px;
  color: var(--text-primary);
  text-decoration: none;
  transition: all 0.3s ease;
}

.contact-item:hover {
  background: rgba(99, 102, 241, 0.2);
  transform: translateX(-5px);
}

.contact-icon {
  font-size: 1.5rem;
}

/* CTA Section */
.cta-section {
  padding: 4rem 0;
}

.cta-box {
  text-align: center;
  padding: 3rem;
  max-width: 600px;
  margin: 0 auto;
}

.cta-box h2 {
  margin-bottom: 1rem;
}

.cta-box p {
  color: var(--text-secondary);
  margin-bottom: 2rem;
}

.btn-large {
  padding: 1rem 2.5rem;
  font-size: 1.1rem;
}

/* Hero CTA */
.hero-cta {
  display: flex;
  gap: 1rem;
  justify-content: center;
  flex-wrap: wrap;
}

/* Responsive */
@media (max-width: 768px) {
  .about-grid {
    grid-template-columns: 1fr;
  }

  .profile-avatar {
    width: 120px;
    height: 120px;
  }

  .profile-avatar span {
    font-size: 4rem;
  }
}
</style>

<!-- JSON-LD Structured Data for Person -->
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Person",
  "name": "יוסף אלישר",
  "alternateName": "Yosef Elishar",
  "email": "Jelyashar@gmail.com",
  "telephone": "+972-58-442-3342",
  "url": "https://analist0.github.io/my-jekyll-blog/about",
  "sameAs": [
    "https://github.com/analist0",
    "https://twitter.com/analist0"
  ],
  "jobTitle": "Full-Stack Developer",
  "knowsAbout": ["Python", "JavaScript", "AI", "Machine Learning", "DevOps", "Full-Stack Development"],
  "description": "מפתח Full-Stack, מומחה AI ואוטומציה. בניית מערכות מתקדמות, פיתוח בינה מלאכותית וכלים טכנולוגיים חדשניים."
}
</script>

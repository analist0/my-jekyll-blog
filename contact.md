---
layout: default
title: יצירת קשר
---

# יצירת קשר

מעניין אותך לשאול שאלה, להציע שיתוף פעולה או לספר לי מה אתה חושב על הבלוג? שלח לי הודעה!

<form action="#" method="POST">
  <div style="margin-bottom: 1rem;">
    <label for="name" style="display: block; margin-bottom: 0.5rem;">שם:</label>
    <input type="text" id="name" name="name" required style="width: 100%; padding: 0.5rem;">
  </div>
  
  <div style="margin-bottom: 1rem;">
    <label for="email" style="display: block; margin-bottom: 0.5rem;">אימייל:</label>
    <input type="email" id="email" name="email" required style="width: 100%; padding: 0.5rem;">
  </div>
  
  <div style="margin-bottom: 1rem;">
    <label for="subject" style="display: block; margin-bottom: 0.5rem;">נושא:</label>
    <input type="text" id="subject" name="subject" required style="width: 100%; padding: 0.5rem;">
  </div>
  
  <div style="margin-bottom: 1rem;">
    <label for="message" style="display: block; margin-bottom: 0.5rem;">הודעה:</label>
    <textarea id="message" name="message" rows="5" required style="width: 100%; padding: 0.5rem;"></textarea>
  </div>
  
  <button type="submit" style="background: #0057d9; color: white; padding: 0.7rem 1.5rem; border: none; border-radius: 4px; cursor: pointer;">שלח הודעה</button>
</form>
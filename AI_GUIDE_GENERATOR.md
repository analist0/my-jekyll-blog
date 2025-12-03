# 🤖 AI Repository Guide Generator

מערכת אוטומטית שיוצרת מדריכי התקנה מקצועיים לריפוזים פופולריים של AI/LLM מקומיים.

## 🎯 מה זה עושה?

הסיסטם רץ **3 פעמים ביום** (בוקר, צהריים, ערב) ו:

1. 🔍 **מחפש** את הריפו הכי פופולרי ב-AI/LLM מהשבוע האחרון
2. 📸 **צולם** screenshot של דף הריפו ב-GitHub
3. 🤖 **יוצר** מדריך מקצועי בעברית עם Claude AI
4. 📝 **מפרסם** פוסט חדש בבלוג Jekyll
5. 🚀 **דוחף** ל-GitHub Pages אוטומטית

## ⏰ זמני הרצה

- **08:00** - בוקר ☀️
- **14:00** - צהריים 🌤️
- **20:00** - ערב 🌙

*(זמן ישראל)*

## 🔧 התקנה והגדרה

### שלב 1: הוסף GitHub Secret - Claude API Key

1. קבל API Key מ-Anthropic:
   - לך ל: https://console.anthropic.com/settings/keys
   - צור API Key חדש
   - העתק את המפתח

2. הוסף ל-GitHub Secrets:
   ```
   GitHub Repo → Settings → Secrets and variables → Actions → New repository secret
   ```

   - **Name**: `ANTHROPIC_API_KEY`
   - **Value**: `sk-ant-...` (המפתח שלך)

### שלב 2: אפשר Workflow Permissions

```
GitHub Repo → Settings → Actions → General → Workflow permissions
```

- ✅ בחר: **Read and write permissions**
- ✅ סמן: **Allow GitHub Actions to create and approve pull requests**

### שלב 3: הפעל את ה-Workflow

הוורקפלואו יתחיל לרוץ אוטומטית בזמנים שנקבעו.

אפשר גם להפעיל ידנית:
```
GitHub Repo → Actions → AI Repo Guide Generator → Run workflow
```

## 📁 מבנה הקבצים

```
my-jekyll-blog/
├── .github/
│   └── workflows/
│       └── ai-repo-guide-generator.yml    # GitHub Actions workflow
├── scripts/
│   ├── generate_ai_repo_guide.py          # סקריפט Python ראשי
│   └── requirements.txt                    # תלויות Python
├── _posts/
│   └── YYYY-MM-DD-repo-name-guide.md      # פוסטים שנוצרו
├── assets/
│   └── images/
│       └── repos/
│           └── *.png                       # Screenshots
└── AI_GUIDE_GENERATOR.md                   # התיעוד הזה
```

## 🎨 מה נכלל במדריך?

כל מדריך שנוצר כולל:

### 1. סקירה כללית
- מה זה הפרויקט
- למה הוא חשוב
- מה הוא פותר

### 2. דרישות מערכת
- Python version
- תלויות
- חומרה מומלצת

### 3. התקנה צעד אחר צעד
- 🐧 **Linux/Mac**
- 🪟 **Windows**
- 📱 **Termux/Android**

### 4. הגדרה ראשונית
- קונפיגורציה
- משתני סביבה
- הגדרות ראשוניות

### 5. שימוש בסיסי
- דוגמאות קוד
- פקודות נפוצות
- תרחישי שימוש

### 6. טיפים מתקדמים
- אופטימיזציות
- פיצ'רים מתקדמים
- טריקים

### 7. פתרון בעיות
- בעיות נפוצות
- Troubleshooting
- Debug tips

### 8. משאבים נוספים
- דוקומנטציה רשמית
- קהילה
- מדריכים נוספים

## 🔍 איך זה בוחר ריפוזים?

המערכת מחפשת ריפוזים לפי:

### מילות מפתח:
- `llama`, `ollama`, `local-llm`
- `mistral`, `qwen`, `gemma`, `phi`
- `stable-diffusion`, `whisper`
- `rag`, `vector-database`
- `ai-assistant`, `chatbot`

### קריטריונים:
- ⭐ יותר מ-50 כוכבים
- 📅 עודכן בשבוע האחרון
- 🤖 רלוונטי ל-AI/LLM מקומי
- 🐍 מתמקד ב-Python (אבל לא חובה)

## 🧪 בדיקה מקומית

אם רוצה לבדוק את הסקריפט לפני:

```bash
cd ~/my-jekyll-blog

# התקן תלויות
pip install -r scripts/requirements.txt
playwright install chromium

# הגדר משתני סביבה
export ANTHROPIC_API_KEY="sk-ant-..."
export GITHUB_TOKEN="ghp_..."  # אופציונלי

# הרץ
python scripts/generate_ai_repo_guide.py
```

## 📊 דוגמת Output

```
============================================================
🤖 AI Repository Guide Generator
============================================================

🔍 Searching for trending AI repositories...
✅ Selected repo: ollama/ollama
   ⭐ Stars: 142,583
   📝 Description: Get up and running with Llama 3.3, Mistral...

📸 Capturing screenshot of https://github.com/ollama/ollama...
✅ Screenshot saved to assets/images/repos/ollama-20250203.png

🤖 Generating professional guide with Claude...
✅ Generated 12,457 characters of guide content

📝 Creating Jekyll blog post...
✅ Post created: 2025-02-03-ollama-guide.md

============================================================
✅ Guide generation complete!
📄 Post: _posts/2025-02-03-ollama-guide.md
🖼️  Screenshot: assets/images/repos/ollama-20250203.png
============================================================
```

## 🎯 תכונות מיוחדות

### ✅ מה יש:
- ✨ מדריכים בעברית מקצועית
- 📸 Screenshots אוטומטיים
- 🤖 יצירת תוכן עם Claude Sonnet 4.5
- 🔄 רץ אוטומטית 3 פעמים ביום
- 📱 תמיכה ב-RTL (עברית)
- 🎨 פורמט Jekyll מסודר
- 🏷️ תגים ו-categories אוטומטיים
- 📊 סטטיסטיקות ריפו
- 🔗 לינקים לכל המשאבים

### 🎨 אימוג'ים במדריך:
- 📦 התקנה
- 🚀 הפעלה
- ⚡ ביצועים
- ✅ הצלחה
- ⚠️ אזהרות
- 💡 טיפים
- 🐛 באגים
- 🔧 תיקונים

## 🔒 אבטחה

- ✅ API Keys מאוחסנים ב-GitHub Secrets (מוצפן)
- ✅ לא נשמרים בקוד
- ✅ Workflow permissions מוגבל
- ✅ Rate limiting ל-API calls

## 🐛 פתרון בעיות

### Workflow לא רץ:
```bash
# בדוק Workflow permissions
Settings → Actions → General → Workflow permissions
→ Read and write permissions ✅
```

### API Key לא עובד:
```bash
# ודא ש-Secret נקרא נכון
ANTHROPIC_API_KEY (לא anthropic_api_key)

# בדוק ש-Key תקף ב-Anthropic Console
```

### Screenshot נכשל:
```bash
# Playwright לפעמים דורש timeout יותר ארוך
# הסקריפט מטפל בזה אוטומטית
```

## 📈 שיפורים עתידיים

רעיונות להרחבה:

- [ ] שלח התראה ל-Telegram כשמדריך חדש יוצר
- [ ] תמיכה בשפות נוספות (אנגלית)
- [ ] השוואה בין ריפוזים דומים
- [ ] וידאו הדרכה (קישור ל-YouTube)
- [ ] אינטגרציה עם n8n workflow
- [ ] דירוג איכות הריפו
- [ ] המלצות למשתמש

## 🙏 תודות

- 🤖 **Claude AI** - יצירת המדריכים
- 🐙 **GitHub API** - מציאת ריפוזים
- 🎭 **Playwright** - Screenshots
- 📝 **Jekyll** - מערכת הבלוג

---

**נוצר על ידי**: Yossi (analist0)
**תאריך**: {{ site.time | date: "%d/%m/%Y" }}
**רישיון**: MIT

🚀 **Happy AI Coding!**

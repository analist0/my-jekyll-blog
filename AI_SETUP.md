# 🤖 AI Content Generator - Setup Guide

מערכת פשוטה ומודולרית ליצירת תוכן אוטומטי עם **מפתח אחד**.

## ✨ מה המערכת עושה?

המערכת משתמשת ב-AI API אחד לכל הפונקציות:

### 📦 מודולים:
1. **ניתוח טרנדים** - מזהה נושאים חמים (ללא Twitter API!)
2. **ניתוח סנטימנט** - בודק מה אנשים חושבים על הנושא
3. **יצירת תוכן** - כותב מאמרים מלאים בעברית
4. **יצירת תמונות** - מייצר תמונות (אופציונלי)

## 🔑 הגדרת מפתח API

### שלב 1: קבל מפתח API

בחר ספק אחד:

- **OpenAI** (מומלץ): https://platform.openai.com/api-keys
  - תומך: GPT-4, DALL-E 3
  - עלות: ~$0.01-0.03 למאמר

- **Anthropic (Claude)**: https://console.anthropic.com/
  - תומך: Claude 3.5 Sonnet
  - עלות: ~$0.015 למאמר

- **Google Gemini**: https://ai.google.dev/
  - תומך: Gemini Pro
  - חינם למכסה נדיבה

### שלב 2: הוסף ל-GitHub Secrets

1. לך ל: https://github.com/analist0/my-jekyll-blog/settings/secrets/actions

2. לחץ **"New repository secret"**

3. הוסף:
   ```
   Name: AI_API_KEY
   Value: [המפתח שלך כאן]
   ```

### שלב 3: הגדר את הספק (אופציונלי)

1. לך ל: https://github.com/analist0/my-jekyll-blog/settings/variables/actions

2. הוסף משתנה:
   ```
   Name: AI_PROVIDER
   Value: openai / anthropic / gemini
   ```

3. (אופציונלי) להפעיל יצירת תמונות:
   ```
   Name: GENERATE_IMAGE
   Value: true
   ```

## 🚀 שימוש

### ריצה ידנית:
1. לך ל: https://github.com/analist0/my-jekyll-blog/actions
2. בחר **"Daily AI Content Publisher"**
3. לחץ **"Run workflow"**

### ריצה אוטומטית:
- רץ אוטומטית כל יום ב-9:00 בבוקר (UTC)

## 📁 מבנה הקבצים

```
my-jekyll-blog/
├── ai_content_generator.py      # הסקריפט הראשי
├── .github/
│   └── workflows/
│       └── daily_x_trend_publisher.yml  # ה-workflow
└── _posts/                       # מאמרים שנוצרו
```

## 🔧 התאמה אישית

### שנה נושאים:
ערוך `ai_content_generator.py` - פונקציה `analyze_trends()`:
```python
prompt = f"""
Generate trending topics about: [הנושאים שלך]
"""
```

### שנה סגנון כתיבה:
ערוך `ai_content_generator.py` - פונקציה `generate_article()`:
```python
prompt = f"""
Write in [Hebrew/English] with [casual/professional] tone...
"""
```

## 💰 עלויות משוערות

| ספק | מודל | עלות למאמר | תמונה |
|-----|------|------------|--------|
| OpenAI | GPT-4 | ~$0.02 | +$0.04 (DALL-E 3) |
| Anthropic | Claude 3.5 | ~$0.015 | לא זמין |
| Google | Gemini Pro | חינם* | לא זמין |

*עד למכסה החודשית

## 🆘 פתרון בעיות

### "AI_API_KEY not set"
➡️ ודא שהוספת את המפתח ב-GitHub Secrets

### "Invalid API key"
➡️ בדוק שהמפתח תקין והחשבון פעיל

### "Rate limit exceeded"
➡️ המתן כמה דקות או שדרג את התוכנית

## 📝 דוגמה לריצה מקומית

```bash
# התקן תלויות
pip install requests

# הגדר מפתח
export AI_API_KEY="your-key-here"
export AI_PROVIDER="openai"

# הרץ
python ai_content_generator.py
```

## 🎯 יתרונות המערכת החדשה

✅ **מפתח אחד** במקום 5
✅ **פשוט יותר** - פחות הגדרות
✅ **גמיש יותר** - החלף ספקים בקלות
✅ **זול יותר** - לא צריך Twitter API Elevated
✅ **מודולרי** - קל להוסיף פיצ'רים

---

**צריך עזרה?** פתח issue או שאל!

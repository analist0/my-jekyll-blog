---
layout: unified-post
title: "Automating Identity Verification: Building a Python Telegram Bot for SheerID Authentication with tgbot-verify"
description: "מדריך מקיף ומפורט על Automating Identity Verification: Building a Python Telegram Bot for SheerID Authentication with tgbot-verify. כולל הסברים צעד-אחר-צעד, דוגמאות קוד, שיטות עבודה מומלצות ומקרי שימוש מהעולם האמיתי."
date: 2025-12-09 09:32:20 +0200
categories: ['Tutorial', 'Development']
tags: ['automating', 'identity', 'verification', 'building', 'python', 'telegram']
author: "Tech Insights"
lang: he
---

---
layout: post
title: "אוטומציה של אימות זהות: בניית בוט טלגרם בפייתון לשימוש ב-SheerID עם tgbot-verify"
description: "מדריך מקיף ומפורט לבניית בוט טלגרם בפייתון שמשתמש ב-SheerID לביצוע אימות זהות באמצעות tgbot-verify. כולל דוגמאות קוד, שיטות עבודה מומלצות, מלכודות נפוצות, טכניקות מתקדמות ודוגמאות מהעולם האמיתי."
date: 2023-10-10
author: "מומחה טכני"
categories: [פייתון, טלגרם, אוטומציה, אימות זהות, SheerID, tgbot-verify]
tags: [פייתון, בוט טלגרם, אימות זהות, SheerID, tgbot-verify, אוטומציה]
---

# אוטומציה של אימות זהות: בניית בוט טלגרם בפייתון לשימוש ב-SheerID עם tgbot-verify 📚🤖

## הקדמה

בעולם הדיגיטלי של היום, אימות זהות הוא חלק חיוני בהגנה על אבטחת המידע ובוודאות כי המשתמשים הם מי שהם טוענים להיות. אחת הדרכים הפופולריות לבצע אימות זהות היא באמצעות שירותים כמו SheerID, המאפשרים לבצע אימות זהות בצורה אוטומטית ומאובטחת. כדי להנגיש את התהליך הזה למשתמשי טלגרם, ניתן לבנות בוט טלגרם שמשתמש ב-SheerID לביצוע האימות באמצעות כלי כמו tgbot-verify.

במדריך זה, נלמד כיצד לבנות בוט טלגרם בפייתון שמשתמש ב-SheerID לביצוע אימות זהות באמצעות tgbot-verify. נעבור על כל הצעדים הדרושים, החל מהדרישות המוקדמות ועד לשלבי ההטמעה המתקדמים. נציג דוגמאות קוד, שיטות עבודה מומלצות, מלכודות נפוצות וטכניקות מתקדמות, ונסיים בדוגמאות מהעולם האמיתי ובצעדים הבאים.

## דרישות מוקדמות וכלים נדרשים

לפני שנתחיל בבניית הבוט, עלינו לוודא שיש לנו את כל הכלים והדרישות המוקדמות הבאים:

1. **פייתון 3.7 ומעלה**: הבוט יתבסס על פייתון, ולכן עלינו לוודא שיש לנו גרסה עדכנית של פייתון מותקנת במחשב.
2. **חשבון טלגרם**: נזדקק לחשבון טלגרם כדי ליצור את הבוט.
3. **BotFather**: כלי בטלגרם שמאפשר ליצור בוטים חדשים ולקבל את ה-API Key הדרוש לתקשורת עם הבוט.
4. **חשבון SheerID**: נזדקק לחשבון SheerID כדי להשתמש בשירותי האימות שלהם.
5. **tgbot-verify**: כלי שמאפשר לנו לבצע אימות זהות באמצעות SheerID בתוך הבוט שלנו.
6. **ספריות פייתון**: נשתמש בספריות כמו `python-telegram-bot`, `requests`, ו-`json` כדי לבנות את הבוט.

### התקנת הדרישות

כדי להתקין את הספריות הדרושות, נשתמש בפקודות הבאות:

{% raw %}
```bash
pip install python-telegram-bot requests
```{% raw %}
{% endraw %}

## הטמעה צעד-אחר-צעד עם דוגמאות קוד

בחלק זה נעבור על כל הצעדים הדרושים לבניית הבוט, החל מיצירת הבוט בטלגרם ועד לשילוב של SheerID ו-tgbot-verify בקוד שלנו.

### צעד 1: יצירת הבוט בטלגרם

ראשית, נפתח את האפליקציה של טלגרם ונתחיל שיחה עם BotFather. נשתמש בפקודה {% endraw %}`/newbot` כדי ליצור בוט חדש. נקבל שאלות על שם הבוט ועל שם המשתמש שלו, ולאחר מכן נקבל את ה-API Key הדרוש לנו.

### צעד 2: התחלת קוד הבוט

נתחיל בכתיבת קוד הבוט הבסיסי. נשתמש בספריית `python-telegram-bot` כדי ליצור בוט פשוט שמגיב לפקודות בסיסיות.

{% raw %}
```python
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# הגדרת הלוגינג
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# הגדרת הפונקציה לפקודת /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('שלום! אני בוט טלגרם לאימות זהות. השתמש בפקודה /verify כדי להתחיל.')

# הגדרת הפונקציה לפקודת /help
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('השתמש בפקודה /verify כדי להתחיל את תהליך האימות.')

# הגדרת הפונקציה לפקודת /verify
async def verify(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('תהליך האימות יתחיל בקרוב.')

def main():
    # יצירת האפליקציה עם ה-API Key שלנו
    application = Application.builder().token('YOUR_API_KEY').build()

    # הוספת הפקודות לבוט
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("verify", verify))

    # התחלת הבוט
    application.run_polling()

if __name__ == '__main__':
    main()
```{% raw %}
{% endraw %}

הקוד הזה יוצר בוט בסיסי שמגיב לפקודות {% endraw %}`/start`, `/help`, ו-`/verify`. כמובן, נצטרך להוסיף את הלוגיקה של האימות עצמו.

### צעד 3: שילוב של SheerID ו-tgbot-verify

כדי לשלב את SheerID ו-tgbot-verify בבוט שלנו, נצטרך להוסיף את הלוגיקה הדרושה לביצוע האימות. נתחיל בהוספת הפונקציה שמתחילה את תהליך האימות.

{% raw %}
```python
import requests
import json

# הגדרת הפונקציה לביצוע האימות
async def start_verification(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # שליחת בקשה ל-SheerID כדי להתחיל את תהליך האימות
    url = 'https://api.sheerid.com/rest/v2/verification/start'
    headers = {
        'Authorization': 'Bearer YOUR_SHEERID_API_KEY',
        'Content-Type': 'application/json'
    }
    data = {
        'programId': 'YOUR_PROGRAM_ID',
        'affiliateId': 'YOUR_AFFILIATE_ID',
        'userId': update.effective_user.id
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        verification_id = response.json()['verificationId']
        # שמירת ה-verification_id במשתנה גלובלי או במסד נתונים
        context.user_data['verification_id'] = verification_id

        # שליחת הודעה למשתמש עם הוראות להמשך התהליך
        await update.message.reply_text(f'תהליך האימות התחיל. ה-verification ID שלך הוא: {verification_id}. בבקשה סיים את התהליך באתר של SheerID.')
    else:
        await update.message.reply_text('שגיאה בהתחלת תהליך האימות. אנא נסה שוב מאוחר יותר.')
```
{% endraw %}

הפונקציה הזו מבצעת בקשה ל-SheerID כדי להתחיל את תהליך האימות ושומרת את ה-verification ID במשתנה גלובלי או במסד נתונים.

### צעד 4: שילוב של tgbot-verify

כדי להשתמש ב-tgbot-verify, נצטרך להוסיף את הלוגיקה הדרושה לביצוע האימות בתוך הבוט. נתחיל בהוספת הפונקציה שמבצעת את האימות באמצעות tgbot-verify.

{% raw %}
```python
# הגדרת הפונקציה לביצוע האימות באמצעות tgbot-verify
async def verify_identity(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # בדיקה אם יש verification ID שמור
    if 'verification_id' not in context.user_data:
        await update.message.reply_text('לא נמצא verification ID. אנא התחל את תהליך האימות עם הפקודה /verify.')
        return

    verification_id = context.user_data['verification_id']

    # שליחת בקשה ל-SheerID כדי לבדוק את סטטוס האימות
    url = f'https://api.sheerid.com/rest/v2/verification/{verification_id}/status'
    headers = {
        'Authorization': 'Bearer YOUR_SHEERID_API_KEY',
        'Content-Type': 'application/json'
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        status = response.json()['status']
        if status == 'VERIFIED':
            # ביצוע האימות באמצעות tgbot-verify
            tgbot_verify_url = 'https://tgbot-verify.sheerid.com/verify'
            tgbot_verify_data = {
                'verificationId': verification_id,
                'userId': update.effective_user.id
            }
            tgbot_verify_response = requests.post(tgbot_verify_url, headers=headers, data=json.dumps(tgbot_verify_data))

            if tgbot_verify_response.status_code == 200:
                await update.message.reply_text('אימות זהות בוצע בהצלחה!')
            else:
                await update.message.reply_text('שגיאה בביצוע האימות באמצעות tgbot-verify.')
        else:
            await update.message.reply_text(f'סטטוס האימות: {status}. אנא סיים את התהליך באתר של SheerID.')
    else:
        await update.message.reply_text('שגיאה בבדיקת סטטוס האימות. אנא נסה שוב מאוחר יותר.')
```
{% endraw %}

הפונקציה הזו בודקת את סטטוס האימות ב-SheerID ובמידה והאימות הושלם, היא מבצעת את האימות באמצעות tgbot-verify.

### צעד 5: שילוב הפונקציות בקוד הבוט

כדי לשלב את הפונקציות בקוד הבוט, נצטרך להוסיף אותן לפונקציית ה-main ולשנות את הפונקציה לפקודת /verify כדי להתחיל את תהליך האימות.

{% raw %}
```python
# שינוי הפונקציה לפקודת /verify
async def verify(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await start_verification(update, context)

# שינוי פונקציית ה-main
def main():
    # יצירת האפליקציה עם ה-API Key שלנו
    application = Application.builder().token('YOUR_API_KEY').build()

    # הוספת הפקודות לבוט
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("verify", verify))
    application.add_handler(CommandHandler("check", verify_identity))

    # התחלת הבוט
    application.run_polling()

if __name__ == '__main__':
    main()
```{% raw %}
{% endraw %}

הקוד הזה משלב את הפונקציות החדשות בבוט שלנו ומאפשר למשתמשים להתחיל את תהליך האימות ולבדוק את סטטוס האימות שלהם.

## שיטות עבודה מומלצות וטיפים

בחלק זה נציג מספר שיטות עבודה מומלצות וטיפים שיעזרו לכם לבנות בוט טלגרם מוצלח ומאובטח.

### שיטות עבודה מומלצות

1. **שימוש בלוגינג**: שימוש בלוגינג יאפשר לכם לעקוב אחר פעולות הבוט ולזהות בעיות בזמן אמת. בקוד שלנו השתמשנו בספריית הלוגינג של פייתון כדי לרשום את הפעולות של הבוט.

2. **שימוש בספריות מוכרות**: שימוש בספריות מוכרות ומתוחזקות כמו {% endraw %}`python-telegram-bot` יאפשר לכם לחסוך זמן ולמנוע בעיות אבטחה. הספרייה הזו מטופלת באופן קבוע ומכילה את כל הכלים הדרושים לבניית בוט טלגרם.

3. **שימוש במסד נתונים**: שימוש במסד נתונים יאפשר לכם לשמור מידע על המשתמשים ועל תהליכי האימות שלהם. במקום לשמור את ה-verification ID במשתנה גלובלי, ניתן לשמור אותו במסד נתונים כמו PostgreSQL או MongoDB.

4. **בדיקות יחידה**: ביצוע בדיקות יחידה יאפשר לכם לוודא שהקוד שלכם עובד כמצופה. ניתן לכתוב בדיקות יחידה לפונקציות שונות בבוט כדי לוודא שהן מתפקדות כראוי.

5. **אבטחת מידע**: שמירה על אבטחת המידע היא חשובה מאוד. ניתן להשתמש בשיטות כמו הצפנה של הנתונים ובדיקת SSL כדי לוודא שהמידע של המשתמשים מאובטח.

### טיפים

1. **שימוש בפקודות ברורות**: שימוש בפקודות ברורות ומובנות יאפשר למשתמשים לתקשר עם הבוט בצורה קלה יותר. בקוד שלנו השתמשנו בפקודות כמו `/start`, `/help`, `/verify`, ו-`/check`.

2. **מתן הוראות ברורות**: מתן הוראות ברורות למשתמשים יאפשר להם להבין את תהליך האימות ולבצע אותו בצורה נכונה. בקוד שלנו שלחנו הודעות ברורות למשתמשים עם הוראות להמשך התהליך.

3. **טיפול בשגיאות**: טיפול בשגיאות בצורה נכונה יאפשר למשתמשים לדעת מה קורה כאשר משהו לא עובד כמצופה. בקוד שלנו שלחנו הודעות שגיאה למשתמשים כאשר תהליך האימות לא הצליח.

4. **שימוש ב-API של טלגרם**: שימוש ב-API של טלגרם יאפשר לכם להוסיף פונקציונליות נוספת לבוט שלכם, כמו שליחת תמונות, קבצים, ועוד. ניתן לקרוא את התיעוד של ה-API כדי ללמוד על האפשרויות הזמינות.

5. **התאמה אישית**: התאמה אישית של הבוט לצרכים הספציפיים שלכם תאפשר לכם ליצור חוויה טובה יותר למשתמשים. ניתן להוסיף פונקציות נוספות, כמו שליחת הודעות תזכורת או מתן מידע נוסף למשתמשים.

## מלכודות נפוצות ואיך להימנע מהן

בחלק זה נציג מספר מלכודות נפוצות שעלולות לצוץ במהלך בניית הבוט ונסביר כיצד להימנע מהן.

### מלכודת 1: שגיאות ב-API Key

אחת המלכודות הנפוצות היא שגיאות ב-API Key. אם ה-API Key שלכם לא נכון, הבוט לא יוכל לתקשר עם שרתי טלגרם ולא יפעל כראוי.

**איך להימנע מכך**: ודאו שה-API Key שלכם נכון ושאתם משתמשים בו בצורה נכונה בקוד. ניתן לבדוק את ה-API Key ב-BotFather כדי לוודא שהוא נכון.

### מלכודת 2: בעיות בתקשורת עם SheerID

בעיות בתקשורת עם SheerID עלולות לגרום לכך שהאימות לא יתבצע כראוי. אם השרתים של SheerID לא זמינים או שה-API Key שלכם לא נכון, תהליך האימות ייכשל.

**איך להימנע מכך**: ודאו שה-API Key שלכם ל-SheerID נכון ושהשרתים שלהם זמינים. ניתן לבצע בדיקות קבועות כדי לוודא שהתקשורת עם SheerID מתבצעת כראוי.

### מלכודת 3: בעיות בשמירת ה-verification ID

שמירת ה-verification ID במשתנה גלובלי עלולה לגרום לבעיות אם הבוט מריץ מספר משתמשים בו זמנית. אם שני משתמשים משתמשים בבוט בו זמנית, ה-verification ID שלהם עלול להתערבב.

**איך להימנע מכך**: שימוש במסד נתונים יאפשר לכם לשמור את ה-verification ID של כל משתמש בנפרד ולמנוע בעיות כאלה. ניתן לשמור את ה-verification ID במסד נתונים כמו PostgreSQL או MongoDB.

### מלכודת 4: בעיות בביצוע האימות באמצעות tgbot-verify

בעיות בביצוע האימות באמצעות tgbot-verify עלולות לגרום לכך שהאימות לא יתבצע כראוי. אם השרתים של tgbot-verify לא זמינים או שה-API Key שלכם לא נכון, תהליך האימות ייכשל.

**איך להימנע מכך**: ודאו שה-API Key שלכם ל-tgbot-verify נכון ושהשרתים שלהם זמינים. ניתן לבצע בדיקות קבועות כדי לוודא שהתקשורת עם tgbot-verify מתבצעת כראוי.

### מלכודת 5: בעיות באבטחת המידע

בעיות באבטחת המידע עלולות לגרום לכך שמידע של משתמשים ייחשף לצדדים שלישיים. אם הבוט שלכם לא מאובטח כראוי, מידע רגיש עלול להתגלות.

**איך להימנע מכך**: שימוש בשיטות כמו הצפנה של הנתונים ובדיקת SSL יאפשר לכם לשמור על אבטחת המידע של המשתמשים. ניתן להשתמש בכלים כמו Let's Encrypt כדי לקבל תעודת SSL בחינם.

## טכניקות מתקדמות

בחלק זה נציג מספר טכניקות מתקדמות שתוכלו להשתמש בהן כדי לשפר את הבוט שלכם ולהוסיף לו פונקציונליות נוספת.

### טכניקה 1: שימוש ב-Webhooks

שימוש ב-Webhooks יאפשר לכם לקבל עדכונים בזמן אמת מטלגרם מבלי לרוץ את הבוט באופן קבוע. במקום לרוץ את הבוט באופן קבוע, ניתן להשתמש ב-Webhooks כדי לקבל עדכונים מטלגרם כאשר יש הודעה חדשה.

{% raw %}
```python
# הגדרת הפונקציה לטיפול ב-Webhook
async def webhook_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # טיפול בהודעה
    if update.message:
        await update.message.reply_text('הודעה התקבלה דרך Webhook!')

# הגדרת הפונקציה לרישום ה-Webhook
async def set_webhook():
    # יצירת האפליקציה עם ה-API Key שלנו
    application = Application.builder().token('YOUR_API_KEY').build()

    # רישום ה-Webhook
    await application.bot.set_webhook(url='https://your-domain.com/webhook')

# הגדרת הפונקציה להפעלת ה-Webhook
def main():
    # יצירת האפליקציה עם ה-API Key שלנו
    application = Application.builder().token('YOUR_API_KEY').build()

    # הוספת הפקודות לבוט
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, webhook_handler))

    # התחלת הבוט
    application.run_webhook(
        listen='0.0.0.0',
        port=8443,
        url_path='webhook',
        webhook_url='https://your-domain.com/webhook',
        cert='path/to/cert.pem',
        key='path/to/key.pem'
    )

if __name__ == '__main__':
    import asyncio
    asyncio.run(set_webhook())
    main()
```
{% endraw %}

הקוד הזה מראה כיצד להשתמש ב-Webhooks כדי לקבל עדכונים מטלגרם ולטפל בהודעות בזמן אמת.

### טכניקה 2: שימוש במסד נתונים

שימוש במסד נתונים יאפשר לכם לשמור מידע על המשתמשים ועל תהליכי האימות שלהם. במקום לשמור את ה-verification ID במשתנה גלובלי, ניתן לשמור אותו במסד נתונים כמו PostgreSQL או MongoDB.

{% raw %}
```python
import psycopg2

# הגדרת הפונקציה לשמירת ה-verification ID במסד נתונים
def save_verification_id(user_id, verification_id):
    conn = psycopg2.connect(
        host="localhost",
        database="your_database",
        user="your_username",
        password="your_password"
    )
    cur = conn.cursor()
    cur.execute("INSERT INTO verifications (user_id, verification_id) VALUES (%s, %s)", (user_id, verification_id))
    conn.commit()
    cur.close()
    conn.close()

# הגדרת הפונקציה לקבלת ה-verification ID ממסד הנתונים
def get_verification_id(user_id):
    conn = psycopg2.connect(
        host="localhost",
        database="your_database",
        user="your_username",
        password="your_password"
    )
    cur = conn.cursor()
    cur.execute("SELECT verification_id FROM verifications WHERE user_id = %s", (user_id,))
    verification_id = cur.fetchone()
    cur.close()
    conn.close()
    return verification_id[0] if verification_id else None

# שינוי הפונקציה לביצוע האימות
async def start_verification(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # שליחת בקשה ל-SheerID כדי להתחיל את תהליך האימות
    url = 'https://api.sheerid.com/rest/v2/verification/start'
    headers = {
        'Authorization': 'Bearer YOUR_SHEERID_API_KEY',
        'Content-Type': 'application/json'
    }
    data = {
        'programId': 'YOUR_PROGRAM_ID',
        'affiliateId': 'YOUR_AFFILIATE_ID',
        'userId': update.effective_user.id
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        verification_id = response.json()['verificationId']
        # שמירת ה-verification_id במסד נתונים
        save_verification_id(update.effective_user.id, verification_id)

        # שליחת הודעה למשתמש עם הוראות להמשך התהליך
        await update.message.reply_text(f'תהליך האימות התחיל. ה-verification ID שלך הוא: {verification_id}. בבקשה סיים את התהליך באתר של SheerID.')
    else:
        await update.message.reply_text('שגיאה בהתחלת תהליך האימות. אנא נסה שוב מאוחר יותר.')

# שינוי הפונקציה לביצוע האימות באמצעות tgbot-verify
async def verify_identity(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # בדיקה אם יש verification ID שמור במסד הנתונים
    verification_id = get_verification_id(update.effective_user.id)

    if not verification_id:
        await update.message.reply_text('לא נמצא verification ID. אנא התחל את תהליך האימות עם הפקודה /verify.')
        return

    # שליחת בקשה ל-SheerID כדי לבדוק את סטטוס האימות
    url = f'https://api.sheerid.com/rest/v2/verification/{verification_id}/status'
    headers = {
        'Authorization': 'Bearer YOUR_SHEERID_API_KEY',
        'Content-Type': 'application/json'
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        status = response.json()['status']
        if status == 'VERIFIED':
            # ביצוע האימות באמצעות tgbot-verify
            tgbot_verify_url = 'https://tgbot-verify.sheerid.com/verify'
            tgbot_verify_data = {
                'verificationId': verification_id,
                'userId': update.effective_user.id
            }
            tgbot_verify_response = requests.post(tgbot_verify_url, headers=headers, data=json.dumps(tgbot_verify_data))

            if tgbot_verify_response.status_code == 200:
                await update.message.reply_text('אימות זהות בוצע בהצלחה!')
            else:
                await update.message.reply_text('שגיאה בביצוע האימות באמצעות tgbot-verify.')
        else:
            await update.message.reply_text(f'סטטוס האימות: {status}. אנא סיים את התהליך באתר של SheerID.')
    else:
        await update.message.reply_text('שגיאה בבדיקת סטטוס האימות. אנא נסה שוב מאוחר יותר.')
```
{% endraw %}

הקוד הזה מראה כיצד לשמור את ה-verification ID במסד נתונים ולקבל אותו בחזרה כאשר נדרש.

### טכניקה 3: שימוש ב-Asyncio

שימוש ב-Asyncio יאפשר לכם לטפל בהודעות בצורה אסינכרונית ולשפר את ביצועי הבוט. במקום לטפל בהודעות בצורה סינכרונית, ניתן להשתמש ב-Asyncio כדי לטפל בהודעות בצורה אסינכרונית ולשפר את ביצועי הבוט.

{% raw %}
```python
import asyncio

# הגדרת הפונקציה לטיפול בהודעות בצורה אסינכרונית
async def process_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # טיפול בהודעה
    if update.message:
        await update.message.reply_text('הודעה התקבלה!')

# הגדרת הפונקציה להפעלת הבוט באופן אסינכרוני
async def main():
    # יצירת האפליקציה עם ה-API Key שלנו
    application = Application.builder().token('YOUR_API_KEY').build()

    # הוספת הפקודות לבוט
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, process_message))

    # התחלת הבוט
    await application.run_polling()

if __name__ == '__main__':
    asyncio.run(main())
```{% raw %}
{% endraw %}

הקוד הזה מראה כיצד להשתמש ב-Asyncio כדי לטפל בהודעות בצורה אסינכרונית ולשפר את ביצועי הבוט.

## דוגמאות מהעולם האמיתי

בחלק זה נציג מספר דוגמאות מהעולם האמיתי שבהן ניתן להשתמש בבוט טלגרם לביצוע אימות זהות באמצעות SheerID ו-tgbot-verify.

### דוגמה 1: אימות זהות לשירותי חברה

חברה שמציעה שירותים מקוונים יכולה להשתמש בבוט טלגרם כדי לאמת את זהות הלקוחות שלה. הלקוחות יכולים להתחיל את תהליך האימות בבוט, לסיים אותו באתר של SheerID, ולאחר מכן לבדוק את סטטוס האימות שלהם בבוט.

{% endraw %}```python
# הגדרת הפונקציה לשליחת הודעה לאחר אימות מוצל
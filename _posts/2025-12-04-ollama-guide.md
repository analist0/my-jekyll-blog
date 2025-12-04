---
layout: post
title: "מדריך מקצועי: ollama - Get up and running with OpenAI gpt-oss, DeepSeek-R1, Gemma 3 and other models."
date: 2025-12-04 06:43:42 +0200
categories: [AI, LLM, מדריכים]
tags: [local-ai, llm, installation, go]
image: /assets/images/repos/ollama-20251204.png
author: AI Guide Bot
lang: he
dir: rtl
---

![ollama](/assets/images/repos/ollama-20251204.png)

# 🚀 ollama

**⭐ 157,037 כוכבים | 🔧 Go | 📅 עדכון אחרון: 2025-12-04**

[🔗 קישור לריפו](https://github.com/ollama/ollama) | [⬇️ הורדה](https://github.com/ollama/ollama/archive/refs/heads/main.zip)

---

# 🦙 מדריך התקנה מקיף ל-Ollama - הרצת מודלי AI מקומיים

## 📋 תוכן עניינים
- [סקירה כללית](#סקירה-כללית)
- [דרישות מערכת](#דרישות-מערכת)
- [התקנה צעד אחר צעד](#התקנה-צעד-אחר-צעד)
- [הגדרה ראשונית](#הגדרה-ראשונית)
- [שימוש בסיסי](#שימוש-בסיסי)
- [טיפים מתקדמים](#טיפים-מתקדמים)
- [פתרון בעיות נפוצות](#פתרון-בעיות-נפוצות)
- [משאבים נוספים](#משאבים-נוספים)

---

## 🎯 סקירה כללית

### מה זה Ollama?

**Ollama** היא פלטפורמה מקומית להרצת מודלי שפה גדולים (LLMs) על המחשב האישי שלך, ללא צורך בחיבור לאינטרנט או שירותי ענן. הפרויקט זכה ל-**157,000+ כוכבים** ב-GitHub והפך לסטנדרט דה-פקטו להרצת AI מקומי.

### 🌟 למה Ollama?

- **🔒 פרטיות מלאה** - כל הנתונים נשארים במחשב שלך
- **⚡ מהירות גבוהה** - ללא תלות ברשת או בשרתים חיצוניים
- **💰 ללא עלויות** - אין צורך במנוי או ב-API keys
- **🎨 גמישות מלאה** - תמיכה במגוון רחב של מודלים (Llama, Gemma, DeepSeek-R1 ועוד)
- **🛠️ קל לשימוש** - ממשק פשוט דמוי Docker

### מקרי שימוש אידיאליים

✅ פיתוח יישומי AI מקומיים  
✅ ניתוח מסמכים רגישים  
✅ עבודה ללא חיבור לאינטרנט  
✅ ניסויים ולמידה של מודלי שפה  
✅ בניית chatbots ו-assistants מותאמים אישית

---

## 💻 דרישות מערכת

### דרישות חומרה מינימליות

| רכיב | דרישה מינימלית | מומלץ |
|------|----------------|-------|
| **RAM** | 8GB (למודלים של 7B) | 16GB+ |
| | 16GB (למודלים של 13B) | 32GB+ |
| | 32GB (למודלים של 33B+) | 64GB+ |
| **אחסון** | 10GB פנויים | 50GB+ SSD |
| **מעבד** | CPU מודרני (4 ליבות) | 8+ ליבות |
| **GPU** (אופציונלי) | NVIDIA/AMD עם 4GB+ VRAM | 8GB+ VRAM |

### מערכות הפעלה נתמכות

- ✅ **Linux** (כל הדיסטריביוציות המרכזיות)
- ✅ **macOS** 11 Big Sur ומעלה
- ✅ **Windows** 10/11 (WSL2 מומלץ)
- ✅ **Docker** (על כל פלטפורמה)

### ⚠️ הערות חשובות

- מודלים גדולים יותר דורשים יותר זיכרון (ראה טבלת מודלים)
- GPU מאיץ משמעותית את המהירות אך לא הכרחי
- מומלץ SSD לביצועים אופטימליים

---

## 🚀 התקנה צעד אחר צעד

### 🐧 Linux

#### שיטה 1: התקנה אוטומטית (מומלץ)

```bash
# הורדה והתקנה אוטומטית
curl -fsSL https://ollama.com/install.sh | sh
```

**מה הסקריפט עושה?**
- מזהה את הדיסטריביוציה שלך
- מוריד את הקובץ המתאים
- מגדיר שירות systemd
- מוסיף את ollama ל-PATH

#### שיטה 2: התקנה ידנית (Ubuntu/Debian)

```bash
# 1. הורדת הבינארי
curl -L https://ollama.com/download/ollama-linux-amd64 -o ollama

# 2. הפיכתו לקובץ הפעלה
chmod +x ollama

# 3. העברה לתיקיית מערכת
sudo mv ollama /usr/local/bin/

# 4. יצירת משתמש מערכת
sudo useradd -r -s /bin/false -m -d /usr/share/ollama ollama

# 5. יצירת קובץ שירות systemd
sudo tee /etc/systemd/system/ollama.service > /dev/null <<EOF
[Unit]
Description=Ollama Service
After=network-online.target

[Service]
ExecStart=/usr/local/bin/ollama serve
User=ollama
Group=ollama
Restart=always
RestartSec=3

[Install]
WantedBy=default.target
EOF

# 6. הפעלת השירות
sudo systemctl daemon-reload
sudo systemctl enable ollama
sudo systemctl start ollama
```

#### אימות ההתקנה

```bash
# בדיקת גרסה
ollama --version

# בדיקת סטטוס השירות
systemctl status ollama

# בדיקת חיבור לשרת
curl http://localhost:11434
```

---

### 🍎 macOS

#### התקנה

```bash
# 1. הורדת קובץ ההתקנה
curl -L https://ollama.com/download/Ollama.dmg -o Ollama.dmg

# 2. פתיחת קובץ ה-DMG
open Ollama.dmg
```

**או באמצעות Homebrew:**

```bash
# התקנה דרך Homebrew
brew install ollama

# הפעלת השירות
brew services start ollama
```

#### אימות

```bash
# בדיקה ש-Ollama פועל
ollama --version

# הרצת מודל ראשון
ollama run gemma3:1b
```

---

### 🪟 Windows

#### שיטה 1: מתקין רשמי (מומלץ למתחילים)

1. **הורדה:**
   ```
   https://ollama.com/download/OllamaSetup.exe
   ```

2. **התקנה:**
   - הפעל את הקובץ שהורדת
   - עקוב אחר אשף ההתקנה
   - Ollama יתווסף אוטומטית ל-PATH

3. **אימות:**
   ```powershell
   # פתח PowerShell או CMD
   ollama --version
   ```

#### שיטה 2: WSL2 (מומלץ למתקדמים)

```bash
# 1. הפעל WSL2 עם Ubuntu
wsl --install

# 2. בתוך WSL, התקן Ollama
curl -fsSL https://ollama.com/install.sh | sh

# 3. הפעל את השירות
ollama serve
```

**יתרונות WSL2:**
- ביצועים טובים יותר למודלים גדולים
- תאימות מלאה למערכת Linux
- תמיכה טובה יותר ב-GPU (עם CUDA)

---

### 🐳 Docker

#### התקנה בסיסית

```bash
# הרצת Ollama בקונטיינר
docker run -d -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama
```

#### עם תמיכת GPU (NVIDIA)

```bash
# התקן NVIDIA Container Toolkit תחילה
# https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html

# הרצה עם GPU
docker run -d --gpus=all -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama
```

#### Docker Compose (מומלץ לפרויקטים)

```yaml
# docker-compose.yml
version: '3.8'

services:
  ollama:
    image: ollama/ollama:latest
    container_name: ollama
    ports:
      - "11434:11434"
    volumes:
      - ollama_data:/root/.ollama
    restart: unless-stopped
    # הוספת GPU (אופציונלי)
    deploy:
      resources:
        reservations:
          devices:
            - driver: nvidia
              count: all
              capabilities: [gpu]

volumes:
  ollama_data:
```

```bash
# הפעלה
docker-compose up -d

# צפייה בלוגים
docker-compose logs -f
```

---

### 📱 Termux (Android)

> ⚠️ **שים לב:** ביצועים מוגבלים, מתאים רק למודלים קטנים (1B-3B)

```bash
# 1. התקן Termux מ-F-Droid (לא מ-Play Store)

# 2. עדכון חבילות
pkg update && pkg upgrade

# 3. התקנת תלויות
pkg install wget proot-distro

# 4. התקנת Ubuntu בתוך Termux
proot-distro install ubuntu
proot-distro login ubuntu

# 5. בתוך Ubuntu, התקן Ollama
curl -fsSL https://ollama.com/install.sh | sh

# 6. הרצה
ollama serve &
ollama run gemma3:1b
```

---

## ⚙️ הגדרה ראשונית

### הורדת המודל הראשון

```bash
# מודל קל ומהיר ללמידה (815MB)
ollama pull gemma3:1b

# מודל מאוזן (3.3GB)
ollama pull gemma3

# מודל חזק לעברית (4.7GB)
ollama pull llama3.1
```

### 🔧 הגדרות סביבה

#### שינוי תיקיית אחסון המודלים

```bash
# Linux/Mac - הוסף ל-~/.bashrc או ~/.zshrc
export OLLAMA_MODELS="/path/to/your/models"

# Windows - הגדר משתנה סביבה
setx OLLAMA_MODELS "C:\path\to\models"
```

#### שינוי פורט השרת

```bash
# הגדרת פורט אחר (ברירת מחדל: 11434)
export OLLAMA_HOST="0.0.0.0:8080"

# הפעלה מחדש של השירות
sudo systemctl restart ollama  # Linux
brew services restart ollama   # macOS
```

#### הגבלת שימוש בזיכרון

```bash
# הגבלת שימוש ב-RAM (בגיגה-בייטים)
export OLLAMA_MAX_LOADED_MODELS=1
export OLLAMA_NUM_PARALLEL=1
```

### 🎨 התאמת מודל אישי (Modelfile)

צור קובץ `Modelfile`:

```dockerfile
# Modelfile - דוגמה למודל מותאם
FROM llama3.1

# הגדרת פרמטרים
PARAMETER temperature 0.7
PARAMETER top_p 0.9
PARAMETER top_k 40

# הגדרת הקשר מערכת בעברית
SYSTEM """
אתה עוזר AI ידידותי ומועיל שמדבר עברית בצורה טבעית.
אתה עונה בתמציתיות ובבהירות, ומספק דוגמאות כשצריך.
"""
```

יצירת המודל המותאם:

```bash
# יצירת מודל חדש
ollama create my-hebrew-assistant -f Modelfile

# הרצה
ollama run my-hebrew-assistant
```

---

## 📖 שימוש בסיסי

### ממשק שורת פקודה (CLI)

#### שיחה אינטראקטיבית

```bash
# הרצת מודל במצב שיחה
ollama run gemma3

# דוגמת שיחה:
>>> מה זה בינה מלאכותית?
בינה מלאכותית היא תחום במדעי המחשב...

>>> /bye  # יציאה מהשיחה
```

#### פקודות שימושיות בשיחה

```
/help           - הצגת עזרה
/bye או /exit  - יציאה
/clear          - ניקוי מסך
/save <שם>      - שמירת שיחה
/load <שם>      - טעינת שיחה
```

#### שאילתה חד-פעמית

```bash
# שליחת הודעה בודדת
echo "כתוב שיר קצר על הים" | ollama run gemma3

# עם redirect של פלט
ollama run gemma3 "סכם את הטקסט הבא: $(cat document.txt)" > summary.txt
```

### 🔧 פקודות ניהול

```bash
# רשימת כל המודלים המותקנים
ollama list

# מחיקת מודל
ollama rm llama3.1

# הצגת מידע על מודל
ollama show gemma3

# עצירת שרת
pkill ollama  # Linux/Mac
taskkill /F /IM ollama.exe  # Windows
```

---

## 🐍 שימוש בספריות תכנות

### Python

#### התקנה

```bash
pip install ollama
```

#### דוגמאות קוד

**דוגמה בסיסית:**

```python
import ollama

# שליחת שאילתה פשוטה
response = ollama.chat(
    model='gemma3',
    messages=[
        {
            'role': 'user',
            'content': 'מה זה Python?'
        }
    ]
)

print(response['message']['content'])
```

**שיחה עם הקשר:**

```python
import ollama

messages = []

def chat(user_input):
    # הוספת הודעת משתמש
    messages.append({
        'role': 'user',
        'content': user_input
    })
    
    # קבלת תשובה
    response = ollama.chat(
        model='gemma3',
        messages=messages
    )
    
    # הוספת תשובת המודל להיסטוריה
    messages.append({
        'role': 'assistant',
        'content': response['message']['content']
    })
    
    return response['message']['content']

# שימוש
print(chat("היי, מה שלומך?"))
print(chat("תוכל לעזור לי עם Python?"))
```

**Streaming (תשובה בזמן אמת):**

```python
import ollama

stream = ollama.chat(
    model='gemma3',
    messages=[{'role': 'user', 'content': 'כתוב סיפור קצר'}],
    stream=True
)

for chunk in stream:
    print(chunk['message']['content'], end='', flush=True)
```

**יצירת embeddings:**

```python
import ollama

# המרת טקסט לווקטור
embeddings = ollama.embeddings(
    model='nomic-embed-text',
    prompt='זהו טקסט לדוגמה'
)

print(embeddings['embedding'])  # רשימה של מספרים
```

---

### JavaScript/Node.js

#### התקנה

```bash
npm install ollama
```

#### דוגמאות קוד

**דוגמה בסיסית:**

```javascript
import ollama from 'ollama';

async function main() {
  const response = await ollama.chat({
    model: 'gemma3',
    messages: [
      { role: 'user', content: 'מה זה JavaScript?' }
    ]
  });
  
  console.log(response.message.content);
}

main();
```

**Streaming:**

```javascript
import ollama from 'ollama';

async function streamChat() {
  const stream = await ollama.chat({
    model: 'gemma3',
    messages: [{ role: 'user', content: 'ספר לי בדיחה' }],
    stream: true
  });

  for await (const chunk of stream) {
    process.stdout.write(chunk.message.content);
  }
}

streamChat();
```

---

### 🌐 REST API

Ollama מספק REST API מלא:

#### גנרציה בסיסית

```bash
curl http://localhost:11434/api/generate -d '{
  "model": "gemma3",
  "prompt": "מדוע השמיים כחולים?",
  "stream": false
}'
```

#### שיחה עם הקשר

```bash
curl http://localhost:11434/api/chat -d '{
  "model": "gemma3",
  "messages": [
    {
      "role": "system",
      "content": "אתה מומחה לפיזיקה"
    },
    {
      "role": "user",
      "content": "הסבר על אור"
    }
  ],
  "stream": false
}'
```

#### Python עם requests

```python
import requests
import json

def ollama_generate(prompt, model="gemma3"):
    url = "http://localhost:11434/api/generate"
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False
    }
    
    response = requests.post(url, json=payload)
    return response.json()['response']

# שימוש
result = ollama_generate("מה זה למידת מכונה?")
print(result)
```

---

## 🚀 טיפים מתקדמים

### ⚡ אופטימיזציה לביצועים

#### 1. שימוש ב-GPU

```bash
# ודא שיש לך CUDA מותקן (NVIDIA)
nvidia-smi

# Ollama יזהה אוטומטית את ה-GPU
# לאימות, בדוק בלוגים:
journalctl -u ollama -f

# צפוי לראות: "Using NVIDIA GPU"
```

#### 2. בחירת quantization נכון

מודלים מגיעים בגרסאות quantization שונות:

| Quantization | גודל | איכות | מהירות | מתי להשתמש |
|--------------|------|-------|--------|------------|
| **Q4_0** | קטן מאוד | סבירה | מהירה מאוד | RAM מוגבל |
| **Q5_K_M** | בינוני | טובה | מהירה | מאוזן (מומלץ) |
| **Q6_K** | גדול יותר | מצוינת | בינונית | יש הרבה RAM |
| **F16** | הכי גדול | מושלמת | איטית | GPU חזק |

```bash
# דוגמה: הורדת מודל בגרסה ממוטבת
ollama pull llama3.1:8b-q5_k_m
```

#### 3. ניהול זיכרון יעיל

```bash
# הגבל מספר מודלים בזיכרון בו-זמנית
export OLLAMA_MAX_LOADED_MODELS=1

# הגדר timeout לפריקת מודלים (בדקות)
export OLLAMA_KEEP_ALIVE=5m

# השבת keep-alive לחלוטין (פריקה מיידית)
export OLLAMA_KEEP_ALIVE=0
```

#### 4. שימוש במחשבים מרוחקים

```bash
# במחשב השרת:
OLLAMA_HOST=0.0.0.0:11434 ollama serve

# במחשב הלקוח:
export OLLAMA_HOST=http://192.168.1.100:11434
ollama list  # רשימת מודלים מהשרת המרוחק
```

---

### 🎨 יצירת Modelfiles מתקדמים

#### מודל עם פרסונה

```dockerfile
FROM llama3.1

# פרמטרים ליצירתיות
PARAMETER temperature 1.2
PARAMETER top_p 0.95
PARAMETER repeat_penalty 1.1

SYSTEM """
אתה סופר מפורסם בשם ירון שמתמחה בסיפורים מופרכים.
אתה כותב בסגנון הומוריסטי ודמיוני.
תמיד מתחיל סיפורים ב"פעם אחת..."
"""

TEMPLATE """
{{ .System }}

סופר: {{ .Prompt }}
"""
```

#### מודל לקוד תכנות

```dockerfile
FROM codellama

PARAMETER temperature 0.2
PARAMETER top_k 10

SYSTEM """
אתה מתכנת מומחה. אתה עונה רק בקוד תקין וממוטב.
לפני כל קוד, תכתוב הסבר קצר בשורה אחת.
"""
```

שמירה והרצה:

```bash
ollama create code-expert -f Modelfile
ollama run code-expert "כתוב פונקציה למיון בועות ב-Python"
```

---

### 🔐 התאמה למסמכים מקומיים (RAG)

**RAG** = Retrieval-Augmented Generation

```python
import ollama
import os

def read_documents(folder_path):
    """קריאת כל המסמכים מתיקייה"""
    documents = []
    for filename in os.listdir(folder_path):
        if filename.endswith('.txt'):
            with open(os.path.join(folder_path, filename), 'r', encoding='utf-8') as f:
                documents.append(f.read())
    return documents

def create_context(documents, query):
    """יצירת הקשר רלוונטי"""
    # כאן אפשר להוסיף חיפוש מתקדם יותר
    context = "\n\n".join(documents[:3])  # 3 מסמכים ראשונים
    return context

def rag_query(query, documents_folder):
    """שאילתה עם RAG"""
    docs = read_documents(documents_folder)
    context = create_context(docs, query)
    
    prompt = f"""
    בהתבסס על המסמכים הבאים:
    
    {context}
    
    שאלה: {query}
    
    תשובה:
    """
    
    response = ollama.generate(
        model='gemma3',
        prompt=prompt
    )
    
    return response['response']

# שימוש
answer = rag_query(
    "מה המדיניות לגבי חופשות?",
    "./company_docs"
)
print(answer)
```

---

### 📊 ניטור ביצועים

```python
import ollama
import time

def benchmark_model(model, prompt, runs=5):
    """בדיקת ביצועי מודל"""
    times = []
    
    for i in range(runs):
        start = time.time()
        ollama.generate(model=model, prompt=prompt)
        elapsed = time.time() - start
        times.append(elapsed)
        print(f"ריצה {i+1}: {elapsed:.2f} שניות")
    
    avg_time = sum(times) / len(times)
    print(f"\nממוצע: {avg_time:.2f} שניות")
    print(f"מהיר ביותר: {min(times):.2f} שניות")
    print(f"איטי ביותר: {max(times):.2f} שניות")

# שימוש
benchmark_model(
    model='gemma3:1b',
    prompt='כתוב משפט קצר על מזג האוויר'
)
```

---

## 🛠️ פתרון בעיות נפוצות

### ❌ שגיאה: "connection refused"

**סיבה:** השרת לא רץ

**פתרון:**

```bash
# Linux
sudo systemctl start ollama
sudo systemctl status ollama

# macOS
brew services start ollama

# Windows - הרץ מחדש את האפליקציה או:
ollama serve
```

---

### ❌ שגיאה: "out of memory"

**סיבה:** המודל גדול מדי ל-RAM

**פתרונות:**

```bash
# 1. השתמש במודל קטן יותר
ollama pull gemma3:1b  # במקום gemma3:27b

# 2. השתמש ב-quantization נמוך יותר
ollama pull llama3.1:8b-q4_0  # במקום q6_k

# 3. סגור יישומים אחרים

# 4. הגדל swap (Linux)
sudo fallocate -l 8G /swapfile
sudo chmod 600 /swapfile
sudo mkswap /swapfile
sudo swapon /swapfile
```

---

### ❌ שגיאה: "model not found"

**פתרון:**

```bash
# ודא שהמודל מותקן
ollama list

# אם לא, הורד אותו
ollama pull gemma3

# בדוק איות שם המודל (case-sensitive)
ollama run gemma3  # ולא Gemma3
```

---

### ❌ תגובות איטיות מאוד

**אבחון:**

```bash
# בדוק שימוש ב-CPU
htop  # Linux/Mac
# Task Manager  # Windows

# בדוק אם GPU מזוהה
nvidia-smi  # NVIDIA
rocm-smi    # AMD

# בדוק לוגים
journalctl -u ollama -n 50  # Linux
```

**פתרונות:**

1. **ודא שימוש ב-GPU:**
   ```bash
   # התקן CUDA drivers
   # ראה: https://developer.nvidia.com/cuda-downloads
   
   # אימות
   nvidia-smi
   ```

2. **השתמש במודל קל יותר:**
   ```bash
   ollama pull phi4-mini  # 3.8B - מהיר מאוד
   ```

3. **הפחת הגדרות איכות:**
   ```python
   ollama.generate(
       model='gemma3',
       prompt='...',
       options={
           'num_ctx': 2048,  # הקטן הקשר (ברירת מחדל: 4096)
           'num_predict': 100  # הגבל אורך תשובה
       }
   )
   ```

---

### ❌ בעיות עם עברית

**תסמינים:** טקסט משובש, תווים לא קריאים

**פתרון:**

```python
# ודא encoding נכון ב-Python
import sys
sys.stdout.reconfigure(encoding='utf-8')

# או בשורת פקודה:
export PYTHONIOENCODING=utf-8  # Linux/Mac
chcp 65001  # Windows CMD
```

**בחירת מודל טוב לעברית:**

```bash
# מומלץ:
ollama pull llama3.1       # תמיכה מצוינת
ollama pull gemma3         # תמיכה טובה
ollama pull qwq            # תמיכה טובה

# פחות מומלץ:
ollama pull mistral  # תמיכה חלקית בעברית
```

---

### ❌ שגיאה: "invalid model file"

**פתרון:**

```bash
# מחק מ

---

## 📊 סטטיסטיקות הפרויקט

- **כוכבים**: 157,037 ⭐
- **Forks**: 13,822 🔱
- **Issues**: 2,316 🐛
- **שפה**: Go 💻
- **רישיון**: MIT License 📜

## 🔗 קישורים שימושיים

- [ריפו ב-GitHub](https://github.com/ollama/ollama)
- [Issues & תמיכה](https://github.com/ollama/ollama/issues)
- [Discussions](https://github.com/ollama/ollama/discussions)
- [Wiki](https://github.com/ollama/ollama/wiki)

---

*מדריך זה נוצר אוטומטית על ידי AI Guide Bot עם Claude AI*
*עדכון אחרון: 04/12/2025 06:43*

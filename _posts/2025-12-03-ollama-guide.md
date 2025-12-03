---
layout: post
title: "מדריך מקצועי: ollama - Get up and running with OpenAI gpt-oss, DeepSeek-R1, Gemma 3 and other models."
date: 2025-12-03 18:58:45 +0200
categories: [AI, LLM, מדריכים]
tags: [local-ai, llm, installation, go]
image: /assets/images/repos/ollama-20251203.png
author: AI Guide Bot
lang: he
dir: rtl
---

![ollama](/assets/images/repos/ollama-20251203.png)

# 🚀 ollama

**⭐ 156,999 כוכבים | 🔧 Go | 📅 עדכון אחרון: 2025-12-03**

[🔗 קישור לריפו](https://github.com/ollama/ollama) | [⬇️ הורדה](https://github.com/ollama/ollama/archive/refs/heads/main.zip)

---

# 🦙 מדריך התקנה מקיף ל-Ollama - הרצת מודלי AI מקומית

## 📋 תוכן עניינים
1. [סקירה כללית](#סקירה-כללית)
2. [דרישות מערכת](#דרישות-מערכת)
3. [התקנה צעד אחר צעד](#התקנה-צעד-אחר-צעד)
4. [הגדרה ראשונית](#הגדרה-ראשונית)
5. [שימוש בסיסי](#שימוש-בסיסי)
6. [טיפים מתקדמים](#טיפים-מתקדמים)
7. [פתרון בעיות נפוצות](#פתרון-בעיות-נפוצות)
8. [משאבים נוספים](#משאבים-נוספים)

---

## 🎯 סקירה כללית

### מה זה Ollama?

**Ollama** היא פלטפורמה מקומית להרצת מודלי שפה גדולים (LLM) על המחשב האישי שלך. עם למעלה מ-**156,000 כוכבים** ב-GitHub, זהו הכלי המוביל להרצת AI באופן פרטי ומקומי.

### 🌟 יתרונות מרכזיים

- **🔒 פרטיות מלאה** - כל הנתונים נשארים במחשב שלך
- **⚡ ביצועים מהירים** - אין תלות בחיבור אינטרנט
- **💰 חינמי לחלוטין** - ללא עלויות API
- **🎨 התאמה אישית** - יכולת להתאים מודלים לצרכים שלך
- **🔌 אינטגרציה פשוטה** - ספריות Python ו-JavaScript

### למי זה מיועד?

✅ מפתחים שרוצים לשלב AI באפליקציות  
✅ חוקרים שזקוקים לפרטיות מלאה  
✅ חובבי AI שרוצים להתנסות במודלים שונים  
✅ ארגונים עם דרישות אבטחת מידע מחמירות

---

## 💻 דרישות מערכת

### דרישות חומרה מינימליות

#### מודלים קטנים (1B-7B פרמטרים)
- **RAM**: 8GB מינימום
- **אחסון**: 10GB פנויים
- **מעבד**: Intel i5/AMD Ryzen 5 או טוב יותר
- **GPU** (אופציונלי): NVIDIA עם 4GB VRAM

#### מודלים בינוניים (13B-33B פרמטרים)
- **RAM**: 16GB מינימום
- **אחסון**: 30GB פנויים
- **מעבד**: Intel i7/AMD Ryzen 7
- **GPU** (מומלץ): NVIDIA עם 8GB VRAM

#### מודלים גדולים (70B+ פרמטרים)
- **RAM**: 32GB ומעלה
- **אחסון**: 100GB+ פנויים
- **מעבד**: Intel i9/AMD Ryzen 9
- **GPU** (הכרחי): NVIDIA RTX 3090/4090 או A100

### ⚠️ הערות חשובות

> **שימו לב**: הרצת מודלים על CPU בלבד אפשרית אך תהיה **איטית משמעותית**. מומלץ מאוד GPU של NVIDIA עם תמיכת CUDA.

### מערכות הפעלה נתמכות

- 🍎 **macOS** 11 Big Sur ומעלה (Intel ו-Apple Silicon)
- 🪟 **Windows** 10/11 (64-bit)
- 🐧 **Linux** - רוב ההפצות (Ubuntu, Debian, Fedora, Arch וכו')
- 🐳 **Docker** - כל פלטפורמה עם Docker

---

## 🚀 התקנה צעד אחר צעד

### 🍎 macOS

#### שיטה 1: התקנה גרפית (מומלץ למתחילים)

1. **הורדת הקובץ**
   ```bash
   # גשו לדפדפן והורידו את הקובץ
   # או השתמשו ב-curl:
   curl -L https://ollama.com/download/Ollama.dmg -o Ollama.dmg
   ```

2. **התקנה**
   - פתחו את הקובץ `Ollama.dmg`
   - גררו את Ollama לתיקיית Applications
   - פתחו את Ollama מה-Launchpad

3. **אימות ההתקנה**
   ```bash
   # פתחו Terminal ובדקו:
   ollama --version
   ```

#### שיטה 2: התקנה דרך Homebrew

```bash
# אם אין לכם Homebrew, התקינו אותו תחילה:
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# התקנת Ollama
brew install ollama

# הפעלת השירות
brew services start ollama
```

### 🪟 Windows

#### התקנה סטנדרטית

1. **הורדה והתקנה**
   ```powershell
   # הורידו את הקובץ או השתמשו ב-PowerShell:
   Invoke-WebRequest -Uri "https://ollama.com/download/OllamaSetup.exe" -OutFile "OllamaSetup.exe"
   
   # הרצת ההתקנה
   .\OllamaSetup.exe
   ```

2. **עקבו אחר אשף ההתקנה**
   - לחצו Next/Install
   - בחרו את תיקיית ההתקנה (ברירת מחדל: `C:\Program Files\Ollama`)
   - המתינו לסיום ההתקנה

3. **אימות**
   ```powershell
   # פתחו PowerShell או CMD
   ollama --version
   ```

#### ⚙️ הגדרת GPU ב-Windows

```powershell
# בדיקת תמיכת CUDA (לבעלי כרטיסי NVIDIA)
nvidia-smi

# אם הפקודה עובדת, Ollama יזהה אוטומטית את ה-GPU
# אחרת, התקינו את NVIDIA CUDA Toolkit:
# https://developer.nvidia.com/cuda-downloads
```

### 🐧 Linux

#### שיטה 1: סקריפט התקנה אוטומטי (מומלץ)

```bash
# התקנה בפקודה אחת
curl -fsSL https://ollama.com/install.sh | sh

# הפעלת השירות
sudo systemctl start ollama
sudo systemctl enable ollama  # הפעלה אוטומטית בעת אתחול
```

#### שיטה 2: התקנה ידנית (למתקדמים)

```bash
# 1. הורדת הקובץ הבינארי
curl -L https://ollama.com/download/ollama-linux-amd64 -o ollama
chmod +x ollama
sudo mv ollama /usr/local/bin/

# 2. יצירת משתמש מערכת
sudo useradd -r -s /bin/false -m -d /usr/share/ollama ollama

# 3. יצירת קובץ systemd service
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
Environment="PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"

[Install]
WantedBy=default.target
EOF

# 4. הפעלת השירות
sudo systemctl daemon-reload
sudo systemctl enable ollama
sudo systemctl start ollama
```

#### 🎮 הגדרת GPU ב-Linux (NVIDIA)

```bash
# התקנת NVIDIA Container Toolkit (אם משתמשים ב-Docker)
distribution=$(. /etc/os-release;echo $ID$VERSION_ID)
curl -s -L https://nvidia.github.io/libnvidia-container/gpgkey | sudo apt-key add -
curl -s -L https://nvidia.github.io/libnvidia-container/$distribution/libnvidia-container.list | \
  sudo tee /etc/apt/sources.list.d/nvidia-container-toolkit.list

sudo apt-get update
sudo apt-get install -y nvidia-container-toolkit

# אימות
nvidia-smi
```

#### 🎯 Ubuntu/Debian - התקנה מהירה

```bash
# עדכון המערכת
sudo apt update && sudo apt upgrade -y

# התקנת תלויות
sudo apt install -y curl

# התקנת Ollama
curl -fsSL https://ollama.com/install.sh | sh

# בדיקת סטטוס
sudo systemctl status ollama
```

#### 🔴 Fedora/RHEL - התקנה מהירה

```bash
# עדכון המערכת
sudo dnf update -y

# התקנת Ollama
curl -fsSL https://ollama.com/install.sh | sh

# בדיקת סטטוס
sudo systemctl status ollama
```

### 🐳 Docker

#### שיטה 1: Docker רגיל (CPU בלבד)

```bash
# הרצת Ollama כקונטיינר
docker run -d \
  -v ollama:/root/.ollama \
  -p 11434:11434 \
  --name ollama \
  ollama/ollama

# אימות
docker ps | grep ollama
```

#### שיטה 2: Docker עם GPU (NVIDIA)

```bash
# הרצה עם תמיכת GPU
docker run -d \
  --gpus=all \
  -v ollama:/root/.ollama \
  -p 11434:11434 \
  --name ollama \
  ollama/ollama

# בדיקת גישה ל-GPU
docker exec ollama nvidia-smi
```

#### 📦 Docker Compose

צרו קובץ `docker-compose.yml`:

```yaml
version: '3.8'

services:
  ollama:
    image: ollama/ollama:latest
    container_name: ollama
    ports:
      - "11434:11434"
    volumes:
      - ollama_data:/root/.ollama
    # הסירו את ההערה למחשבים עם GPU
    # deploy:
    #   resources:
    #     reservations:
    #       devices:
    #         - driver: nvidia
    #           count: all
    #           capabilities: [gpu]
    restart: unless-stopped

volumes:
  ollama_data:
```

```bash
# הפעלה
docker-compose up -d

# בדיקת לוגים
docker-compose logs -f ollama
```

### 📱 Termux (Android)

> ⚠️ **שימו לב**: הרצת Ollama על אנדרואיד דורשת מכשיר חזק (8GB+ RAM) והיא **ניסיונית**.

```bash
# 1. התקנת Termux מ-F-Droid (לא מ-Play Store!)
# https://f-droid.org/en/packages/com.termux/

# 2. עדכון חבילות
pkg update && pkg upgrade -y

# 3. התקנת תלויות
pkg install -y proot-distro

# 4. התקנת Ubuntu בתוך Termux
proot-distro install ubuntu
proot-distro login ubuntu

# 5. כעת בתוך Ubuntu, הריצו:
apt update && apt install -y curl
curl -fsSL https://ollama.com/install.sh | sh

# 6. הפעלת Ollama
ollama serve &
```

---

## ⚙️ הגדרה ראשונית

### בדיקת התקנה תקינה

```bash
# בדיקת גרסה
ollama --version

# בדיקת חיבור לשרת
curl http://localhost:11434/api/version
```

**פלט צפוי:**
```json
{"version":"0.1.XX"}
```

### הורדת המודל הראשון

```bash
# הורדת Gemma 3 (מודל קטן וטוב למתחילים - 815MB)
ollama pull gemma3:1b

# הורדת DeepSeek-R1 (מודל מצוין לחשיבה - 4.7GB)
ollama pull deepseek-r1

# הורדת Llama 3.2 (מודל מאוזן - 2GB)
ollama pull llama3.2
```

### 📊 הצגת מודלים מותקנים

```bash
# רשימת כל המודלים במחשב
ollama list
```

**פלט לדוגמה:**
```
NAME              ID              SIZE    MODIFIED
gemma3:1b        abc123def456     815 MB  2 hours ago
deepseek-r1      789ghi012jkl     4.7 GB  5 minutes ago
llama3.2         mno345pqr678     2.0 GB  1 day ago
```

### 🗑️ מחיקת מודלים

```bash
# מחיקת מודל ספציפי
ollama rm gemma3:1b

# מחיקת כל המודלים (זהירות!)
ollama list | awk 'NR>1 {print $1}' | xargs -I {} ollama rm {}
```

### 🔧 הגדרות סביבה מתקדמות

#### שינוי תיקיית אחסון המודלים

**Linux/Mac:**
```bash
# הוספה ל-~/.bashrc או ~/.zshrc
export OLLAMA_MODELS="/path/to/your/models"

# טעינה מחדש
source ~/.bashrc
```

**Windows (PowerShell):**
```powershell
# הוספה למשתנה סביבה קבוע
[System.Environment]::SetEnvironmentVariable('OLLAMA_MODELS', 'D:\OllamaModels', 'User')
```

#### הגדרת מספר הליכים (threads)

```bash
# הגדרת 8 ליבות
export OLLAMA_NUM_THREADS=8

# הפעלת Ollama עם ההגדרה
ollama serve
```

#### שינוי פורט ברירת המחדל

```bash
# שימוש בפורט 8080 במקום 11434
export OLLAMA_HOST=0.0.0.0:8080
ollama serve
```

---

## 🎮 שימוש בסיסי

### צ'אט אינטראקטיבי

```bash
# פתיחת צ'אט עם Gemma 3
ollama run gemma3

# דוגמת שיחה:
>>> היי, מה המזג האוויר היום?
אני מודל AI ואין לי גישה למידע בזמן אמת כולל מזג אוויר. 
אני ממליץ לבדוק באפליקציית מזג אוויר או באתר ייעודי.

>>> תודה! /bye
```

#### פקודות שימושיות בצ'אט

- `/bye` - יציאה מהצ'אט
- `/clear` - ניקוי ההיסטוריה
- `/show info` - הצגת מידע על המודל
- `/show modelfile` - הצגת תצורת המודל
- `/?` - עזרה

### הרצת פקודה בודדת

```bash
# שאלה בודדת ללא צ'אט אינטראקטיבי
ollama run gemma3 "מהי בינה מלאכותית?"

# עם הפניית פלט לקובץ
ollama run llama3.2 "כתוב שיר על החיים" > poem.txt
```

### 🐍 שימוש ב-Python

#### התקנת הספרייה

```bash
pip install ollama
```

#### דוגמה בסיסית

```python
import ollama

# שיחה פשוטה
response = ollama.chat(model='gemma3', messages=[
    {
        'role': 'user',
        'content': 'למה השמיים כחולים?',
    },
])

print(response['message']['content'])
```

#### דוגמה מתקדמת עם streaming

```python
import ollama

# הצגת תשובה בזמן אמת
stream = ollama.chat(
    model='deepseek-r1',
    messages=[{'role': 'user', 'content': 'הסבר על חורים שחורים'}],
    stream=True,
)

for chunk in stream:
    print(chunk['message']['content'], end='', flush=True)
```

#### יצירת chatbot עם הקשר

```python
import ollama

conversation_history = []

def chat(user_message):
    # הוספת הודעת המשתמש להיסטוריה
    conversation_history.append({
        'role': 'user',
        'content': user_message
    })
    
    # קבלת תשובה
    response = ollama.chat(
        model='llama3.2',
        messages=conversation_history
    )
    
    # הוספת תשובת המודל להיסטוריה
    conversation_history.append({
        'role': 'assistant',
        'content': response['message']['content']
    })
    
    return response['message']['content']

# שימוש
print(chat("היי, קוראים לי דני"))
print(chat("איך קוראים לי?"))  # המודל יזכור!
```

### 💻 שימוש ב-JavaScript/TypeScript

#### התקנת הספרייה

```bash
npm install ollama
# או
yarn add ollama
```

#### דוגמה בסיסית

```javascript
import ollama from 'ollama';

async function main() {
    const response = await ollama.chat({
        model: 'gemma3',
        messages: [{ role: 'user', content: 'מהי תכנות?' }],
    });
    
    console.log(response.message.content);
}

main();
```

#### דוגמה עם streaming

```javascript
import ollama from 'ollama';

async function streamChat() {
    const stream = await ollama.chat({
        model: 'llama3.2',
        messages: [{ role: 'user', content: 'ספר לי סיפור קצר' }],
        stream: true,
    });

    for await (const chunk of stream) {
        process.stdout.write(chunk.message.content);
    }
}

streamChat();
```

### 🌐 שימוש ב-REST API

#### בדיקת זמינות

```bash
curl http://localhost:11434/api/version
```

#### שליחת שאלה

```bash
curl -X POST http://localhost:11434/api/generate -d '{
  "model": "gemma3",
  "prompt": "מדוע הירח זורח בלילה?",
  "stream": false
}'
```

#### צ'אט עם הקשר

```bash
curl -X POST http://localhost:11434/api/chat -d '{
  "model": "llama3.2",
  "messages": [
    {
      "role": "system",
      "content": "אתה עוזר מועיל שמדבר בעברית"
    },
    {
      "role": "user",
      "content": "מהו פיתון?"
    }
  ],
  "stream": false
}'
```

---

## 🚀 טיפים מתקדמים

### 1. יצירת Modelfile מותאם אישית

#### דוגמה: בוט תמיכה טכנית

צרו קובץ בשם `Modelfile`:

```dockerfile
FROM llama3.2

# הגדרת פרמטרי טמפרטורה (יצירתיות)
PARAMETER temperature 0.7
PARAMETER top_p 0.9

# הגדרת הקשר מערכת
SYSTEM """
אתה מומחה תמיכה טכנית עם ניסיון של 10 שנים.
אתה מדבר בעברית בצורה ברורה ומקצועית.
אתה תמיד מציע פתרונות מעשיים ובדוקים.
"""

# הגדרת תבנית
TEMPLATE """
{{ .System }}

שאלה: {{ .Prompt }}

תשובה מפורטת:
"""
```

#### יצירה והרצה

```bash
# יצירת המודל המותאם
ollama create tech-support -f ./Modelfile

# הרצה
ollama run tech-support "המחשב שלי לא נדלק"
```

### 2. שימוש במודלי ראייה (Vision Models)

```bash
# הורדת מודל ראייה
ollama pull llama3.2-vision

# ניתוח תמונה
ollama run llama3.2-vision "תאר את התמונה הזו" < /path/to/image.jpg
```

#### דוגמה ב-Python

```python
import ollama

# ניתוח תמונה
with open('photo.jpg', 'rb') as file:
    response = ollama.chat(
        model='llama3.2-vision',
        messages=[{
            'role': 'user',
            'content': 'מה אתה רואה בתמונה?',
            'images': [file.read()]
        }]
    )
    
print(response['message']['content'])
```

### 3. אופטימיזציה לביצועים

#### הגדרת quantization (דחיסה)

```bash
# הורדת גרסה דחוסה יותר (מהירה יותר, פחות מדויקת)
ollama pull llama3.2:Q4_K_M  # דחיסה בינונית
ollama pull llama3.2:Q2_K    # דחיסה גבוהה (הכי מהיר)
```

#### שימוש ב-GPU layers

```bash
# הגדרת מספר layers ב-GPU (Linux/Mac)
export OLLAMA_NUM_GPU=32  # כל ה-layers
ollama run llama3.2
```

#### הגדרת context window

```bash
# הגדלת חלון הקשר ל-8K tokens
ollama run gemma3 --context-length 8192
```

### 4. שמירת שיחות

```python
import ollama
import json
from datetime import datetime

def save_chat(messages, filename=None):
    if not filename:
        filename = f"chat_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(messages, f, ensure_ascii=False, indent=2)
    
    print(f"💾 שיחה נשמרה ב-{filename}")

# דוגמת שימוש
messages = [
    {'role': 'user', 'content': 'היי'},
    {'role': 'assistant', 'content': 'שלום! איך אוכל לעזור?'}
]

save_chat(messages)
```

### 5. שרת מרוחק עם Ollama

#### הפעלת שרת נגיש מרחוק

```bash
# הפעלה על כל הממשקים
OLLAMA_HOST=0.0.0.0:11434 ollama serve
```

#### התחברות מלקוח מרוחק

```python
import ollama

# התחברות לשרת מרוחק
client = ollama.Client(host='http://192.168.1.100:11434')

response = client.chat(
    model='gemma3',
    messages=[{'role': 'user', 'content': 'hello'}]
)

print(response['message']['content'])
```

### 6. בדיקת ביצועים (Benchmarking)

```bash
#!/bin/bash

echo "🧪 בדיקת ביצועים..."

# בדיקת זמן תשובה
time ollama run gemma3 "ספור עד 10" --verbose

# בדיקת tokens per second
ollama run llama3.2 "כתוב פסקה של 100 מילים" --verbose 2>&1 | grep "tokens"
```

### 7. אינטגרציה עם LangChain

```bash
pip install langchain langchain-community
```

```python
from langchain_community.llms import Ollama
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

# יצירת מודל
llm = Ollama(model="llama3.2")

# יצירת template
prompt = PromptTemplate(
    input_variables=["topic"],
    template="כתוב מאמר קצר על {topic} בעברית"
)

# יצירת chain
chain = LLMChain(llm=llm, prompt=prompt)

# הרצה
result = chain.run(topic="בינה מלאכותית")
print(result)
```

### 8. Multi-Modal: טקסט + תמונות

```python
import ollama
import base64

def analyze_image(image_path, question):
    with open(image_path, 'rb') as f:
        image_data = base64.b64encode(f.read()).decode('utf-8')
    
    response = ollama.chat(
        model='llama3.2-vision',
        messages=[{
            'role': 'user',
            'content': question,
            'images': [image_data]
        }]
    )
    
    return response['message']['content']

# שימוש
result = analyze_image('document.png', 'תמצת את המסמך הזה')
print(result)
```

---

## 🔧 פתרון בעיות נפוצות

### ❌ בעיה: "connection refused" או "cannot connect"

**פתרון:**

```bash
# 1. בדיקה אם השירות רץ
ps aux | grep ollama

# 2. הפעלת השירות ידנית
ollama serve

# 3. בדיקת פורט
netstat -tuln | grep 11434

# 4. Linux - בדיקת systemd
sudo systemctl status ollama
sudo systemctl restart ollama
```

### ❌ בעיה: "model not found"

**פתרון:**

```bash
# רשימת מודלים זמינים
ollama list

# הורדת המודל מחדש
ollama pull <model-name>

# ניקוי cache
rm -rf ~/.ollama/models/<model-name>
ollama pull <model-name>
```

### ❌ בעיה: ביצועים איטיים מאוד

**אבחון:**

```bash
# בדיקה אם משתמשים ב-GPU
ollama run llama3.2 --verbose "test" 2>&1 | grep -i gpu

# Linux: בדיקת GPU
nvidia-smi
```

**פתרונות:**

```bash
# 1. הורדת מודל קטן יותר
ollama pull gemma3:1b

# 2. שימוש בגרסה דחוסה
ollama pull llama3.2:Q4_K_M

# 3. הקטנת context window
ollama run llama3.2 --context-length 2048

# 4. הגדלת מספר threads
export OLLAMA_NUM_THREADS=8
```

### ❌ בעיה: שגיאת "out of memory"

**פתרונות:**

```bash
# 1. סגירת תוכניות אחרות

# 2. שימוש במודל קטן יותר
ollama pull gemma3:1b

---

## 📊 סטטיסטיקות הפרויקט

- **כוכבים**: 156,999 ⭐
- **Forks**: 13,816 🔱
- **Issues**: 2,315 🐛
- **שפה**: Go 💻
- **רישיון**: MIT License 📜

## 🔗 קישורים שימושיים

- [ריפו ב-GitHub](https://github.com/ollama/ollama)
- [Issues & תמיכה](https://github.com/ollama/ollama/issues)
- [Discussions](https://github.com/ollama/ollama/discussions)
- [Wiki](https://github.com/ollama/ollama/wiki)

---

*מדריך זה נוצר אוטומטית על ידי AI Guide Bot עם Claude AI*
*עדכון אחרון: 03/12/2025 18:58*

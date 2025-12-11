---
layout: unified-post
title: "מדריך מקצועי: ollama - Get up and running with OpenAI gpt-oss, DeepSeek-R1, Gemma 3 and other models."
date: 2025-12-04 12:26:40 +0200
categories: [AI, LLM, מדריכים]
tags: [local-ai, llm, installation, go]
image: /assets/images/repos/ollama-20251204.png
author: AI Guide Bot
lang: he
dir: rtl
---

![ollama](/assets/images/repos/ollama-20251204.png)

# 🚀 ollama

**⭐ 157,060 כוכבים | 🔧 Go | 📅 עדכון אחרון: 2025-12-04**

[🔗 קישור לריפו](https://github.com/ollama/ollama) | [⬇️ הורדה](https://github.com/ollama/ollama/archive/refs/heads/main.zip)

---

# 📘 מדריך התקנה מקיף ל-Ollama - הרצת מודלי AI מקומית

<div align="center">

![Ollama](https://img.shields.io/github/stars/ollama/ollama?style=social)
![License](https://img.shields.io/badge/license-MIT-blue)
![Go](https://img.shields.io/badge/Go-00ADD8?logo=go&logoColor=white)

</div>

---

## 📋 תוכן עניינים

1. [סקירה כללית](#-סקירה-כללית)
2. [דרישות מערכת](#-דרישות-מערכת)
3. [התקנה צעד אחר צעד](#-התקנה-צעד-אחר-צעד)
4. [הגדרה ראשונית](#-הגדרה-ראשונית)
5. [שימוש בסיסי](#-שימוש-בסיסי)
6. [טיפים מתקדמים](#-טיפים-מתקדמים)
7. [פתרון בעיות נפוצות](#-פתרון-בעיות-נפוצות)
8. [משאבים נוספים](#-משאבים-נוספים)

---

## 🎯 סקירה כללית

### מה זה Ollama?

**Ollama** היא פלטפורמה קלת משקל ופשוטה להרצה של מודלי שפה גדולים (LLM) באופן **מקומי** על המחשב שלך. במקום להסתמך על שירותי ענן יקרים או לשתף מידע רגיש עם צדדים שלישיים, Ollama מאפשרת לך:

✨ **יתרונות מרכזיים:**
- 🔒 **פרטיות מלאה** - הנתונים שלך נשארים במחשב שלך
- 💰 **חינמי לחלוטין** - אין עלויות API או מנויים
- ⚡ **מהיר ויעיל** - אופטימיזציה מתקדמת לחומרה מקומית
- 🎨 **גמיש** - תמיכה במגוון רחב של מודלים פתוחים
- 🔌 **אופליין** - עבודה ללא חיבור לאינטרנט

### למי זה מתאים?

- 👨‍💻 מפתחים שרוצים לשלב AI ביישומים שלהם
- 🔬 חוקרים הזקוקים לפרטיות וביקורת מלאה
- 🎓 סטודנטים ומתלמדים שרוצים ללמוד על LLMs
- 🏢 ארגונים עם דרישות אבטחה מחמירות
- 💻 חובבי טכנולוגיה שרוצים להתנסות במודלים מתקדמים

---

## 💻 דרישות מערכת

### דרישות חומרה מינימליות

| רכיב | מינימום | מומלץ | אופטימלי |
|------|---------|-------|----------|
| **RAM** | 8GB | 16GB | 32GB+ |
| **מעבד** | 4 ליבות | 8 ליבות | 16+ ליבות |
| **אחסון פנוי** | 10GB | 50GB | 100GB+ |
| **כרטיס מסך** | אינטגרטיבי | NVIDIA/AMD 6GB+ | RTX 3090/4090 |

### 📊 המלצות לפי מודל

| גודל מודל | RAM נדרש | דוגמאות למודלים |
|-----------|----------|-----------------|
| **1B-3B** | 8GB | Gemma 3:1b, Llama 3.2:1b, Phi 4 Mini |
| **7B-8B** | 16GB | Llama 3.1, Mistral, DeepSeek-R1 |
| **13B-14B** | 32GB | Phi 4, Llama 2 13B |
| **70B+** | 64GB+ | Llama 3.3 70B, Llama 4:scout |

### דרישות תוכנה

#### 🐧 Linux
- מערכת הפעלה: Ubuntu 18.04+, Debian 10+, RHEL 8+, Fedora 35+
- Kernel: 4.15+
- curl או wget
- (אופציונלי) Docker 20.10+

#### 🍎 macOS
- גרסה: macOS 11 Big Sur ומעלה
- עיבוד Intel או Apple Silicon (M1/M2/M3)

#### 🪟 Windows
- גרסה: Windows 10 22H2 / Windows 11
- WSL2 (אופציונלי אך מומלץ למפתחים)

---

## 🚀 התקנה צעד אחר צעד

### 🐧 Linux (שיטה מומלצת)

#### שיטה 1: התקנה אוטומטית (מהירה)

{% raw %}
```bash
# הורדה והתקנה בפקודה אחת
curl -fsSL https://ollama.com/install.sh | sh
```
{% endraw %}

**מה הסקריפט עושה?**
1. זיהוי אוטומטי של ההפצה והארכיטקטורה
2. הורדת הגרסה המתאימה ביותר
3. התקנת שירות systemd
4. הפעלה אוטומטית של השירות

#### שיטה 2: התקנה ידנית (שליטה מלאה)

{% raw %}
```bash
# 1. הורדת קובץ הבינארי
curl -L https://ollama.com/download/ollama-linux-amd64 -o ollama

# 2. הוספת הרשאות הרצה
chmod +x ollama

# 3. העברה לנתיב מערכת
sudo mv ollama /usr/local/bin/

# 4. יצירת משתמש מיוחד (אבטחה מומלצת)
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
Environment="PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"

[Install]
WantedBy=default.target
EOF

# 6. הפעלת השירות
sudo systemctl daemon-reload
sudo systemctl enable ollama
sudo systemctl start ollama

# 7. בדיקת סטטוס
sudo systemctl status ollama
```
{% endraw %}

#### 🎮 תמיכה בכרטיסי מסך NVIDIA

{% raw %}
```bash
# התקנת NVIDIA Container Toolkit
distribution=$(. /etc/os-release;echo $ID$VERSION_ID)
curl -s -L https://nvidia.github.io/nvidia-docker/gpgkey | sudo apt-key add -
curl -s -L https://nvidia.github.io/nvidia-docker/$distribution/nvidia-docker.list | \
  sudo tee /etc/apt/sources.list.d/nvidia-docker.list

sudo apt-get update
sudo apt-get install -y nvidia-container-toolkit

# אתחול Ollama
sudo systemctl restart ollama
```
{% endraw %}

---

### 🍎 macOS

#### שיטה 1: התקנה גרפית (מומלץ למתחילים)

1. **הורדה:**
   {% raw %}
```bash
   # פתיחת דפדפן והורדה
   open https://ollama.com/download/Ollama.dmg
   ```
{% endraw %}

2. **התקנה:**
   - פתח את קובץ ה-DMG שהורד
   - גרור את אייקון Ollama לתיקיית Applications
   - פתח את Ollama מתיקיית Applications
   - אשר את ההתראות בפעם הראשונה

3. **אימות:**
   {% raw %}
```bash
   # בדיקה שהפקודה זמינה בטרמינל
   ollama --version
   ```
{% endraw %}

#### שיטה 2: Homebrew (למפתחים)

{% raw %}
```bash
# התקנה דרך Homebrew
brew install ollama

# הפעלת השירות
brew services start ollama

# בדיקת סטטוס
brew services list | grep ollama
```
{% endraw %}

#### 💡 טיפ למשתמשי Apple Silicon

{% raw %}
```bash
# בדיקת סוג המעבד
uname -m

# תוצאה: arm64 = Apple Silicon (M1/M2/M3)
# תוצאה: x86_64 = Intel

# Ollama מזהה אוטומטית ומשתמש באופטימיזציות המתאימות
```
{% endraw %}

---

### 🪟 Windows

#### שיטה 1: התקנה גרפית (מומלצת)

1. **הורדה:**
   - גש לכתובת: https://ollama.com/download/OllamaSetup.exe
   - או דרך PowerShell:
   {% raw %}
```powershell
   # הורדה דרך PowerShell
   Invoke-WebRequest -Uri "https://ollama.com/download/OllamaSetup.exe" -OutFile "$env:TEMP\OllamaSetup.exe"
   
   # הרצת ההתקנה
   Start-Process "$env:TEMP\OllamaSetup.exe"
   ```{% raw %}
{% endraw %}

2. **התקנה:**
   - הרץ את {% endraw %}`OllamaSetup.exe`
   - אשר את User Account Control (UAC)
   - עקוב אחר אשף ההתקנה
   - Ollama יתווסף אוטומטית ל-PATH

3. **אימות:**
   {% raw %}
```powershell
   # פתח PowerShell או CMD חדש
   ollama --version
   ```
{% endraw %}

#### שיטה 2: WSL2 (למפתחים)

{% raw %}
```bash
# 1. וודא ש-WSL2 מותקן
wsl --install

# 2. פתח Ubuntu או הפצה אחרת
wsl

# 3. התקן Ollama בתוך WSL
curl -fsSL https://ollama.com/install.sh | sh

# 4. הרץ מ-Windows PowerShell
wsl ollama serve
```
{% endraw %}

#### ⚙️ הגדרות נוספות ל-Windows

{% raw %}
```powershell
# הוספת Ollama לחומת האש (אם נדרש)
New-NetFirewallRule -DisplayName "Ollama" -Direction Inbound -Program "C:\Program Files\Ollama\ollama.exe" -Action Allow

# שינוי יציאת ברירת המחדל (אופציונלי)
[Environment]::SetEnvironmentVariable("OLLAMA_HOST", "0.0.0.0:11434", "User")
```
{% endraw %}

---

### 🐳 Docker (כל מערכות ההפעלה)

#### התקנה בסיסית

{% raw %}
```bash
# הרצת Ollama בקונטיינר
docker run -d -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama
```
{% endraw %}

#### עם תמיכת GPU (NVIDIA)

{% raw %}
```bash
# הרצה עם CUDA
docker run -d \
  --gpus=all \
  -v ollama:/root/.ollama \
  -p 11434:11434 \
  --name ollama \
  ollama/ollama
```{% raw %}
{% endraw %}

#### Docker Compose (מומלץ לפרודקשן)

צור קובץ {% endraw %}`docker-compose.yml`:

{% raw %}
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
    restart: unless-stopped
    # הסר הערה לתמיכת GPU:
    # deploy:
    #   resources:
    #     reservations:
    #       devices:
    #         - driver: nvidia
    #           count: all
    #           capabilities: [gpu]

volumes:
  ollama_data:
    driver: local
```
{% endraw %}

{% raw %}
```bash
# הפעלה
docker-compose up -d

# בדיקת לוגים
docker-compose logs -f

# עצירה
docker-compose down
```
{% endraw %}

---

### 📱 Android (Termux) - אקספרימנטלי

⚠️ **שים לב:** זוהי שיטה לא רשמית ומתאימה למשתמשים מתקדמים בלבד.

{% raw %}
```bash
# 1. התקן Termux מ-F-Droid (לא Google Play!)
# הורד מ: https://f-droid.org/packages/com.termux/

# 2. עדכן חבילות
pkg update && pkg upgrade

# 3. התקן תלויות
pkg install wget proot-distro

# 4. התקן Ubuntu בתוך Termux
proot-distro install ubuntu
proot-distro login ubuntu

# 5. כעת פעל לפי הוראות Linux
curl -fsSL https://ollama.com/install.sh | sh

# 6. הרץ מודל קטן (מומלץ gemma3:1b)
ollama run gemma3:1b
```
{% endraw %}

💡 **המלצות לאנדרואיד:**
- השתמש במודלים קטנים (1B-3B)
- סגור אפליקציות אחרות בזמן השימוש
- חבר את המכשיר למטען
- דרוש לפחות 8GB RAM בטלפון

---

## ⚙️ הגדרה ראשונית

### בדיקת התקנה תקינה

{% raw %}
```bash
# בדיקת גרסה
ollama --version
# פלט מצופה: ollama version is X.X.X

# בדיקת חיבור לשרת
ollama list
# פלט מצופה: רשימה ריקה או מודלים קיימים
```
{% endraw %}

### הורדת המודל הראשון

{% raw %}
```bash
# הורדת מודל קל למתחילים (Gemma 3 - 4B)
ollama pull gemma3

# תהליך ההורדה מציג:
# pulling manifest
# pulling model... 100%
# verifying sha256 digest
# success
```{% raw %}
{% endraw %}

### 🎯 בחירת המודל הראשון שלך

| מודל | גודל | שימוש מומלץ | RAM נדרש |
|------|------|-------------|----------|
| {% endraw %}`gemma3:1b` | 815MB | ⚡ תשובות מהירות, צ'אט בסיסי | 4GB |
| `gemma3` | 3.3GB | 💬 שיחות כלליות, קוד פשוט | 8GB |
| `llama3.2` | 2.0GB | 🎯 איזון בין מהירות לאיכות | 8GB |
| `deepseek-r1` | 4.7GB | 🧠 חשיבה מתקדמת, מתמטיקה | 16GB |
| `llama3.2-vision` | 7.9GB | 👁️ עיבוד תמונות | 16GB |
| `codellama` | 3.8GB | 💻 כתיבת קוד | 8GB |

{% raw %}
```bash
# דוגמה: הורדת מודל לקוד
ollama pull codellama

# דוגמה: הורדת מודל ראייה
ollama pull llama3.2-vision
```
{% endraw %}

### 🔧 משתני סביבה (אופציונלי)

#### Linux/macOS

{% raw %}
```bash
# הוספה ל-~/.bashrc או ~/.zshrc

# שינוי כתובת השרת
export OLLAMA_HOST="0.0.0.0:11434"

# מיקום אחסון המודלים
export OLLAMA_MODELS="/path/to/models"

# הגבלת זיכרון GPU (MB)
export OLLAMA_MAX_VRAM=4096

# החלת השינויים
source ~/.bashrc
```
{% endraw %}

#### Windows (PowerShell)

{% raw %}
```powershell
# הגדרת משתנים קבועים
[Environment]::SetEnvironmentVariable("OLLAMA_HOST", "0.0.0.0:11434", "User")
[Environment]::SetEnvironmentVariable("OLLAMA_MODELS", "C:\ollama-models", "User")

# הפעלה מחדש של PowerShell
```
{% endraw %}

---

## 🎮 שימוש בסיסי

### 1️⃣ מצב אינטראקטיבי (צ'אט)

{% raw %}
```bash
# הרצת מודל במצב שיחה
ollama run gemma3

# דוגמה לשיחה:
# >>> היי! ספר לי בקצרה מה זה למידת מכונה
# 
# למידת מכונה היא תחום בבינה מלכותית שבו מחשבים לומדים
# מנתונים מבלי להיות מתוכנתים במפורש...
#
# >>> /bye
```{% raw %}
{% endraw %}

#### פקודות שימושיות במצב אינטראקטיבי

| פקודה | תיאור |
|-------|-------|
| {% endraw %}`/bye` | יציאה מהצ'אט |
| `/clear` | ניקוי היסטוריית השיחה |
| `/set parameter value` | שינוי פרמטרים |
| `/show info` | הצגת מידע על המודל |
| `/multiline` | כתיבת פסקה מרובת שורות |

### 2️⃣ שאילתה חד-פעמית

{% raw %}
```bash
# שאילתה ישירה ללא כניסה למצב אינטראקטיבי
ollama run gemma3 "כתוב לי פונקציה פייתון שמחשבת פיבונאצ'י"

# עם פרמטרים מותאמים אישית
ollama run gemma3 --temperature 0.7 --top-p 0.9 \
  "הסבר את תורת היחסות של איינשטיין בפשטות"
```
{% endraw %}

### 3️⃣ עבודה עם קבצים

{% raw %}
```bash
# העברת קובץ טקסט למודל
cat document.txt | ollama run gemma3 "סכם את הטקסט הבא:"

# ניתוח קוד
ollama run codellama "סקור את הקוד הבא ומצא באגים: $(cat script.py)"
```
{% endraw %}

### 4️⃣ עבודה עם תמונות (מודלי Vision)

{% raw %}
```bash
# ניתוח תמונה
ollama run llama3.2-vision "מה אתה רואה בתמונה הזו?" --image path/to/image.jpg

# תיאור מפורט
ollama run llama3.2-vision \
  "תאר את התמונה בפירוט, כולל צבעים, אובייקטים ורקע" \
  --image photo.png
```
{% endraw %}

### 5️⃣ API REST - שימוש מתוכניות

#### Python

{% raw %}
```python
import requests
import json

# שליחת בקשה למודל
url = "http://localhost:11434/api/generate"
payload = {
    "model": "gemma3",
    "prompt": "מה בירת ישראל?",
    "stream": False
}

response = requests.post(url, json=payload)
result = response.json()
print(result['response'])
```
{% endraw %}

#### דוגמה מתקדמת עם Streaming

{% raw %}
```python
import requests

url = "http://localhost:11434/api/generate"
payload = {
    "model": "gemma3",
    "prompt": "כתוב סיפור קצר על רובוט",
    "stream": True
}

with requests.post(url, json=payload, stream=True) as response:
    for line in response.iter_lines():
        if line:
            data = json.loads(line)
            print(data.get('response', ''), end='', flush=True)
```
{% endraw %}

#### JavaScript/Node.js

{% raw %}
```javascript
const ollama = require('ollama');

async function chat() {
  const response = await ollama.generate({
    model: 'gemma3',
    prompt: 'מה שלומך?'
  });
  
  console.log(response.response);
}

chat();
```
{% endraw %}

#### cURL (בדיקות מהירות)

{% raw %}
```bash
# בקשה פשוטה
curl http://localhost:11434/api/generate -d '{
  "model": "gemma3",
  "prompt": "למה השמיים כחולים?",
  "stream": false
}'

# עם פרמטרים מתקדמים
curl http://localhost:11434/api/generate -d '{
  "model": "gemma3",
  "prompt": "כתוב שיר על החיים",
  "stream": false,
  "options": {
    "temperature": 0.8,
    "top_p": 0.9,
    "top_k": 40
  }
}'
```
{% endraw %}

---

## 🔥 טיפים מתקדמים

### 1. יצירת Modelfile מותאם אישית

Modelfile מאפשר לך להתאים מודל קיים להתנהגות ספציפית.

{% raw %}
```{% raw %}dockerfile
# צור קובץ בשם Modelfile

FROM gemma3

# הגדרת טמפרטורה - שולט ביצירתיות
PARAMETER temperature 0.9

# הוראות מערכת - מגדירות את אופי המודל
SYSTEM """
אתה עוזר טכני מומחה בתחום הפייתון.
תן תשובות קצרות וממוקדות עם דוגמאות קוד.
השתמש בתחביר markdown לעיצוב.
"""

# הודעת פתיחה
TEMPLATE """{{ if .System }}<|system|>
{{ .System }}<|end|>
{{ end }}{{ if .Prompt }}<|user|>
{{ .Prompt }}<|end|>
{{ end }}<|assistant|>
"""
{% endraw %}```
{% endraw %}

{% raw %}
```bash
# יצירת המודל המותאם
ollama create python-expert -f Modelfile

# הרצה
ollama run python-expert "איך ליצור virtual environment?"
```
{% endraw %}

### 2. ייבוא מודלים מ-Hugging Face (GGUF)

{% raw %}
```{% raw %}bash
# 1. הורד מודל GGUF מ-Hugging Face
wget https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.2-GGUF/resolve/main/mistral-7b-instruct-v0.2.Q4_K_M.gguf

# 2. צור Modelfile
cat > Modelfile << 'EOF'
FROM ./mistral-7b-instruct-v0.2.Q4_K_M.gguf

PARAMETER stop "<|im_end|>"
PARAMETER stop "<|im_start|>"

TEMPLATE """<|im_start|>system
{{ .System }}<|im_end|>
<|im_start|>user
{{ .Prompt }}<|im_end|>
<|im_start|>assistant
"""
EOF

# 3. יצירת המודל
ollama create my-mistral -f Modelfile

# 4. הרצה
ollama run my-mistral
{% endraw %}```
{% endraw %}

### 3. אופטימיזציה למודלים גדולים

#### Quantization - הקטנת גודל המודל

{% raw %}
```bash
# הורדת מודל בקוונטיזציות שונות

# Q4_0 - הכי קטן, הכי מהיר, איכות בינונית
ollama pull llama3.1:8b-q4_0

# Q5_K_M - איזון טוב
ollama pull llama3.1:8b-q5_k_m

# Q8_0 - איכות גבוהה, איטי יותר
ollama pull llama3.1:8b-q8_0

# השוואת גדלים
ollama list
```
{% endraw %}

#### Context Window - הגדלת זיכרון השיחה

{% raw %}
```bash
# הרצה עם חלון הקשר מוגדל (ברירת מחדל: 2048)
ollama run gemma3 --ctx-size 4096

# או ב-Modelfile:
# PARAMETER num_ctx 4096
```
{% endraw %}

### 4. גישה מרחוק לשרת Ollama

#### הגדרת שרת

{% raw %}
```bash
# Linux/macOS - ערוך את קובץ השירות
sudo systemctl edit ollama

# הוסף:
[Service]
Environment="OLLAMA_HOST=0.0.0.0:11434"

# אתחל
sudo systemctl restart ollama

# Windows - פתח PowerShell כמנהל
[Environment]::SetEnvironmentVariable("OLLAMA_HOST", "0.0.0.0:11434", "Machine")
Restart-Service Ollama
```
{% endraw %}

#### חיבור מלקוח

{% raw %}
```bash
# במחשב מרוחק
export OLLAMA_HOST="http://192.168.1.100:11434"
ollama list

# בקשת API מרחוק
curl http://192.168.1.100:11434/api/generate -d '{
  "model": "gemma3",
  "prompt": "Hello from remote!"
}'
```
{% endraw %}

### 5. Multi-modal - שילוב טקסט ותמונות

{% raw %}
```python
import base64
import requests

# קריאת תמונה
with open("image.jpg", "rb") as f:
    image_data = base64.b64encode(f.read()).decode()

# שליחה למודל
url = "http://localhost:11434/api/generate"
payload = {
    "model": "llama3.2-vision",
    "prompt": "תאר מה יש בתמונה ומצא אובייקטים חשודים",
    "images": [image_data],
    "stream": False
}

response = requests.post(url, json=payload)
print(response.json()['response'])
```
{% endraw %}

### 6. Batch Processing - עיבוד אצווה

{% raw %}
```bash
#!/bin/bash
# עיבוד רשימת שאלות מקובץ

while IFS= read -r question; do
    echo "שאלה: $question"
    echo "תשובה:"
    ollama run gemma3 "$question" --nowordwrap
    echo "---"
done < questions.txt > answers.txt
```
{% endraw %}

### 7. שימוש ב-GPU מרובים

{% raw %}
```bash
# הצגת GPU זמינים
nvidia-smi

# הגדרת משתני סביבה
export CUDA_VISIBLE_DEVICES=0,1  # שימוש ב-GPU 0 ו-1

# או בהרצה ספציפית
CUDA_VISIBLE_DEVICES=1 ollama run llama3.3:70b
```
{% endraw %}

### 8. Prompt Engineering - טכניקות מתקדמות

#### Chain of Thought (חשיבה שלבית)

{% raw %}
```bash
ollama run gemma3 "
פתור את הבעיה הבאה צעד אחר צעד:

אם לרכבת יש 15 קרונות, ובכל קרון 28 מושבים,
ו-85% מהמושבים תפוסים, כמה נוסעים יש ברכבת?

הראה את התהליך:
1. חישוב סה\"ך מושבים
2. חישוב מושבים תפוסים
3. תשובה סופית
"
```{% raw %}
{% endraw %}

#### Few-Shot Learning (למידה מדוגמאות)

{% endraw %}```bash
ollama run gemma3 "
תרגם משפטים לאנגלית:

דוגמה 1:
עברית: שלום עולם
א

---

## 📊 סטטיסטיקות הפרויקט

- **כוכבים**: 157,060 ⭐
- **Forks**: 13,828 🔱
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
*עדכון אחרון: 04/12/2025 12:26*

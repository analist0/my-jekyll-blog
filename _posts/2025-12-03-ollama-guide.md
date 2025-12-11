---
layout: unified-post
title: "מדריך מקצועי: ollama - Get up and running with OpenAI gpt-oss, DeepSeek-R1, Gemma 3 and other models."
date: 2025-12-03 19:13:07 +0200
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

# 📚 מדריך התקנה מקיף ל-Ollama - הרצת מודלי AI מקומית

## 🎯 סקירה כללית

**Ollama** היא פלטפורמה קלה ויעילה להרצת מודלי שפה גדולים (LLMs) באופן מקומי על המחשב שלך. במקום להסתמך על שירותי ענן יקרים, Ollama מאפשרת לך להריץ מודלים כמו Llama, Gemma, DeepSeek-R1 ועוד ישירות על המכונה שלך.

### 🌟 למה Ollama?

- **🔒 פרטיות מלאה** - הנתונים שלך נשארים אצלך במחשב
- **💰 חינם לחלוטין** - ללא עלויות API או מנויים חודשיים
- **⚡ מהירות** - אין תלות ברשת, תגובות מיידיות
- **🎨 התאמה אישית** - יכולת לכוונן ולהתאים מודלים לצרכים שלך
- **🔌 עבודה אופליין** - פועל גם ללא חיבור לאינטרנט

---

## 💻 דרישות מערכת

### דרישות מינימום:

| רכיב | דרישה |
|------|-------|
| **RAM** | 8GB (למודלים של 7B פרמטרים) |
| **אחסון** | 10GB פנויים לפחות |
| **מעבד** | מעבד מודרני (Intel i5/AMD Ryzen 5 ומעלה) |
| **מערכת הפעלה** | Windows 10+, macOS 11+, או Linux |

### דרישות מומלצות:

| גודל מודל | RAM מומלץ | דוגמה |
|-----------|-----------|--------|
| 1B-7B | 8-16GB | Gemma 3:1b, Llama 3.2 |
| 13B-27B | 16-32GB | Gemma 3:27b, Phi 4 |
| 33B-70B | 32-64GB | Llama 3.3, QwQ |
| 100B+ | 64GB+ | Llama 4, DeepSeek-R1:671b |

⚠️ **הערה חשובה**: מודלים גדולים יותר דורשים יותר זיכרון. אם אין לך מספיק RAM, המערכת תשתמש ב-swap ותהיה איטית מאוד.

💡 **טיפ**: אם יש לך כרטיס מסך NVIDIA, Ollama תשתמש בו אוטומטית להאצת החישובים.

---

## 🚀 התקנה צעד אחר צעד

### 🐧 Linux

#### שיטה 1: התקנה אוטומטית (מומלץ)

{% raw %}
```bash
# הורדה והתקנה בפקודה אחת
curl -fsSL https://ollama.com/install.sh | sh
```{% raw %}
{% endraw %}

התסריט יבצע את הפעולות הבאות:
- ✅ הורדת הקבצים הדרושים
- ✅ התקנת Ollama ב-{% endraw %}`/usr/local/bin`
- ✅ יצירת שירות systemd
- ✅ הפעלת השירות אוטומטית

#### שיטה 2: התקנה ידנית

{% raw %}
```bash
# Ubuntu/Debian
sudo apt update
sudo apt install curl

# הורדת הקובץ
curl -L https://ollama.com/download/ollama-linux-amd64 -o ollama
chmod +x ollama
sudo mv ollama /usr/local/bin/

# יצירת שירות systemd
sudo useradd -r -s /bin/false -m -d /usr/share/ollama ollama

# יצירת קובץ השירות
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

# הפעלת השירות
sudo systemctl daemon-reload
sudo systemctl enable ollama
sudo systemctl start ollama
```
{% endraw %}

#### בדיקת ההתקנה:

{% raw %}
```bash
# בדיקת גרסה
ollama --version

# בדיקת סטטוס השירות
systemctl status ollama
```
{% endraw %}

---

### 🍎 macOS

#### התקנה:

1. **הורד את הקובץ**:
   - גש ל-[https://ollama.com/download/Ollama.dmg](https://ollama.com/download/Ollama.dmg)
   - או השתמש ב-Terminal:

{% raw %}
```bash
# הורדה עם curl
curl -L https://ollama.com/download/Ollama.dmg -o ~/Downloads/Ollama.dmg
```
{% endraw %}

2. **התקן את האפליקציה**:
   - פתח את קובץ ה-DMG שהורדת
   - גרור את Ollama.app לתיקיית Applications
   - פתח את Ollama מתיקיית Applications

3. **הפעלה ראשונית**:
   - בהפעלה הראשונה, macOS עשוי לבקש אישור (System Settings → Privacy & Security)
   - Ollama תרוץ כאפליקציית רקע בשורת התפריטים

#### בדיקת התקנה:

{% raw %}
```bash
# פתח Terminal ובדוק
ollama --version

# אם הפקודה לא נמצאת, הוסף ל-PATH:
echo 'export PATH="/Applications/Ollama.app/Contents/MacOS:$PATH"' >> ~/.zshrc
source ~/.zshrc
```{% raw %}
{% endraw %}

---

### 🪟 Windows

#### התקנה:

1. **הורד את המתקין**:
   - גש ל-[https://ollama.com/download/OllamaSetup.exe](https://ollama.com/download/OllamaSetup.exe)

2. **הפעל את המתקין**:
   - הפעל את {% endraw %}`OllamaSetup.exe`
   - עקוב אחר ההוראות על המסך
   - אישור אדמין נדרש

3. **אחרי ההתקנה**:
   - Ollama תרוץ אוטומטית כשירות רקע
   - סמל יופיע במגש המערכת (System Tray)

#### בדיקת התקנה:

פתח **PowerShell** או **Command Prompt**:

{% raw %}
```powershell
# בדיקת גרסה
ollama --version

# בדיקת שהשירות רץ
ollama list
```{% raw %}
{% endraw %}

#### פתרון בעיות Windows:

אם הפקודה {% endraw %}`ollama` לא נמצאת:

{% raw %}
```powershell
# הוסף ל-PATH (PowerShell כאדמין)
$env:Path += ";C:\Users\$env:USERNAME\AppData\Local\Programs\Ollama"
[Environment]::SetEnvironmentVariable("Path", $env:Path, [System.EnvironmentVariableScope]::User)
```
{% endraw %}

---

### 🐳 Docker

#### הרצה בסיסית:

{% raw %}
```bash
# הרצת Ollama ב-Docker
docker run -d -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama
```
{% endraw %}

#### עם תמיכת GPU (NVIDIA):

{% raw %}
```bash
# התקנת NVIDIA Container Toolkit (פעם אחת)
distribution=$(. /etc/os-release;echo $ID$VERSION_ID)
curl -s -L https://nvidia.github.io/nvidia-docker/gpgkey | sudo apt-key add -
curl -s -L https://nvidia.github.io/nvidia-docker/$distribution/nvidia-docker.list | sudo tee /etc/apt/sources.list.d/nvidia-docker.list

sudo apt-get update
sudo apt-get install -y nvidia-container-toolkit
sudo systemctl restart docker

# הרצת Ollama עם GPU
docker run -d --gpus=all -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama
```{% raw %}
{% endraw %}

#### שימוש עם Docker Compose:

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
    # הסר את ההערה אם יש GPU
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
{% endraw %}

הפעלה:

{% raw %}
```bash
docker-compose up -d
```
{% endraw %}

---

### 📱 Termux (Android)

⚠️ **אזהרה**: הרצת LLMs על Android היא אקספרימנטלית ומתאימה רק למודלים קטנים מאוד.

{% raw %}
```bash
# התקנת Termux מ-F-Droid (לא מ-Play Store!)
# אז פתח את Termux והרץ:

# עדכון חבילות
pkg update && pkg upgrade -y

# התקנת תלויות
pkg install wget proot-distro -y

# התקנת Ubuntu בתוך Termux
proot-distro install ubuntu
proot-distro login ubuntu

# כעת אתה בסביבת Ubuntu, התקן Ollama:
apt update
apt install curl -y
curl -fsSL https://ollama.com/install.sh | sh

# הרצת Ollama
ollama serve &
```
{% endraw %}

💡 **טיפ**: על Android, השתמש במודלים קטנים בלבד (1B-3B פרמטרים):
{% raw %}
```bash
ollama run gemma3:1b
ollama run llama3.2:1b
```
{% endraw %}

---

## ⚙️ הגדרה ראשונית

### 1️⃣ הורדת המודל הראשון

אחרי ההתקנה, הורד מודל כדי להתחיל:

{% raw %}
```bash
# מודל קל למתחילים (815MB)
ollama pull gemma3:1b

# או מודל יותר מתקדם (4.7GB)
ollama pull llama3.1
```{% raw %}
{% endraw %}

הפקודה {% endraw %}`pull` מורידה את המודל מהשרת של Ollama ושומרת אותו מקומית.

### 2️⃣ בדיקת המודלים המותקנים

{% raw %}
```bash
# הצגת כל המודלים שהורדת
ollama list
```
{% endraw %}

פלט לדוגמה:
{% raw %}
```
NAME                ID              SIZE      MODIFIED
gemma3:1b          a1b2c3d4e5f6    815 MB    2 minutes ago
llama3.1:latest    f6e5d4c3b2a1    4.7 GB    5 minutes ago
```
{% endraw %}

### 3️⃣ הרצת מודל ראשון

{% raw %}
```bash
# הרצת מודל במצב אינטראקטיבי
ollama run gemma3:1b
```
{% endraw %}

אתה תראה prompt שבו תוכל להקליד שאלות:

{% raw %}
```
>>> מהי בינה מלאכותית?
בינה מלאכותית (AI) היא תחום במדעי המחשב העוסק ביצירת מערכות
מחשב המסוגלות לבצע משימות הדורשות בדרך כלל אינטליגנציה אנושית...

>>> /bye
```
{% endraw %}

### 4️⃣ הגדרות סביבה מתקדמות

#### שינוי תיקיית האחסון:

{% raw %}
```bash
# Linux/Mac
export OLLAMA_MODELS="/path/to/custom/models"
echo 'export OLLAMA_MODELS="/path/to/custom/models"' >> ~/.bashrc

# Windows (PowerShell)
$env:OLLAMA_MODELS = "D:\OllamaModels"
[Environment]::SetEnvironmentVariable("OLLAMA_MODELS", "D:\OllamaModels", "User")
```
{% endraw %}

#### הגדרת זיכרון GPU:

{% raw %}
```bash
# הגבלת שימוש ב-VRAM (במקרה של מספר GPUs)
export OLLAMA_NUM_GPU=1
export OLLAMA_GPU_LAYERS=35  # כמה שכבות להעביר ל-GPU
```
{% endraw %}

#### שינוי פורט:

{% raw %}
```bash
# שינוי מפורט ברירת המחדל 11434
export OLLAMA_HOST=0.0.0.0:8080

# הפעלה מחדש של ollama
# Linux:
sudo systemctl restart ollama

# Mac/Windows:
# סגור ופתח מחדש את האפליקציה
```{% raw %}
{% endraw %}

---

## 🎓 שימוש בסיסי

### פקודות CLI עיקריות

#### 1. {% endraw %}`ollama run` - הרצה אינטראקטיבית

{% raw %}
```bash
# הרצה בסיסית
ollama run llama3.1

# עם prompt מוכן מראש
ollama run llama3.1 "כתוב לי סיפור קצר על חתול חלל"

# עם פרמטרים
ollama run llama3.1 --verbose
```{% raw %}
{% endraw %}

#### 2. {% endraw %}`ollama pull` - הורדת מודל

{% raw %}
```bash
# הורדת מודל ספציפי
ollama pull deepseek-r1

# הורדת גרסה ספציפית
ollama pull llama3.1:70b

# הצגת התקדמות
ollama pull gemma3:27b --verbose
```{% raw %}
{% endraw %}

#### 3. {% endraw %}`ollama list` - רשימת מודלים

{% raw %}
```bash
# הצגת כל המודלים
ollama list

# עם מידע מפורט
ollama list --verbose
```{% raw %}
{% endraw %}

#### 4. {% endraw %}`ollama rm` - מחיקת מודל

{% raw %}
```bash
# מחיקת מודל שאינך משתמש בו
ollama rm llama2-uncensored

# מחיקת גרסה ספציפית
ollama rm gemma3:27b
```{% raw %}
{% endraw %}

#### 5. {% endraw %}`ollama ps` - תהליכים פעילים

{% raw %}
```bash
# הצגת מודלים שרצים כרגע
ollama ps
```{% raw %}
{% endraw %}

#### 6. {% endraw %}`ollama cp` - העתקת מודל

{% raw %}
```bash
# יצירת עותק עם שם מותאם
ollama cp llama3.1 my-custom-llama
```
{% endraw %}

### שימוש ב-Multiline Prompts

{% raw %}
```bash
ollama run gemma3 "
אתה עוזר תכנות מומחה.
כתוב פונקציה ב-Python שמחשבת את המספר הפיבונאצ'י ה-n.
הוסף הערות מפורטות.
"
```
{% endraw %}

### שימוש במצב Silent (ללא פלט ביניים)

{% raw %}
```bash
ollama run --verbose=false gemma3 "מה 2+2?"
```{% raw %}
{% endraw %}

---

## 🔧 שימוש מתקדם

### יצירת Modelfile מותאם אישית

**Modelfile** הוא קובץ תצורה שמאפשר להתאים מודל לצרכים שלך.

#### דוגמה 1: מודל עם system prompt מותאם

צור קובץ בשם {% endraw %}`Modelfile`:

{% raw %}
```dockerfile
# שימוש במודל בסיס
FROM llama3.1

# הגדרת ההתנהגות
SYSTEM """
אתה עוזר תכנות מומחה המתמחה ב-Python ו-JavaScript.
תמיד תסביר את הקוד שלך בעברית בצורה ברורה וקצרה.
הוסף דוגמאות שימוש לכל פונקציה שאתה כותב.
"""

# פרמטרים
PARAMETER temperature 0.7
PARAMETER top_p 0.9
PARAMETER top_k 40
```
{% endraw %}

יצירה והרצה:

{% raw %}
```bash
# יצירת המודל המותאם
ollama create code-assistant -f Modelfile

# הרצת המודל
ollama run code-assistant
```
{% endraw %}

#### דוגמה 2: מודל מתורגם

{% raw %}
```dockerfile
FROM mistral

SYSTEM """
אתה מתרגם מקצועי.
תרגם כל טקסט שאתה מקבל מאנגלית לעברית.
שמור על המשמעות המקורית והטון.
"""

PARAMETER temperature 0.3
```
{% endraw %}

{% raw %}
```bash
ollama create translator -f Modelfile
ollama run translator "Translate: Hello world"
```
{% endraw %}

#### דוגמה 3: ייבוא מודל GGUF

{% raw %}
```dockerfile
# ייבוא מודל מקומי (GGUF)
FROM ./models/my-model.gguf

# הוספת הוראות
SYSTEM "אתה צ'טבוט ידידותי"

PARAMETER temperature 0.8
PARAMETER num_ctx 4096
```
{% endraw %}

{% raw %}
```bash
ollama create my-imported-model -f Modelfile
```{% raw %}
{% endraw %}

### פרמטרים חשובים ב-Modelfile

| פרמטר | תיאור | ערכים | ברירת מחדל |
|-------|-------|-------|------------|
| {% endraw %}`temperature` | יצירתיות (נמוך=דטרמיניסטי, גבוה=יצירתי) | 0.0-2.0 | 0.8 |
| `top_p` | Nucleus sampling | 0.0-1.0 | 0.9 |
| `top_k` | מספר טוקנים לשקול | 1-100 | 40 |
| `num_ctx` | אורך ההקשר (context window) | 512-32768 | 2048 |
| `num_predict` | מקסימום טוקנים בתשובה | -1-2048 | 128 |
| `repeat_penalty` | עונש על חזרות | 1.0-2.0 | 1.1 |

### שימוש ב-API של Ollama

Ollama חושפת REST API על פורט 11434.

#### Python:

{% raw %}
```python
import requests
import json

def chat_with_ollama(prompt, model="gemma3"):
    url = "http://localhost:11434/api/generate"
    
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False
    }
    
    response = requests.post(url, json=payload)
    
    if response.status_code == 200:
        return response.json()["response"]
    else:
        return f"שגיאה: {response.status_code}"

# שימוש
result = chat_with_ollama("מהי בירת ישראל?")
print(result)
```
{% endraw %}

#### עם ספריית ollama-python:

{% raw %}
```bash
pip install ollama
```
{% endraw %}

{% raw %}
```python
import ollama

# שיחה בסיסית
response = ollama.chat(model='gemma3', messages=[
    {
        'role': 'user',
        'content': 'למה השמים כחולים?'
    }
])

print(response['message']['content'])

# שיחה עם streaming
for chunk in ollama.chat(
    model='gemma3',
    messages=[{'role': 'user', 'content': 'ספר לי בדיחה'}],
    stream=True
):
    print(chunk['message']['content'], end='', flush=True)
```
{% endraw %}

#### JavaScript/TypeScript:

{% raw %}
```bash
npm install ollama
```
{% endraw %}

{% raw %}
```javascript
import ollama from 'ollama';

// שיחה בסיסית
const response = await ollama.chat({
    model: 'gemma3',
    messages: [{ role: 'user', content: 'שלום, מה שלומך?' }]
});

console.log(response.message.content);

// עם streaming
const stream = await ollama.chat({
    model: 'gemma3',
    messages: [{ role: 'user', content: 'כתוב סיפור קצר' }],
    stream: true
});

for await (const chunk of stream) {
    process.stdout.write(chunk.message.content);
}
```
{% endraw %}

#### cURL (לבדיקות):

{% raw %}
```bash
# בקשה בסיסית
curl http://localhost:11434/api/generate -d '{
  "model": "gemma3",
  "prompt": "למה השמים כחולים?",
  "stream": false
}'

# בדיקת מודלים זמינים
curl http://localhost:11434/api/tags

# מידע על מודל ספציפי
curl http://localhost:11434/api/show -d '{
  "name": "gemma3"
}'
```
{% endraw %}

---

## 💡 טיפים ואופטימיזציות

### 1️⃣ בחירת המודל הנכון

{% raw %}
```bash
# למשימות קלות וחסכון במשאבים:
ollama run gemma3:1b          # 815MB, מהיר מאוד
ollama run llama3.2:1b        # 1.3GB, טוב לסיכומים

# לאיזון בין איכות למהירות:
ollama run gemma3:4b          # 3.3GB, האיזון הטוב ביותר
ollama run llama3.1           # 4.7GB, איכותי ומהיר

# לאיכות מקסימלית (דורש משאבים רבים):
ollama run llama3.3           # 43GB (70B פרמטרים)
ollama run deepseek-r1:671b   # 404GB (למכונות חזקות בלבד!)
```
{% endraw %}

### 2️⃣ אופטימיזציה למהירות

#### הגדלת מספר תהליכים מקבילים:

{% raw %}
```bash
# הגדרת מספר תהליכים שיכולים לרוץ בו-זמנית
export OLLAMA_MAX_LOADED_MODELS=2

# הגדרת thread count
export OLLAMA_NUM_PARALLEL=4
```
{% endraw %}

#### שימוש ב-GPU בצורה יעילה:

{% raw %}
```bash
# בדיקה אם GPU מזוהה
nvidia-smi  # עבור NVIDIA

# הרצה עם כל השכבות ב-GPU
export OLLAMA_GPU_LAYERS=999  # טוען מקסימום שכבות אפשרי

# או רק חלק (לחיסכון ב-VRAM):
export OLLAMA_GPU_LAYERS=20
```
{% endraw %}

### 3️⃣ ניהול זיכרון

{% raw %}
```bash
# ניקוי מודלים שלא בשימוש מהזיכרון
ollama stop <model-name>

# הגבלת גודל context (חוסך זיכרון):
ollama run gemma3 --num-ctx 2048

# מחיקת מודלים שלא צריך:
ollama rm <unused-model>
```
{% endraw %}

### 4️⃣ שימוש ב-Quantization

מודלים מגיעים בגרסאות quantization שונות:

{% raw %}
```bash
# גרסאות quantization נפוצות:
ollama pull llama3.1:q4_0     # 4-bit, קטן מאוד (הפחתה באיכות)
ollama pull llama3.1:q4_k_m   # 4-bit medium (איזון טוב)
ollama pull llama3.1:q5_k_m   # 5-bit medium (איכות טובה יותר)
ollama pull llama3.1:q8_0     # 8-bit (איכות גבוהה, יותר כבד)
ollama pull llama3.1:latest   # גרסת ברירת מחדל (בדרך כלל q4)
```{% raw %}
{% endraw %}

💡 **המלצה**: {% endraw %}`q4_k_m` נותן את האיזון הטוב ביותר בין גודל לאיכות.

### 5️⃣ Batch Processing

{% raw %}
```bash
# עיבוד מרובה prompts מקובץ
cat prompts.txt | while read prompt; do
    echo "=== $prompt ==="
    ollama run gemma3 "$prompt"
    echo ""
done
```
{% endraw %}

### 6️⃣ שימוש ב-RAG (Retrieval Augmented Generation)

דוגמה בסיסית ל-RAG עם Ollama:

{% raw %}
```python
import ollama

# מסמכים לחיפוש (בפועל יהיו מ-vector DB)
documents = [
    "Ollama היא פלטפורמה להרצת LLMs מקומית",
    "היא תומכת במודלים כמו Llama, Gemma ו-Mistral",
    "ניתן להריץ אותה על Mac, Windows ו-Linux"
]

def rag_query(question):
    # שלב 1: מציאת מסמכים רלוונטיים (פשטני - בפועל תשתמש ב-embeddings)
    context = "\n".join(documents)
    
    # שלב 2: שאילתה עם הקשר
    prompt = f"""
    בהתבסס על המידע הבא:
    {context}
    
    שאלה: {question}
    
    תשובה:
    """
    
    response = ollama.chat(model='gemma3', messages=[
        {'role': 'user', 'content': prompt}
    ])
    
    return response['message']['content']

# שימוש
answer = rag_query("על אילו מערכות הפעלה Ollama פועלת?")
print(answer)
```
{% endraw %}

---

## ⚠️ פתרון בעיות נפוצות

### 🔴 בעיה: "ollama: command not found"

**פתרון Linux/Mac:**
{% raw %}
```bash
# בדוק אם Ollama מותקן
which ollama

# אם לא, הוסף ל-PATH
# Linux:
export PATH=$PATH:/usr/local/bin
echo 'export PATH=$PATH:/usr/local/bin' >> ~/.bashrc

# Mac:
export PATH="/Applications/Ollama.app/Contents/MacOS:$PATH"
echo 'export PATH="/Applications/Ollama.app/Contents/MacOS:$PATH"' >> ~/.zshrc
```
{% endraw %}

**פתרון Windows:**
{% raw %}
```powershell
# בדוק אם בתיקיית התקנה
cd $env:LOCALAPPDATA\Programs\Ollama
.\ollama.exe --version

# אם עובד, הוסף ל-PATH
$env:Path += ";$env:LOCALAPPDATA\Programs\Ollama"
```
{% endraw %}

---

### 🔴 בעיה: "Failed to load model"

**סיבות אפשריות:**

1. **אין מספיק RAM:**
{% raw %}
```bash
# בדוק שימוש בזיכרון
free -h  # Linux
vm_stat  # Mac

# השתמש במודל קטן יותר
ollama run gemma3:1b
```
{% endraw %}

2. **המודל לא הורד במלואו:**
{% raw %}
```bash
# מחק והורד מחדש
ollama rm gemma3
ollama pull gemma3
```
{% endraw %}

3. **קבצים פגומים:**
{% raw %}
```bash
# נקה cache ונסה שוב
rm -rf ~/.ollama/models/<model-name>
ollama pull <model-name>
```
{% endraw %}

---

### 🔴 בעיה: הדור איטי מאוד

**אבחון:**

{% raw %}
```bash
# בדוק אם GPU מזוהה
nvidia-smi  # NVIDIA
rocm-smi    # AMD

# בדוק איזה device בשימוש
ollama ps
```{% raw %}
{% endraw %}

**פתרון:**

{% endraw %}```bash
# אילוץ שימוש ב-CPU (אם GPU גורם לבעיות)
export OLLAMA_COMPUTE=cpu
sudo systemctl restart ollama

# או הגבל שכבות ב-

---

## 📊 סטטיסטיקות הפרויקט

- **כוכבים**: 156,999 ⭐
- **Forks**: 13,818 🔱
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
*עדכון אחרון: 03/12/2025 19:13*

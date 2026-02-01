#!/usr/bin/env python3
"""
AI Repository Guide Generator
Finds trending AI/LLM repos and generates professional installation guides using Google Gemini / Perplexity
"""

import os
import sys
import json
import requests
from datetime import datetime, timedelta
from pathlib import Path
import time

# Configuration
GITHUB_API = "https://api.github.com"
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN")
GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY")
PERPLEXITY_API_KEY = os.environ.get("PERPLEXITY_API_KEY")
GEMINI_MODEL = os.environ.get("GEMINI_MODEL", "gemini-2.5-flash")
PERPLEXITY_MODEL = os.environ.get("PERPLEXITY_MODEL", "llama-3.1-sonar-large-128k-online")

# Focus keywords for local AI/LLM repos
AI_KEYWORDS = [
    "llama", "ollama", "local-llm", "llm", "gpt", "mistral",
    "language-model", "transformer", "stable-diffusion", "whisper",
    "text-generation", "ai-assistant", "chatbot", "deepseek",
    "qwen", "gemma", "phi", "rag", "vector-database"
]

def get_trending_ai_repos():
    """Find the most popular AI repository from the last week"""
    print("🔍 Searching for trending AI repositories...")

    # Search for repos created/updated in the last week with high stars
    one_week_ago = (datetime.now() - timedelta(days=7)).strftime("%Y-%m-%d")

    # Try multiple search queries to find the best AI repo
    queries = [
        f"local llm stars:>100 created:>{one_week_ago}",
        f"ollama stars:>50 pushed:>{one_week_ago}",
        f"ai assistant stars:>100 language:python pushed:>{one_week_ago}",
        f"llm inference stars:>100 pushed:>{one_week_ago}",
        f"vector database ai stars:>50 pushed:>{one_week_ago}"
    ]

    best_repo = None
    max_stars = 0

    headers = {"Authorization": f"token {GITHUB_TOKEN}"} if GITHUB_TOKEN else {}

    for query in queries:
        try:
            url = f"{GITHUB_API}/search/repositories?q={query}&sort=stars&order=desc&per_page=5"
            response = requests.get(url, headers=headers)

            if response.status_code == 200:
                data = response.json()
                for repo in data.get("items", []):
                    # Filter for AI/LLM related repos
                    repo_text = f"{repo['name']} {repo['description'] or ''}".lower()
                    if any(keyword in repo_text for keyword in AI_KEYWORDS):
                        stars = repo["stargazers_count"]
                        if stars > max_stars:
                            max_stars = stars
                            best_repo = repo

            time.sleep(2)  # Rate limiting
        except Exception as e:
            print(f"⚠️  Error searching with query '{query}': {e}")
            continue

    if not best_repo:
        # Fallback: get most popular AI repos of all time
        url = f"{GITHUB_API}/search/repositories?q=ollama+OR+llama+language:python&sort=stars&order=desc&per_page=1"
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            if data.get("items"):
                best_repo = data["items"][0]

    return best_repo

def get_repo_readme(repo):
    """Fetch repository README content"""
    try:
        url = f"{GITHUB_API}/repos/{repo['full_name']}/readme"
        headers = {
            "Accept": "application/vnd.github.v3.raw"
        }
        if GITHUB_TOKEN:
            headers["Authorization"] = f"token {GITHUB_TOKEN}"

        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
        return ""
    except Exception as e:
        print(f"⚠️  Error fetching README: {e}")
        return ""

def generate_socialify_card(repo_full_name, output_path):
    """Generate beautiful repo card using Socialify API"""
    print(f"🎨 Generating Socialify card for {repo_full_name}...")

    try:
        # Socialify API URL with customization
        # Options: owner, name, description, language, stargazers, forks, issues, pulls, theme
        socialify_url = (
            f"https://socialify.git.ci/{repo_full_name}/image?"
            f"description=1&"
            f"descriptionEditable=&"
            f"font=Raleway&"
            f"language=1&"
            f"name=1&"
            f"owner=1&"
            f"pattern=Circuit%20Board&"
            f"stargazers=1&"
            f"theme=Dark"
        )

        print(f"📥 Downloading from: {socialify_url}")

        # Download the image
        response = requests.get(socialify_url, timeout=30)
        response.raise_for_status()

        # Save the image
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        with open(output_path, 'wb') as f:
            f.write(response.content)

        print(f"✅ Socialify card saved to {output_path}")
        return True

    except Exception as e:
        print(f"⚠️  Error generating Socialify card: {e}")

        # Fallback: Try GitHub OG image
        try:
            og_url = f"https://opengraph.githubassets.com/1/{repo_full_name}"
            print(f"📥 Trying GitHub OG image: {og_url}")

            response = requests.get(og_url, timeout=30)
            response.raise_for_status()

            os.makedirs(os.path.dirname(output_path), exist_ok=True)
            with open(output_path, 'wb') as f:
                f.write(response.content)

            print(f"✅ GitHub OG image saved to {output_path}")
            return True

        except Exception as fallback_error:
            print(f"⚠️  Fallback also failed: {fallback_error}")

            # Last resort: Create a placeholder
            try:
                from PIL import Image, ImageDraw, ImageFont
                img = Image.new('RGB', (1280, 640), color=(13, 17, 23))
                draw = ImageDraw.Draw(img)

                text = f"🚀 {repo_full_name}\n\nView at GitHub"
                draw.text((640, 320), text, fill=(139, 148, 158), anchor="mm")

                os.makedirs(os.path.dirname(output_path), exist_ok=True)
                img.save(output_path)
                print(f"⚠️  Created placeholder image at {output_path}")
            except Exception as img_error:
                print(f"❌ Could not create placeholder: {img_error}")

            return False

def _build_guide_prompt(repo, readme_content):
    """Build the guide generation prompt"""
    return f"""
אתה כותב טכני מקצועי מוביל שמתמחה במדריכי התקנה מתקדמים של כלי AI, LLM, וטכנולוגיות חדשניות.

הריפו: {repo['full_name']}
תיאור: {repo['description']}
כוכבים: {repo['stargazers_count']:,}
שפה: {repo['language']}
URL: {repo['html_url']}

README (קטע):
{readme_content[:4000]}

צור מדריך התקנה **מקצועי, מתקדם וחדשני** בעברית שכולל:

## 📚 מדריך התקנה מקיף ל-{repo['name']}

## 🎯 סקירה כללית
- מה זה הפרויקט ולמה הוא חשוב
- למה {repo['name']} זה game-changer
- תרחישי שימוש מעשיים (3-5 דוגמאות קונקרטיות)
- השוואה לפתרונות אחרים (יתרונות וחסרונות)

## 💻 דרישות מערכת
טבלת דרישות מפורטת:
| רכיב | מינימום | מומלץ |
|------|---------|-------|
| RAM | ... | ... |
| אחסון | ... | ... |
| מעבד | ... | ... |
| מערכת הפעלה | ... | ... |

## 📦 התקנה - שלושת המסלולים

### 🚀 מסלול מהיר (Quick Start)
```bash
# הדרך הכי מהירה להתחיל
[פקודות התקנה מהירות]
```

### 🔧 מסלול מלא (Full Installation)
#### על Linux/macOS:
```bash
# שלב 1: הכנת הסביבה
[פקודות מפורטות עם הסברים]

# שלב 2: התקנת dependencies
[...]

# שלב 3: התקנת {repo['name']}
[...]
```

#### על Windows:
```powershell
# שימוש ב-PowerShell
[פקודות Windows]
```

#### על Termux/Android:
```bash
# התקנה ב-Termux (אם רלוונטי)
[פקודות Termux]
```

### 🐳 מסלול Docker (מומלץ לפרודקשן)
```bash
# שימוש ב-Docker
[Dockerfile או docker-compose]
```

## ⚙️ הגדרה ראשונית
### קובץ הגדרות מומלץ:
```yaml
# config.yaml לדוגמה
[הגדרות מומלצות]
```

### טיוונינג לביצועים:
- אופטימיזציית זיכרון
- שימוש ב-GPU (אם רלוונטי)
- קונפיגורציה למערכות חלשות

## 🎨 שימוש בסיסי - דוגמאות מעשיות

### דוגמה 1: Hello World
```python
# או bash/javascript - תלוי בפרויקט
[קוד לדוגמה פשוט עם הסברים]
```

### דוגמה 2: שימוש מתקדם
```python
# תרחיש מעשי יותר
[קוד מתקדם יותר]
```

### דוגמה 3: אינטגרציה עם כלים אחרים
```python
# איך להשתמש עם API/SDK/כלים נוספים
[קוד אינטגרציה]
```

## 🚀 טיפים מתקדמים וחדשניים

### 💡 טריק 1: [שם הטריק]
[הסבר והדגמה]

### 💡 טריק 2: [שם הטריק]
[הסבר והדגמה]

### 💡 טריק 3: [שם הטריק]
[הסבר והדגמה]

## 🎯 Use Cases מעשיים
1. **[שם Use Case 1]**: [תיאור קצר + דוגמת קוד]
2. **[שם Use Case 2]**: [תיאור קצר + דוגמת קוד]
3. **[שם Use Case 3]**: [תיאור קצר + דוגמת קוד]

## ⚡ ביצועים ואופטימיזציה
- Benchmarks (אם יש)
- טיפים להאצה
- שימוש ביעיל במשאבים

## 🐛 פתרון בעיות נפוצות

### בעיה 1: [שם הבעיה]
**סימפטומים**: [...]
**פתרון**:
```bash
[פקודות לפתרון]
```

### בעיה 2: [שם הבעיה]
**סימפטומים**: [...]
**פתרון**:
```bash
[פקודות לפתרון]
```

## 🔐 אבטחה ו-Best Practices
- [טיפ אבטחה 1]
- [טיפ אבטחה 2]
- [Best practice 1]
- [Best practice 2]

## 🌐 קהילה ומשאבים
- [📖 דוקומנטציה רשמית](link)
- [💬 Discord/Slack/Forum](link)
- [🎓 טיוטוריאלים מומלצים](link)
- [📺 סרטוני הדרכה](link)
- [📝 מאמרים מומלצים](link)

## 🔄 עדכונים וגרסאות
- איך לעדכן לגרסה חדשה
- Changelog חשוב
- Breaking changes (אם יש)

## 💭 מילים לסיום
[סיכום קצר של למה כדאי להשתמש בזה ואיך זה יכול לעזור]

---

**חשוב מאוד**:
1. כתוב בעברית מקצועית וברורה
2. כל בלוק קוד צריך להיות מלווה בהסבר קצר
3. השתמש בטבלאות, רשימות, וקופסאות הערה (> Note:)
4. הוסף אימוג'ים רלוונטיים לכל כותרת (📦 🚀 ⚡ ✅ ⚠️ 💡 🔐 🎯 💻 🌐)
5. בלוקי קוד צריכים syntax highlighting עם שם השפה (```bash, ```python, וכו')
6. תהיה ספציפי ומעשי - תמיד תן דוגמאות קוד אמיתיות
7. הדגש טיפים חדשניים ופחות מוכרים שלא כל אחד יודע
8. התמקד בפרקטיקליות - מה שבאמת עובד בשטח

פורמט: Markdown עשיר עם כותרות ברורות, קופסאות קוד, טבלאות, ורשימות.
"""


def generate_guide_with_gemini(repo, readme_content):
    """Generate comprehensive installation guide using Google Gemini"""
    print(f"🤖 Generating professional guide with Gemini ({GEMINI_MODEL})...")

    if not GOOGLE_API_KEY:
        print("⚠️  No Google API key found!")
        return None

    prompt = _build_guide_prompt(repo, readme_content)

    url = f"https://generativelanguage.googleapis.com/v1beta/models/{GEMINI_MODEL}:generateContent?key={GOOGLE_API_KEY}"

    data = {
        "contents": [{"parts": [{"text": prompt}]}],
        "generationConfig": {
            "temperature": 0.7,
            "maxOutputTokens": 8000
        }
    }

    try:
        response = requests.post(url, json=data, timeout=120)
        response.raise_for_status()

        result = response.json()
        guide_content = result['candidates'][0]['content']['parts'][0]['text']
        print(f"✅ Generated {len(guide_content)} characters of guide content with Gemini")
        return guide_content

    except Exception as e:
        print(f"⚠️  Error generating guide with Gemini: {e}")
        return None


def generate_guide_with_perplexity(repo, readme_content):
    """Generate comprehensive installation guide using Perplexity"""
    print(f"🤖 Generating professional guide with Perplexity ({PERPLEXITY_MODEL})...")

    if not PERPLEXITY_API_KEY:
        print("⚠️  No Perplexity API key found!")
        return None

    prompt = _build_guide_prompt(repo, readme_content)

    url = "https://api.perplexity.ai/chat/completions"
    headers = {
        "Authorization": f"Bearer {PERPLEXITY_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": PERPLEXITY_MODEL,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.7,
        "max_tokens": 8000
    }

    try:
        response = requests.post(url, headers=headers, json=data, timeout=120)
        response.raise_for_status()

        result = response.json()
        guide_content = result['choices'][0]['message']['content']
        print(f"✅ Generated {len(guide_content)} characters of guide content with Perplexity")
        return guide_content

    except Exception as e:
        print(f"⚠️  Error generating guide with Perplexity: {e}")
        return None

def create_jekyll_post(repo, guide_content, screenshot_filename):
    """Create Jekyll blog post with the guide"""
    print("📝 Creating Jekyll blog post...")

    # Generate filename
    date_str = datetime.now().strftime("%Y-%m-%d")
    time_str = datetime.now().strftime("%H-%M")
    repo_name_slug = repo['name'].lower().replace(" ", "-").replace("_", "-")
    filename = f"{date_str}-{repo_name_slug}-guide.md"

    # Escape special chars in title for YAML
    safe_desc = (repo['description'] or repo['name'])[:100].replace('"', '\\"')
    repo_lang = repo['language'].lower() if repo['language'] else 'general'
    license_name = repo.get('license', {}).get('name', 'N/A') if repo.get('license') else 'לא צוין'

    # Escape Liquid syntax in guide content
    import re
    def _wrap_block(match):
        block = match.group(0)
        if '{% raw %}' in block or '{% endraw %}' in block:
            return block
        if '{{' in block or '{%' in block:
            return '{% raw %}\n' + block + '\n{% endraw %}'
        return block
    guide_content = re.sub(r'```[\s\S]*?```', _wrap_block, guide_content, flags=re.MULTILINE)

    # Post metadata
    post_content = f"""---
layout: post-modern
title: "🚀 מדריך מקצועי: {repo['name']} - {safe_desc}"
description: "מדריך התקנה מקיף ומקצועי ל-{repo['name']} עם {repo['stargazers_count']:,} כוכבים. כולל התקנה צעד-אחר-צעד, דוגמאות קוד ו-best practices."
date: {datetime.now().strftime("%Y-%m-%d %H:%M:%S +0200")}
categories: ["AI", "LLM", "מדריכים"]
tags: ["local-ai", "llm", "installation", "{repo_lang}", "{repo['name'].lower()}"]
image: /assets/images/repos/{screenshot_filename}
author: analist0
lang: he
dir: rtl
---

![{repo['name']}](/assets/images/repos/{screenshot_filename})

## 🚀 {repo['name']}

| מדד | ערך |
|-----|-----|
| ⭐ כוכבים | {repo['stargazers_count']:,} |
| 🔧 שפה | {repo['language'] or 'N/A'} |
| 🔱 Forks | {repo['forks_count']:,} |
| 🐛 Issues | {repo['open_issues_count']:,} |
| 📜 רישיון | {license_name} |
| 📅 עדכון אחרון | {repo['updated_at'][:10]} |

[🔗 קישור לריפו]({repo['html_url']}) | [⬇️ הורדה](https://github.com/{repo['full_name']}/archive/refs/heads/main.zip)

---

{guide_content}

---

## 🔗 קישורים שימושיים

- [📖 ריפו ב-GitHub]({repo['html_url']})
- [🐛 Issues & תמיכה]({repo['html_url']}/issues)
- [💬 Discussions]({repo['html_url']}/discussions)
- [📚 Wiki]({repo['html_url']}/wiki)

---

**📝 נכתב על ידי**: analist0 | מומחה אבטחת מידע, בדיקות חדירה ופיתוח
**⏰ עדכון אחרון**: {datetime.now().strftime("%d/%m/%Y %H:%M")}
"""

    # Save post
    posts_dir = Path(__file__).parent.parent / "_posts"
    posts_dir.mkdir(exist_ok=True)

    post_path = posts_dir / filename
    with open(post_path, "w", encoding="utf-8") as f:
        f.write(post_content)

    print(f"✅ Post created: {filename}")
    return filename

def main():
    """Main execution flow"""
    print("=" * 60)
    print("🤖 AI Repository Guide Generator")
    print("=" * 60)

    # 1. Find trending AI repo
    repo = get_trending_ai_repos()
    if not repo:
        print("❌ No suitable AI repository found!")
        sys.exit(1)

    print(f"\n✅ Selected repo: {repo['full_name']}")
    print(f"   ⭐ Stars: {repo['stargazers_count']:,}")
    print(f"   📝 Description: {repo['description']}")

    # 2. Get README content
    readme = get_repo_readme(repo)

    # 3. Generate beautiful Socialify card
    screenshot_dir = Path(__file__).parent.parent / "assets" / "images" / "repos"
    screenshot_dir.mkdir(parents=True, exist_ok=True)

    screenshot_filename = f"{repo['name'].lower()}-{datetime.now().strftime('%Y%m%d')}.png"
    screenshot_path = screenshot_dir / screenshot_filename

    generate_socialify_card(repo['full_name'], str(screenshot_path))

    # 4. Generate guide with Gemini (fallback: Perplexity)
    guide = generate_guide_with_gemini(repo, readme)
    if not guide:
        print("⚠️  Gemini failed, trying Perplexity...")
        guide = generate_guide_with_perplexity(repo, readme)
    if not guide:
        print("❌ Failed to generate guide!")
        sys.exit(1)

    # 5. Create Jekyll post
    post_filename = create_jekyll_post(repo, guide, screenshot_filename)

    print("\n" + "=" * 60)
    print("✅ Guide generation complete!")
    print(f"📄 Post: _posts/{post_filename}")
    print(f"🖼️  Screenshot: assets/images/repos/{screenshot_filename}")
    print("=" * 60)

if __name__ == "__main__":
    main()

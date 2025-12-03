#!/usr/bin/env python3
"""
AI Repository Guide Generator
Finds trending AI/LLM repos and generates professional installation guides using Claude
"""

import os
import sys
import json
import requests
from datetime import datetime, timedelta
from pathlib import Path
import anthropic
from playwright.sync_api import sync_playwright
import time

# Configuration
GITHUB_API = "https://api.github.com"
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN")
ANTHROPIC_API_KEY = os.environ.get("ANTHROPIC_API_KEY")

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

def capture_repo_screenshot(repo_url, output_path):
    """Capture a screenshot of the GitHub repository page"""
    print(f"📸 Capturing screenshot of {repo_url}...")

    try:
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page(viewport={"width": 1280, "height": 1024})

            # Navigate to repo with longer timeout and domcontentloaded instead of networkidle
            page.goto(repo_url, wait_until="domcontentloaded", timeout=60000)

            # Wait a bit for images and content to load
            time.sleep(3)

            # Try to wait for the main content (optional - don't fail if not found)
            try:
                page.wait_for_selector("article.markdown-body", timeout=5000)
            except:
                pass  # Continue anyway

            # Take screenshot
            page.screenshot(path=output_path, full_page=False)

            browser.close()
            print(f"✅ Screenshot saved to {output_path}")
            return True
    except Exception as e:
        print(f"⚠️  Error capturing screenshot: {e}")
        # Create a placeholder image if screenshot fails
        try:
            from PIL import Image, ImageDraw, ImageFont
            img = Image.new('RGB', (1280, 1024), color=(13, 17, 23))
            draw = ImageDraw.Draw(img)

            # Add text: "GitHub Repository Screenshot Failed"
            text = "📸 Screenshot Failed\nView at GitHub"
            draw.text((640, 512), text, fill=(139, 148, 158), anchor="mm")

            os.makedirs(os.path.dirname(output_path), exist_ok=True)
            img.save(output_path)
            print(f"⚠️  Created placeholder image at {output_path}")
        except Exception as img_error:
            print(f"❌ Could not create placeholder: {img_error}")

        return False

def generate_guide_with_claude(repo, readme_content):
    """Generate comprehensive installation guide using Claude"""
    print("🤖 Generating professional guide with Claude...")

    if not ANTHROPIC_API_KEY:
        print("⚠️  No Anthropic API key found!")
        return None

    client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)

    prompt = f"""
אתה כותב טכני מקצועי שמתמחה במדריכי התקנה של כלי AI וLLM מקומיים.

הריפו: {repo['full_name']}
תיאור: {repo['description']}
כוכבים: {repo['stargazers_count']:,}
שפה: {repo['language']}
URL: {repo['html_url']}

README (קטע):
{readme_content[:4000]}

צור מדריך התקנה מקצועי ומקיף **בעברית** שכולל:

1. **סקירה כללית** - מה זה הפרויקט ולמה הוא חשוב
2. **דרישות מערכת** - מה צריך לפני ההתקנה
3. **התקנה צעד אחר צעד**:
   - Linux/Mac
   - Windows
   - Termux/Android (אם רלוונטי)
4. **הגדרה ראשונית** - איך להגדיר אחרי ההתקנה
5. **שימוש בסיסי** - דוגמאות קוד ופקודות
6. **טיפים מתקדמים** - אופטימיזציות וטריקים
7. **פתרון בעיות נפוצות** - troubleshooting
8. **משאבים נוספים** - לינקים למדריכים, דוקומנטציה, קהילה

**חשוב**:
- כתוב בעברית ברורה ומקצועית
- הוסף קטעי קוד עם הסברים
- התמקד במערכות מקומיות (local setup)
- הסבר טכני אך נגיש למתחילים
- השתמש באימוג'ים להמחשה (📦 🚀 ⚡ ✅ ⚠️ 💡)

פורמט: Markdown מובנה עם כותרות והדגשות.
"""

    try:
        message = client.messages.create(
            model="claude-sonnet-4-5-20250929",
            max_tokens=8000,
            messages=[{
                "role": "user",
                "content": prompt
            }]
        )

        guide_content = message.content[0].text
        print(f"✅ Generated {len(guide_content)} characters of guide content")
        return guide_content

    except Exception as e:
        print(f"⚠️  Error generating guide with Claude: {e}")
        return None

def create_jekyll_post(repo, guide_content, screenshot_filename):
    """Create Jekyll blog post with the guide"""
    print("📝 Creating Jekyll blog post...")

    # Generate filename
    date_str = datetime.now().strftime("%Y-%m-%d")
    time_str = datetime.now().strftime("%H-%M")
    repo_name_slug = repo['name'].lower().replace(" ", "-").replace("_", "-")
    filename = f"{date_str}-{repo_name_slug}-guide.md"

    # Post metadata
    post_content = f"""---
layout: post
title: "מדריך מקצועי: {repo['name']} - {repo['description'][:100]}"
date: {datetime.now().strftime("%Y-%m-%d %H:%M:%S +0200")}
categories: [AI, LLM, מדריכים]
tags: [local-ai, llm, installation, {repo['language'].lower() if repo['language'] else 'general'}]
image: /assets/images/repos/{screenshot_filename}
author: AI Guide Bot
lang: he
dir: rtl
---

![{repo['name']}](/assets/images/repos/{screenshot_filename})

# 🚀 {repo['name']}

**⭐ {repo['stargazers_count']:,} כוכבים | 🔧 {repo['language']} | 📅 עדכון אחרון: {repo['updated_at'][:10]}**

[🔗 קישור לריפו]({repo['html_url']}) | [⬇️ הורדה](https://github.com/{repo['full_name']}/archive/refs/heads/main.zip)

---

{guide_content}

---

## 📊 סטטיסטיקות הפרויקט

- **כוכבים**: {repo['stargazers_count']:,} ⭐
- **Forks**: {repo['forks_count']:,} 🔱
- **Issues**: {repo['open_issues_count']:,} 🐛
- **שפה**: {repo['language']} 💻
- **רישיון**: {repo.get('license', {}).get('name', 'N/A') if repo.get('license') else 'לא צוין'} 📜

## 🔗 קישורים שימושיים

- [ריפו ב-GitHub]({repo['html_url']})
- [Issues & תמיכה]({repo['html_url']}/issues)
- [Discussions]({repo['html_url']}/discussions)
- [Wiki]({repo['html_url']}/wiki)

---

*מדריך זה נוצר אוטומטית על ידי AI Guide Bot עם Claude AI*
*עדכון אחרון: {datetime.now().strftime("%d/%m/%Y %H:%M")}*
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

    # 3. Capture screenshot
    screenshot_dir = Path(__file__).parent.parent / "assets" / "images" / "repos"
    screenshot_dir.mkdir(parents=True, exist_ok=True)

    screenshot_filename = f"{repo['name'].lower()}-{datetime.now().strftime('%Y%m%d')}.png"
    screenshot_path = screenshot_dir / screenshot_filename

    capture_repo_screenshot(repo['html_url'], str(screenshot_path))

    # 4. Generate guide with Claude
    guide = generate_guide_with_claude(repo, readme)
    if not guide:
        print("❌ Failed to generate guide with Claude!")
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

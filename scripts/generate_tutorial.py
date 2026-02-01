#!/usr/bin/env python3
"""
🤖 Automatic Tutorial Generator with XAI API
Generates comprehensive technical tutorials on trending topics
"""

import os
import json
import re
import requests
from datetime import datetime
from pathlib import Path
import random

# XAI API Configuration
XAI_API_KEY = os.getenv('XAI_API_KEY')
XAI_API_URL = "https://api.x.ai/v1/chat/completions"
XAI_IMAGE_API_URL = "https://api.x.ai/v1/images/generations"

# Blog directory
BLOG_DIR = Path(os.environ.get('GITHUB_WORKSPACE', Path.cwd()))
POSTS_DIR = BLOG_DIR / '_posts'

# Hot Topics in Tech (English)
HOT_TOPICS = [
    "Building Local AI Assistants with Ollama",
    "Advanced Docker Container Security Best Practices",
    "Creating Serverless APIs with Vercel and Edge Functions",
    "Real-time Data Processing with Apache Kafka",
    "Modern Authentication with OAuth 2.0 and JWT",
    "Building Progressive Web Apps (PWAs) in 2026",
    "GraphQL vs REST: Complete Comparison Guide",
    "Kubernetes Deployment Strategies and Best Practices",
    "Building Microservices with Node.js and Docker",
    "Advanced Git Workflows for Team Collaboration",
    "Building AI Agents with LangChain and LangGraph",
    "Building Real-time Applications with WebSockets",
    "Modern CSS: Grid, Flexbox, and Container Queries",
    "Securing APIs with Rate Limiting and API Keys",
    "Building CLI Tools with Python and Click",
    "Advanced TypeScript Patterns and Best Practices",
    "Creating Chrome Extensions from Scratch",
    "Building REST APIs with FastAPI and Python",
    "Advanced React Hooks and Custom Hooks",
    "Building Data Pipelines with Apache Airflow",
    "Creating Telegram Bots with Python",
    "Advanced SQL Optimization Techniques",
    "Building Discord Bots with Discord.py",
    "Modern State Management with Zustand and Jotai",
    "Creating GitHub Actions CI/CD Pipelines",
    "Building E-commerce with Next.js and Stripe",
    "Advanced MongoDB Aggregation Pipelines",
    "Creating VS Code Extensions",
    "RAG Systems: Building Retrieval Augmented Generation",
    "Advanced Nginx Configuration and Optimization",
    "Building Multi-Agent AI Systems with CrewAI",
    "Vector Databases: Pinecone, Weaviate and Chroma",
    "Fine-tuning LLMs with LoRA and QLoRA",
    "Building Real-time Dashboards with Next.js and D3",
    "Rust for Python Developers: Performance Guide",
]


def escape_liquid_syntax(content):
    """Escape Liquid template syntax in code blocks to prevent Jekyll errors"""

    def wrap_code_block(match):
        code_block = match.group(0)
        if '{% raw %}' in code_block or '{% endraw %}' in code_block:
            return code_block
        if '{{' in code_block or '{%' in code_block:
            return '{% raw %}\n' + code_block + '\n{% endraw %}'
        return code_block

    content = re.sub(r'```[\s\S]*?```', wrap_code_block, content, flags=re.MULTILINE)
    return content


def generate_tutorial(topic):
    """Generate a comprehensive tutorial using XAI API"""

    prompt = f"""צור מדריך טכני מקיף, מפורט וברמה הגבוהה ביותר על הנושא: "{topic}"

דרישות מחמירות:

## 1. אורך ועומק
- לפחות 3500 מילים
- עומק טכני אמיתי - לא שטחי
- כל section צריך להיות substantive

## 2. מבנה מקצועי (השתמש ב-## עבור כותרות ראשיות כדי ליצור תוכן עניינים אוטומטי)

## 🎯 סקירה כללית
- מה הטכנולוגיה ולמה היא חשובה
- 3-5 תרחישי שימוש מהעולם האמיתי
- השוואה קצרה לאלטרנטיבות (טבלה)

## 💻 דרישות מערכת והכנה
- טבלת דרישות מערכת (RAM, CPU, Storage, OS)
- כלים נדרשים + גרסאות
- פקודות הכנה

## 📦 התקנה והגדרה - צעד אחר צעד
- התקנה ב-Linux/macOS
- התקנה ב-Windows
- התקנה עם Docker (אם רלוונטי)
- כל צעד עם דוגמת קוד מלאה

## 🚀 שימוש בסיסי - Hello World
- דוגמת קוד מלאה ועובדת
- הסבר שורה-אחר-שורה

## ⚡ שימוש מתקדם
- 3-4 דוגמאות מתקדמות עם קוד מלא
- Design patterns וארכיטקטורה
- אינטגרציה עם כלים אחרים

## 🏗️ פרויקט מעשי מלא
- פרויקט End-to-End שמדגים את הטכנולוגיה
- קוד מלא ועובד
- הסבר ארכיטקטורה

## ⚙️ אופטימיזציה וביצועים
- טיפים לביצועים
- Benchmarks או השוואות (אם רלוונטי)
- Best Practices

## 🐛 פתרון בעיות נפוצות
- 3-5 בעיות נפוצות עם פתרונות
- פורמט: בעיה -> סימפטומים -> פתרון + קוד

## 🔐 אבטחה ו-Best Practices
- טיפים לאבטחה ספציפיים לטכנולוגיה
- Do's and Don'ts

## 📚 סיכום ומשאבים
- סיכום הנקודות המרכזיות
- צעדים הבאים ללמידה
- קישורים למשאבים (דוקומנטציה, קורסים, קהילות)

## 3. סגנון כתיבה
- מקצועי, טכני אבל נגיש
- כל הטקסט בעברית, קוד ושמות טכניים באנגלית
- הערות בקוד באנגלית
- השתמש באמוג'י בכותרות sections
- השתמש ב-**bold** להדגשות חשובות
- השתמש ב-> blockquotes לטיפים והערות חשובות

## 4. דוגמאות קוד (קריטי!)
- לפחות 8-10 בלוקי קוד
- כל בלוק עם שם שפה: ```python, ```bash, ```javascript, ```yaml וכו'
- קוד מלא ועובד - לא snippets חלקיים
- כלול הערות באנגלית בקוד
- דוגמאות מבסיסי למתקדם

## 5. טבלאות
- לפחות 2-3 טבלאות (השוואות, דרישות, פקודות)
- פורמט markdown תקין: | header | header |

## 6. פורמט
- כתוב MARKDOWN בלבד
- אל תכלול frontmatter (---) - זה יתווסף אוטומטית
- התחל ישר עם התוכן
- ודא שכל בלוק קוד נפתח ונסגר כראוי"""

    try:
        response = requests.post(
            XAI_API_URL,
            headers={
                "Authorization": f"Bearer {XAI_API_KEY}",
                "Content-Type": "application/json"
            },
            json={
                "model": "grok-4-1-fast-reasoning",
                "messages": [
                    {
                        "role": "system",
                        "content": "אתה כותב טכני בכיר ומומחה שיוצר מדריכים מקיפים ומפורטים ברמה הגבוהה ביותר. המדריכים שלך הם ברמה של אתרים כמו DigitalOcean, Real Python ו-freeCodeCamp. אתה כותב בעברית עם קוד ושמות טכניים באנגלית. המדריכים שלך כוללים קוד עובד, טבלאות, דיאגרמות טקסט, ודוגמאות מהעולם האמיתי. אתה לא כותב frontmatter של Jekyll - רק תוכן markdown טהור."
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                "temperature": 0.7,
                "max_tokens": 16000
            },
            timeout=180
        )

        if response.status_code == 200:
            result = response.json()
            content = result['choices'][0]['message']['content']
            # Remove any accidental frontmatter the AI might add
            content = re.sub(r'^---\n[\s\S]*?\n---\n', '', content)
            return content
        else:
            print(f"❌ XAI API Error: {response.status_code}")
            print(f"Response: {response.text[:500]}")
            return None

    except Exception as e:
        print(f"❌ Error calling XAI API: {e}")
        return None


def generate_featured_image(topic):
    """Generate featured image using XAI Image API"""

    image_prompt = f"Professional tech blog featured image about: {topic}. Modern, sleek, futuristic technology theme, high quality digital art, vibrant gradient colors (indigo, purple, cyan), minimalist abstract design, clean and professional, no text overlay, dark background"

    try:
        response = requests.post(
            XAI_IMAGE_API_URL,
            headers={
                "Authorization": f"Bearer {XAI_API_KEY}",
                "Content-Type": "application/json"
            },
            json={
                "model": "grok-2-image",
                "prompt": image_prompt,
                "n": 1,
                "size": "1024x1024"
            },
            timeout=60
        )

        if response.status_code == 200:
            result = response.json()
            image_url = result['data'][0]['url']
            print(f"✅ Generated image: {image_url[:50]}...")
            return image_url
        else:
            print(f"⚠️ Image generation failed: {response.status_code}")
            return None

    except Exception as e:
        print(f"⚠️ Error generating image: {e}")
        return None


def create_post_file(topic, content, image_url=None):
    """Create Jekyll blog post file with professional frontmatter"""

    date = datetime.now()

    # Create safe filename slug
    title_slug = topic.lower()
    title_slug = re.sub(r'[^\w\s-]', '', title_slug).strip()
    title_slug = re.sub(r'[-\s]+', '-', title_slug)[:80]

    filename = f"{date.strftime('%Y-%m-%d')}-{title_slug}.md"
    POSTS_DIR.mkdir(parents=True, exist_ok=True)
    filepath = POSTS_DIR / filename

    # Extract meaningful tags from topic
    tags = re.sub(r'[^\w\s]', '', topic.lower()).split()
    tags = [tag for tag in tags if len(tag) > 3][:8]

    # Escape special YAML characters in title/description
    safe_title = topic.replace('"', '\\"')
    safe_desc = f"מדריך מקיף ומפורט על {topic}. כולל הסברים, דוגמאות קוד מלאות, best practices ופרויקט מעשי.".replace('"', '\\"')

    # Image frontmatter
    image_line = f'\nimage: "{image_url}"' if image_url else ''

    # Escape Liquid syntax in content
    content = escape_liquid_syntax(content)

    frontmatter = f"""---
layout: post-modern
title: "{safe_title}"
description: "{safe_desc}"
date: {date.strftime('%Y-%m-%d %H:%M:%S')} +0200
categories: ["Tutorial", "Development"]
tags: {json.dumps(tags, ensure_ascii=False)}
author: "analist0"
lang: he
dir: rtl{image_line}
---

"""

    full_content = frontmatter + content

    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(full_content)
        print(f"✅ Created: {filepath}")
        return str(filepath)
    except Exception as e:
        print(f"❌ Error creating file: {e}")
        return None


def load_trending_topics():
    """Load trending topics from discover_trending_topics.py output"""
    try:
        with open('trending_topics.json', 'r') as f:
            data = json.load(f)
            topics = data.get('topics', [])
            print(f"📊 Loaded {len(topics)} trending topics from real-time analysis")
            return topics
    except FileNotFoundError:
        print("⚠️ trending_topics.json not found, using fallback topics")
        return []
    except Exception as e:
        print(f"⚠️ Error loading trending topics: {e}")
        return []


def main():
    """Main function"""
    print("🤖 Automatic Tutorial Generator with XAI API")
    print("=" * 60)

    # Check for API key
    if not XAI_API_KEY:
        print("❌ XAI_API_KEY not found!")
        print("Set it with: export XAI_API_KEY='your-key-here'")
        return

    # Get number of tutorials to generate
    try:
        num_tutorials = int(os.getenv('NUM_TUTORIALS', '3'))
    except:
        num_tutorials = 3

    print(f"\n📝 Generating {num_tutorials} tutorials on hot topics...")
    print()

    # Try to load trending topics first
    trending_topics = load_trending_topics()

    if trending_topics and len(trending_topics) >= num_tutorials:
        print("🔥 Using REAL-TIME trending topics!")
        selected_topics = trending_topics[:num_tutorials]
    else:
        print("📚 Using fallback topic list")
        selected_topics = random.sample(HOT_TOPICS, min(num_tutorials, len(HOT_TOPICS)))

    created_files = []

    for i, topic in enumerate(selected_topics, 1):
        print(f"\n[{i}/{num_tutorials}] 🔥 Topic: {topic}")
        print("-" * 60)

        # Generate tutorial
        print("🤖 Generating content with XAI API...")
        content = generate_tutorial(topic)

        if content:
            print(f"✅ Generated {len(content)} characters")

            # Generate featured image
            print("🎨 Generating featured image with XAI Image API...")
            image_url = generate_featured_image(topic)

            # Create post file
            print("📄 Creating blog post file...")
            filepath = create_post_file(topic, content, image_url)

            if filepath:
                created_files.append(filepath)
                print(f"✅ Success! File: {filepath}")
        else:
            print(f"❌ Failed to generate content for: {topic}")

        print()

    # Summary
    print("\n" + "=" * 60)
    print(f"✅ Generated {len(created_files)} tutorials:")
    for filepath in created_files:
        print(f"  - {filepath}")
    print("\n🎉 Done! Ready to commit and push to GitHub.")


if __name__ == '__main__':
    main()

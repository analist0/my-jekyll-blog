#!/usr/bin/env python3
"""
🤖 Automatic Tutorial Generator with XAI API
Generates comprehensive technical tutorials on trending topics
"""

import os
import json
import requests
from datetime import datetime
import random

# XAI API Configuration
XAI_API_KEY = os.getenv('XAI_API_KEY')
XAI_API_URL = "https://api.x.ai/v1/chat/completions"
XAI_IMAGE_API_URL = "https://api.x.ai/v1/images/generations"

# Hot Topics in Tech (English)
HOT_TOPICS = [
    "Building Local AI Assistants with Ollama",
    "Advanced Docker Container Security Best Practices",
    "Creating Serverless APIs with Vercel and Edge Functions",
    "Real-time Data Processing with Apache Kafka",
    "Modern Authentication with OAuth 2.0 and JWT",
    "Building Progressive Web Apps (PWAs) in 2025",
    "GraphQL vs REST: Complete Comparison Guide",
    "Kubernetes Deployment Strategies and Best Practices",
    "Building Microservices with Node.js and Docker",
    "Advanced Git Workflows for Team Collaboration",
    "Creating ChatGPT Plugins and Custom GPTs",
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
    "Building Real-time Dashboards with WebSockets",
    "Advanced Nginx Configuration and Optimization",
]

def generate_tutorial(topic):
    """Generate a comprehensive tutorial using XAI API"""

    prompt = f"""צור מדריך טכני מקיף ומפורט על הנושא: "{topic}"

דרישות:
1. **אורך**: לפחות 3000 מילים (מאוד מפורט ומעמיק)
2. **מבנה**:
   - הקדמה (הסבר חשיבות ומקרי שימוש)
   - דרישות מוקדמות וכלים נדרשים
   - הטמעה צעד-אחר-צעד עם דוגמאות קוד
   - שיטות עבודה מומלצות וטיפים
   - מלכודות נפוצות ואיך להימנע מהן
   - טכניקות מתקדמות
   - דוגמאות מהעולם האמיתי
   - סיכום וצעדים הבאים

3. **סגנון התוכן**:
   - מקצועי וטכני
   - כלול הרבה דוגמאות קוד (Python, JavaScript, Bash, וכו')
   - כלול טבלאות, רשימות ודיאגרמות (כטקסט)
   - הוסף אמוג'י למראה ויזואלי
   - השתמש בעיצוב markdown
   - **חשוב**: כל הטקסט בעברית, אבל קוד באנגלית (כמובן)
   - הערות בקוד באנגלית

4. **דוגמאות קוד**:
   - ספק קטעי קוד שלמים ועובדים
   - כלול הערות והסברים
   - הצג גם דוגמאות בסיסיות וגם מתקדמות
   - כל הקוד באנגלית, אבל ההסברים מעל ומתחת לקוד בעברית

5. **אופטימיזציה לקידום אתרים (SEO)**:
   - כלול מילות מפתח רלוונטיות באופן טבעי
   - הוסף מטא-דאטה בסוף (תגיות, מילות מפתח)

כתוב את המדריך בפורמט MARKDOWN, מוכן לפרסום בבלוג Jekyll.
עשה אותו מאוד מפורט ומקיף - שאף ל-3000+ מילים!

**חשוב מאוד**: כתוב הכל בעברית מלבד קוד ושמות טכניים."""

    try:
        response = requests.post(
            XAI_API_URL,
            headers={
                "Authorization": f"Bearer {XAI_API_KEY}",
                "Content-Type": "application/json"
            },
            json={
                "model": "grok-2-latest",
                "messages": [
                    {
                        "role": "system",
                        "content": "אתה כותב טכני מומחה שיוצר מדריכים מקיפים ומפורטים למפתחים. אתה כותב מדריכים מעמיקים עם הרבה דוגמאות קוד, שיטות עבודה מומלצות, ומקרי שימוש מהעולם האמיתי. המדריכים שלך הם לפחות 3000 מילים ומאוד מפורטים. אתה כותב בעברית אבל קוד ושמות טכניים באנגלית."
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                "temperature": 0.7,
                "max_tokens": 8000,
                "stream": False
            },
            timeout=120
        )

        if response.status_code == 200:
            result = response.json()
            content = result['choices'][0]['message']['content']
            return content
        else:
            print(f"❌ XAI API Error: {response.status_code}")
            print(f"Response: {response.text}")
            return None

    except Exception as e:
        print(f"❌ Error calling XAI API: {e}")
        return None

def generate_featured_image(topic):
    """Generate featured image using XAI Image API"""

    # Create image prompt (in English for better image generation)
    # But describe it as a Hebrew tech blog
    image_prompt = f"Professional Hebrew tech blog featured image about: {topic}. Modern, sleek, futuristic technology theme, high quality digital art, vibrant gradient colors (purple, blue, cyan), minimalist design, clean and professional, 16:9 aspect ratio, no text overlay"

    try:
        response = requests.post(
            XAI_IMAGE_API_URL,
            headers={
                "Authorization": f"Bearer {XAI_API_KEY}",
                "Content-Type": "application/json"
            },
            json={
                "model": "grok-2-vision-1212",
                "prompt": image_prompt,
                "n": 1,
                "size": "1024x1024",
                "quality": "standard"
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
            print(f"Using fallback gradient image")
            return None

    except Exception as e:
        print(f"⚠️ Error generating image: {e}")
        print(f"Using fallback gradient image")
        return None

def create_post_file(topic, content, image_url=None):
    """Create Jekyll blog post file"""

    # Generate filename
    date = datetime.now()
    title_slug = topic.lower()
    title_slug = title_slug.replace(' ', '-')
    title_slug = ''.join(c for c in title_slug if c.isalnum() or c == '-')

    filename = f"{date.strftime('%Y-%m-%d')}-{title_slug}.md"
    filepath = os.path.join('_posts', filename)

    # Use generated image or None (will show gradient fallback)
    featured_image = image_url

    # Extract categories and tags from topic
    categories = ['Tutorial', 'Development']
    tags = topic.lower().replace(':', '').replace('-', ' ').split()
    tags = [tag for tag in tags if len(tag) > 3][:6]

    # Create frontmatter
    if featured_image:
        frontmatter = f"""---
layout: unified-post
title: "{topic}"
description: "Complete comprehensive guide about {topic}. Step-by-step tutorial with code examples, best practices, and real-world use cases."
date: {date.strftime('%Y-%m-%d %H:%M:%S')} +0200
categories: {categories}
tags: {tags}
author: "Tech Insights"
image: "{featured_image}"
image_credit: "Generated with XAI"
image_credit_url: "https://x.ai"
---

"""
    else:
        # No image - will use gradient fallback
        frontmatter = f"""---
layout: unified-post
title: "{topic}"
description: "Complete comprehensive guide about {topic}. Step-by-step tutorial with code examples, best practices, and real-world use cases."
date: {date.strftime('%Y-%m-%d %H:%M:%S')} +0200
categories: {categories}
tags: {tags}
author: "Tech Insights"
---

"""

    # Combine frontmatter and content
    full_content = frontmatter + content

    # Save to file
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(full_content)
        print(f"✅ Created: {filepath}")
        return filepath
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
    if not XAI_API_KEY or XAI_API_KEY.startswith('xai-') == False:
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

#!/usr/bin/env python3
"""
AI Article Generator for Jekyll Blog
Uses X (Twitter) API v2 to find trending AI topics
Generates comprehensive Hebrew articles using OpenAI API
"""

import os
import sys
import json
import requests
from datetime import datetime
from pathlib import Path
import re

# Configuration
X_API_BEARER_TOKEN = os.getenv('X_API_BEARER_TOKEN')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')  # Fallback to OpenAI if needed
ANTHROPIC_API_KEY = os.getenv('ANTHROPIC_API_KEY')  # Claude API

# X API v2 Endpoint
X_API_URL = "https://api.twitter.com/2/tweets/search/recent"

# AI Keywords to search
AI_KEYWORDS = [
    "ChatGPT", "GPT-4", "Claude", "Anthropic", "OpenAI",
    "LLM", "Large Language Model", "Mistral AI", "Llama",
    "Gemini", "Google AI", "DeepMind", "AI breakthrough",
    "machine learning", "deep learning", "neural network",
    "artificial intelligence", "AI model", "AI research",
    "transformer", "diffusion model", "GPT", "local LLM",
    "Ollama", "open source AI", "AI safety", "AGI"
]

def search_trending_ai_topics():
    """Search X (Twitter) for trending AI topics using API v2"""

    if not X_API_BEARER_TOKEN:
        print("⚠️  X_API_BEARER_TOKEN not set, using fallback keywords")
        # Fallback: return top AI keywords
        return [
            "Latest AI Breakthroughs in Machine Learning",
            "Advanced Neural Network Developments",
            "Ethical AI and Responsible Development Trends"
        ]

    headers = {
        "Authorization": f"Bearer {X_API_BEARER_TOKEN}",
        "User-Agent": "AI-Blog-Generator/1.0"
    }

    # Search query - combined AI keywords
    query = " OR ".join(AI_KEYWORDS[:10])  # Use first 10 keywords to avoid query length limit

    params = {
        "query": f"({query}) -is:retweet lang:en",
        "max_results": 100,
        "tweet.fields": "public_metrics,created_at",
        "sort_order": "relevancy"
    }

    try:
        response = requests.get(X_API_URL, headers=headers, params=params, timeout=15)
        response.raise_for_status()
        data = response.json()

        if "data" not in data or not data["data"]:
            print("⚠️  No tweets found, using fallback topics")
            return [
                "Latest AI Breakthroughs in Machine Learning",
                "Advanced Neural Network Developments",
                "Ethical AI and Responsible Development Trends"
            ]

        # Analyze tweets and extract trending topics
        topics = analyze_tweets(data["data"])
        return topics[:3]  # Top 3 topics

    except Exception as e:
        print(f"❌ Error fetching from X API: {e}")
        # Fallback topics
        return [
            "Latest AI Breakthroughs in Machine Learning",
            "Advanced Neural Network Developments",
            "Ethical AI and Responsible Development Trends"
        ]

def analyze_tweets(tweets):
    """Analyze tweets to extract trending topics"""
    # Simple analysis: extract most common phrases
    topics = {}

    for tweet in tweets:
        text = tweet.get("text", "")

        # Extract potential topics (simplified)
        for keyword in AI_KEYWORDS:
            if keyword.lower() in text.lower():
                if keyword not in topics:
                    topics[keyword] = 0
                topics[keyword] += 1

    # Sort by frequency
    sorted_topics = sorted(topics.items(), key=lambda x: x[1], reverse=True)

    # Generate topic titles
    topic_titles = []
    for topic, count in sorted_topics[:5]:
        if "GPT" in topic or "Claude" in topic:
            topic_titles.append(f"Latest Developments in {topic} Technology")
        elif "AI" in topic:
            topic_titles.append(f"Breaking News: {topic} Innovations")
        else:
            topic_titles.append(f"Deep Dive: {topic} in Modern AI")

    return topic_titles if topic_titles else [
        "Latest AI Breakthroughs in Machine Learning",
        "Advanced Neural Network Developments",
        "Ethical AI and Responsible Development Trends"
    ]

def generate_article_content(topic):
    """Generate comprehensive Hebrew article using AI"""

    prompt = f"""כתוב מאמר מקיף ומקצועי בעברית על הנושא: "{topic}"

הדרישות:
1. מאמר באורך 1500-2000 מילים
2. כתיבה מקצועית ברמה גבוהה
3. הסברים מפורטים ועומק טכני
4. מבנה ברור עם כותרות משנה (H2, H3)
5. דוגמאות מעשיות ומקרי שימוש
6. פסקת פתיחה מרתקת
7. סיכום מקיף בסוף
8. שימוש ב-markdown לעיצוב
9. קוד לדוגמה במידת הצורך (עם הסברים)
10. התייחסות למגמות עדכניות ב-AI

המאמר צריך לכלול:
- הקדמה מעניינת שמושכת את הקורא
- הסבר מה הטכנולוגיה/נושא ומדוע הוא חשוב
- הסבר טכני מעמיק אך נגיש
- יישומים מעשיים ודוגמאות
- השוואות למוצרים/טכנולוגיות אחרות
- אתגרים והזדמנויות
- מגמות עתידיות
- סיכום חזק

כתוב בעברית תקנית, מקצועית, עם סגנון כתיבה מושך ונעים לקריאה.
"""

    # Try Claude API first (better for Hebrew)
    if ANTHROPIC_API_KEY:
        try:
            response = requests.post(
                "https://api.anthropic.com/v1/messages",
                headers={
                    "x-api-key": ANTHROPIC_API_KEY,
                    "anthropic-version": "2023-06-01",
                    "content-type": "application/json"
                },
                json={
                    "model": "claude-3-5-sonnet-20241022",
                    "max_tokens": 4000,
                    "messages": [{"role": "user", "content": prompt}]
                },
                timeout=60
            )
            response.raise_for_status()
            data = response.json()
            content = data["content"][0]["text"]
            print("✅ Generated article using Claude API")
            return content
        except Exception as e:
            print(f"⚠️  Claude API failed: {e}")

    # Fallback to OpenAI
    if OPENAI_API_KEY:
        try:
            response = requests.post(
                "https://api.openai.com/v1/chat/completions",
                headers={
                    "Authorization": f"Bearer {OPENAI_API_KEY}",
                    "Content-Type": "application/json"
                },
                json={
                    "model": "gpt-4-turbo-preview",
                    "messages": [{"role": "user", "content": prompt}],
                    "max_tokens": 3000,
                    "temperature": 0.7
                },
                timeout=60
            )
            response.raise_for_status()
            data = response.json()
            content = data["choices"][0]["message"]["content"]
            print("✅ Generated article using OpenAI API")
            return content
        except Exception as e:
            print(f"⚠️  OpenAI API failed: {e}")

    # Final fallback: template article
    print("⚠️  Using template article (no API keys available)")
    return generate_template_article(topic)

def generate_template_article(topic):
    """Generate a template article when APIs are unavailable"""
    return f"""# {topic}

## מבוא

עולם הבינה המלאכותית ממשיך להתפתח בקצב מהיר, והנושא של **{topic}** הוא אחד התחומים המרתקים והחשובים ביותר כיום.

## מה זה {topic}?

{topic} מייצג התקדמות משמעותית בתחום הבינה המלאכותית. טכנולוגיה זו משנה את הדרך בה אנחנו חושבים על מערכות AI ויישומיהן בעולם המודרני.

### היסטוריה קצרה

הפיתוח של טכנולוגיות AI עבר דרך ארוכה, מתקופת המחקר המוקדם ב-1950s ועד להתפתחויות המודרניות של היום.

## יישומים מעשיים

טכנולוגיה זו משמשת במגוון תחומים:

1. **עיבוד שפה טבעית (NLP)** - הבנת טקסט ושיחה אנושית
2. **ראייה ממוחשבת** - זיהוי תמונות ווידאו
3. **למידה מתמשכת** - שיפור ביצועים לאורך זמן
4. **מערכות המלצה** - התאמה אישית לכל משתמש

## אתגרים

למרות ההתקדמות המרשימה, עדיין קיימים אתגרים:

- **עלויות חישוב גבוהות** - אימון מודלים גדולים דורש משאבים רבים
- **איכות נתונים** - תלות בנתוני אימון איכותיים
- **שקיפות והסברים** - הבנת החלטות המודל
- **אתיקה ופרטיות** - שמירה על ערכים אנושיים

## מגמות עתידיות

העתיד נראה מבטיח עם:

- מודלים חסכוניים ויעילים יותר
- AI מקומי (Local LLMs)
- שילוב טוב יותר עם מערכות קיימות
- נגישות רחבה יותר למפתחים

## סיכום

{topic} הוא תחום מרתק בעולם ה-AI שממשיך להתפתח. ההבנה של הטכנולוגיות הללו חיונית לכל מי שמעוניין להישאר מעודכן בעולם הטכנולוגיה המודרנית.

---

*מאמר זה עודכן ב-{datetime.now().strftime("%d.%m.%Y")}*
"""

def create_jekyll_post(topic, content, index):
    """Create Jekyll post file with proper front matter"""

    # Create filename
    date_str = datetime.now().strftime("%Y-%m-%d")
    time_str = datetime.now().strftime("%H%M%S")
    slug = re.sub(r'[^a-z0-9]+', '-', topic.lower())
    slug = slug.strip('-')[:50]  # Limit length

    filename = f"{date_str}-{slug}---{time_str}-{index}.md"

    # Generate tags
    tags = ["AI", "בינה מלאכותית", "טכנולוגיה", "Machine Learning"]
    if "GPT" in topic:
        tags.append("GPT")
    if "neural" in topic.lower():
        tags.extend(["Neural Networks", "רשתות נוירונים"])
    if "ethical" in topic.lower():
        tags.extend(["AI Ethics", "אתיקה"])

    # Front matter
    front_matter = f"""---
layout: post
title: "{topic}"
date: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")} +0300
categories: ["AI", "Technology"]
tags: {json.dumps(tags, ensure_ascii=False)}
author: "analist0"
description: "מאמר מקיף על {topic} - הטכנולוגיה, היישומים, והמגמות העדכניות בתחום הבינה המלאכותית"
excerpt: "{content[:200].replace(chr(10), ' ')}..."
---

"""

    # Combine front matter and content
    full_content = front_matter + content

    # Write to _posts directory
    posts_dir = Path(__file__).parent.parent / "_posts"
    posts_dir.mkdir(exist_ok=True)

    filepath = posts_dir / filename
    filepath.write_text(full_content, encoding='utf-8')

    print(f"✅ Created post: {filename}")
    return filename

def main():
    """Main function"""
    print("🤖 AI Article Generator Starting...")
    print("=" * 50)

    # Step 1: Search trending topics
    print("\n📊 Step 1: Searching trending AI topics on X...")
    topics = search_trending_ai_topics()
    print(f"✅ Found {len(topics)} topics:")
    for i, topic in enumerate(topics, 1):
        print(f"   {i}. {topic}")

    # Step 2: Generate articles
    print("\n✍️  Step 2: Generating articles...")
    created_files = []

    for index, topic in enumerate(topics):
        print(f"\n📝 Generating article {index + 1}/{len(topics)}: {topic}")
        try:
            content = generate_article_content(topic)
            filename = create_jekyll_post(topic, content, index)
            created_files.append(filename)
            print(f"   ✅ Success: {filename}")
        except Exception as e:
            print(f"   ❌ Error: {e}")
            continue

    # Step 3: Summary
    print("\n" + "=" * 50)
    print(f"✅ Generated {len(created_files)} articles:")
    for filename in created_files:
        print(f"   • {filename}")

    print("\n🎉 Article generation complete!")
    return 0

if __name__ == "__main__":
    sys.exit(main())

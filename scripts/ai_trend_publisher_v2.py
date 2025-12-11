#!/usr/bin/env python3
"""
Advanced AI Trend Publisher v2.0
Searches X (Twitter) for REAL trending topics and generates 3 unique professional posts per day
"""

import os
import sys
import json
import requests
import random
from datetime import datetime
from pathlib import Path
import re
import time

# API Configuration
XAI_API_KEY = os.environ.get('XAI_API_KEY', '')
X_BEARER_TOKEN = os.environ.get('X_BEARER_TOKEN', '')

# Blog configuration
BLOG_DIR = Path.home() / 'my-jekyll-blog'
POSTS_DIR = BLOG_DIR / '_posts'

# Search categories (varied to avoid repetition)
TECH_CATEGORIES = [
    # AI & ML
    ("artificial intelligence breakthrough", "בינה מלאכותית"),
    ("machine learning innovation", "למידת מכונה"),
    ("large language models", "מודלי שפה גדולים"),
    ("computer vision AI", "ראייה ממוחשבת"),
    ("generative AI", "AI גנרטיבי"),

    # Development
    ("web development trends", "פיתוח אתרים"),
    ("react javascript framework", "React"),
    ("python programming", "תכנות Python"),
    ("devops automation", "DevOps"),
    ("cloud computing", "cloud"),

    # Emerging Tech
    ("blockchain cryptocurrency", "בלוקצ'יין"),
    ("quantum computing", "מחשוב קוונטי"),
    ("cybersecurity", "אבטחת מידע"),
    ("edge computing IoT", "Edge Computing"),
    ("5G technology", "טכנולוגיית 5G"),

    # Data & Infrastructure
    ("kubernetes docker", "Kubernetes"),
    ("microservices architecture", "מיקרוסרוויסים"),
    ("serverless computing", "Serverless"),
    ("data science analytics", "מדע הנתונים"),
    ("big data processing", "Big Data"),
]

# Post times (morning, afternoon, evening)
POST_SCHEDULES = [
    ("08:00:00", "morning", "בוקר"),
    ("14:00:00", "afternoon", "צהריים"),
    ("20:00:00", "evening", "ערב"),
]


def search_x_trending(query: str, max_results: int = 20):
    """
    Search X (Twitter) for trending topics

    Args:
        query: Search query
        max_results: Number of results to fetch

    Returns:
        list: Trending tweets sorted by engagement
    """

    if not X_BEARER_TOKEN:
        print(f"⚠️  X_BEARER_TOKEN not set, using fallback")
        return None

    url = "https://api.twitter.com/2/tweets/search/recent"

    headers = {
        "Authorization": f"Bearer {X_BEARER_TOKEN}"
    }

    params = {
        "query": f"{query} -is:retweet lang:en",
        "max_results": min(max_results, 100),
        "tweet.fields": "public_metrics,created_at,author_id",
        "expansions": "author_id",
        "user.fields": "username,verified"
    }

    try:
        response = requests.get(url, headers=headers, params=params, timeout=15)
        response.raise_for_status()

        data = response.json()

        if 'data' not in data or not data['data']:
            return None

        # Calculate engagement score
        tweets = []
        for tweet in data['data']:
            metrics = tweet.get('public_metrics', {})
            engagement = (
                metrics.get('like_count', 0) * 1.0 +
                metrics.get('retweet_count', 0) * 2.0 +
                metrics.get('reply_count', 0) * 1.5 +
                metrics.get('quote_count', 0) * 2.5
            )

            tweets.append({
                'text': tweet['text'],
                'engagement': engagement,
                'created_at': tweet.get('created_at'),
                'id': tweet['id']
            })

        # Sort by engagement
        tweets.sort(key=lambda x: x['engagement'], reverse=True)

        return tweets

    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 429:
            print(f"⚠️  X API rate limit exceeded")
        else:
            print(f"⚠️  X API error: {e}")
        return None

    except Exception as e:
        print(f"⚠️  Search failed: {e}")
        return None


def generate_post_with_xai(topic: str, category_he: str, time_slot: str):
    """
    Generate professional blog post using X.AI Grok

    Args:
        topic: Topic from X or fallback
        category_he: Hebrew category name
        time_slot: Time of day (morning/afternoon/evening)

    Returns:
        dict: Post data
    """

    if not XAI_API_KEY:
        return {
            'success': False,
            'error': 'XAI_API_KEY not set'
        }

    # Time-based writing style
    style_prompts = {
        "morning": "energetic and inspirational tone, focus on getting started and learning",
        "afternoon": "informative and practical tone, focus on implementation and best practices",
        "evening": "thoughtful and analytical tone, focus on advanced concepts and future trends"
    }

    style = style_prompts.get(time_slot, "professional and informative")

    prompt = f"""
You are a top-tier tech blogger writing for Israeli developers and tech professionals.

Topic: {topic}
Category: {category_he}
Style: {style}

Create a COMPREHENSIVE, PROFESSIONAL blog post (1800-2500 words) with:

1. **Title (Hebrew)** - exciting, SEO-friendly, clickable
2. **English Title** - for URL slug
3. **Description (Hebrew)** - 1-2 sentences
4. **Full Content in HEBREW** including:
   - Engaging intro (2-3 paragraphs)
   - Clear structure with ## headers
   - 3-5 main sections
   - **At least 3 code examples** (real, working code)
   - Practical examples and use cases
   - Best practices and tips
   - Current industry trends
   - Conclusion with actionable takeaways
5. **5-7 relevant tags** (Hebrew and English mix)
6. **Category** (Hebrew)

Requirements:
- Write in HEBREW (עברית)
- Include REAL, WORKING code examples in:
  * Python, JavaScript, Bash, or relevant language
  * Full code blocks with ```language notation
  * Commented and explained
- Make it mobile-friendly
- Use markdown formatting:
  * ## headers for sections
  * **bold** for emphasis
  * `code` for inline code
  * ```language for code blocks
  * Lists and bullet points
- Professional but accessible
- SEO optimized

Code blocks MUST be formatted like this:
```python
# Example code
def function():
    return "value"
```

Return ONLY valid JSON:
{{
  "title_he": "כותרת בעברית מרגשת",
  "title_en": "english-slug-title",
  "description": "תיאור קצר בעברית",
  "content": "תוכן מלא במארקדאון עם בלוקי קוד",
  "tags": ["תג1", "tag2", "עברית", "english"],
  "category": "קטגוריה בעברית"
}}

IMPORTANT: Return ONLY the JSON, no markdown formatting around it!
"""

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {XAI_API_KEY}"
    }

    payload = {
        "model": "grok-4-1-fast-reasoning",
        "messages": [
            {
                "role": "system",
                "content": "You are an expert tech blogger. Return ONLY valid JSON without markdown code blocks."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        "temperature": 0.85,
        "max_tokens": 4500
    }

    try:
        print(f"   Calling X.AI API...")
        response = requests.post(
            "https://api.x.ai/v1/chat/completions",
            headers=headers,
            json=payload,
            timeout=90
        )
        response.raise_for_status()

        data = response.json()

        if 'choices' not in data or not data['choices']:
            return {'success': False, 'error': 'No response from X.AI'}

        content = data['choices'][0]['message']['content'].strip()

        # Remove markdown code blocks if present
        content = re.sub(r'^```json\s*', '', content)
        content = re.sub(r'\s*```$', '', content)

        # Parse JSON
        post_data = json.loads(content)
        post_data['success'] = True
        post_data['time_slot'] = time_slot

        return post_data

    except json.JSONDecodeError as e:
        return {
            'success': False,
            'error': f'JSON parse error: {e}',
            'raw_content': content[:500]
        }

    except Exception as e:
        return {
            'success': False,
            'error': f'X.AI API error: {e}'
        }


def create_jekyll_post(post_data: dict, slot_index: int):
    """
    Create Jekyll post file

    Args:
        post_data: Post content from X.AI
        slot_index: 0=morning, 1=afternoon, 2=evening

    Returns:
        str: Created file path
    """

    now = datetime.now()
    date_str = now.strftime('%Y-%m-%d')

    time, slot_name, slot_he = POST_SCHEDULES[slot_index]

    # Create URL-friendly slug
    slug = post_data.get('title_en', 'tech-post')
    slug = re.sub(r'[^\w\s-]', '', slug).strip().lower()
    slug = re.sub(r'[-\s]+', '-', slug)

    # Add time to avoid duplicates
    filename = f"{date_str}-{slug}-{slot_name}.md"
    filepath = POSTS_DIR / filename

    # Ensure directory exists
    POSTS_DIR.mkdir(parents=True, exist_ok=True)

    # Create frontmatter
    frontmatter = f"""---
layout: post-modern
title: "{post_data.get('title_he', 'פוסט חדש')}"
description: "{post_data.get('description', '')}"
date: {date_str} {time} +0200
author: analist0
category: "{post_data.get('category', 'טכנולוגיה')}"
tags: {json.dumps(post_data.get('tags', []), ensure_ascii=False)}
generate_image: true
time_slot: {slot_he}
---

"""

    # Full content
    full_content = frontmatter + post_data.get('content', '')

    # Write file
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(full_content)

    print(f"   ✅ Created: {filename}")
    return str(filepath)


def generate_daily_posts():
    """
    Main function - generates 3 unique posts per day
    """

    print("=" * 80)
    print("🚀 AI Trend Publisher v2.0 - Professional Blog Post Generator")
    print("=" * 80)
    print()

    # Check API keys
    if not XAI_API_KEY:
        print("❌ XAI_API_KEY not set!")
        print("   Set: export XAI_API_KEY='xai-...'")
        sys.exit(1)

    if not X_BEARER_TOKEN:
        print("⚠️  X_BEARER_TOKEN not set - using fallback topics")
        print("   For better results, set: export X_BEARER_TOKEN='AAAAAAAAAAAAAAAAAAAAANRILgA...'")
        print()

    # Determine current time slot
    now = datetime.now()
    current_hour = now.hour

    # Map hour to slot
    if current_hour < 12:
        slot_index = 0  # Morning
    elif current_hour < 18:
        slot_index = 1  # Afternoon
    else:
        slot_index = 2  # Evening

    time_str, slot_name, slot_he = POST_SCHEDULES[slot_index]

    print(f"📅 Date: {now.strftime('%Y-%m-%d')}")
    print(f"⏰ Time Slot: {slot_he.upper()} ({slot_name})")
    print()

    # Select 3 DIFFERENT random categories
    selected_categories = random.sample(TECH_CATEGORIES, 3)

    posts_created = []

    for i, (search_query, category_he) in enumerate(selected_categories, 1):
        print(f"\n{'─' * 80}")
        print(f"📝 POST {i}/3: {category_he}")
        print(f"{'─' * 80}")

        # Search X for trending topics
        print(f"🔍 Searching X for: '{search_query}'...")

        trending_tweets = search_x_trending(search_query, max_results=20)

        if trending_tweets and len(trending_tweets) > 0:
            # Pick top trending tweet
            top_tweet = trending_tweets[0]
            topic = top_tweet['text'][:200]  # Limit length
            engagement = top_tweet['engagement']

            print(f"   ✅ Found trending topic!")
            print(f"   💬 Engagement: {int(engagement)} points")
            print(f"   📄 Topic: {topic[:80]}...")
        else:
            # Fallback topic
            topic = f"Latest developments in {search_query}"
            print(f"   ⚠️  Using fallback topic: {topic}")

        print()

        # Generate post with X.AI
        print(f"🤖 Generating professional post with X.AI...")
        post_data = generate_post_with_xai(topic, category_he, slot_name)

        if not post_data.get('success'):
            print(f"   ❌ Failed: {post_data.get('error')}")
            print(f"   Skipping post {i}")
            continue

        print(f"   ✅ Generated!")
        print(f"   📝 Title: {post_data.get('title_he')}")
        print(f"   📊 Content length: {len(post_data.get('content', ''))} chars")
        print(f"   🏷️  Tags: {', '.join(post_data.get('tags', [])[:3])}...")

        print()

        # Create Jekyll file
        print(f"💾 Creating Jekyll post file...")
        filepath = create_jekyll_post(post_data, slot_index)

        posts_created.append({
            'file': filepath,
            'title': post_data.get('title_he'),
            'category': category_he
        })

        # Rate limiting - wait between API calls
        if i < 3:
            print(f"   ⏳ Waiting 10 seconds before next post...")
            time.sleep(10)

    print()
    print("=" * 80)
    print(f"✅ COMPLETED: {len(posts_created)}/3 posts created successfully!")
    print("=" * 80)
    print()

    if posts_created:
        print("📄 Created Posts:")
        for i, post in enumerate(posts_created, 1):
            print(f"   {i}. {post['title']} ({post['category']})")
            print(f"      File: {Path(post['file']).name}")

        print()
        print("🎨 Next Steps:")
        print("   1. Review posts in _posts/ directory")
        print("   2. Generate hero images:")
        for post in posts_created:
            print(f"      python3 scripts/generate_ai_image.py {post['file']}")
        print("   3. Commit and push to GitHub")
        print(f"   4. Next scheduled run: {POST_SCHEDULES[(slot_index + 1) % 3][2]} ({POST_SCHEDULES[(slot_index + 1) % 3][0]})")
    else:
        print("⚠️  No posts were created. Check errors above.")
        sys.exit(1)


if __name__ == '__main__':
    try:
        generate_daily_posts()
    except KeyboardInterrupt:
        print("\n\n⚠️  Interrupted by user")
        sys.exit(130)
    except Exception as e:
        print(f"\n❌ Fatal error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

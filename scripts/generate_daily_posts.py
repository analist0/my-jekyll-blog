#!/usr/bin/env python3
"""
Automated Daily Blog Post Generator
Searches X (Twitter) for trending topics and generates 3 professional blog posts per day
"""

import os
import sys
import json
import requests
from datetime import datetime, timedelta
from pathlib import Path
import re

# API Configuration
XAI_API_KEY = os.environ.get('XAI_API_KEY', '')
X_API_KEY = os.environ.get('X_API_KEY', '')
X_API_SECRET = os.environ.get('X_API_SECRET', '')
X_ACCESS_TOKEN = os.environ.get('X_ACCESS_TOKEN', '')
X_ACCESS_TOKEN_SECRET = os.environ.get('X_ACCESS_TOKEN_SECRET', '')

# Post times (morning, afternoon, evening)
POST_TIMES = [
    ("08:00", "morning"),
    ("14:00", "afternoon"),
    ("20:00", "evening")
]

# Categories to search (varied topics)
SEARCH_CATEGORIES = [
    "artificial intelligence",
    "machine learning",
    "web development",
    "blockchain crypto",
    "cybersecurity",
    "cloud computing",
    "devops automation",
    "mobile development",
    "data science",
    "quantum computing",
    "AR VR metaverse",
    "edge computing",
    "kubernetes docker",
    "serverless",
    "microservices"
]


def get_x_bearer_token():
    """Get X API Bearer token"""
    if X_API_KEY and X_API_SECRET:
        credentials = f"{X_API_KEY}:{X_API_SECRET}"
        import base64
        encoded = base64.b64encode(credentials.encode()).decode()

        response = requests.post(
            'https://api.twitter.com/oauth2/token',
            headers={
                'Authorization': f'Basic {encoded}',
                'Content-Type': 'application/x-www-form-urlencoded'
            },
            data={'grant_type': 'client_credentials'}
        )

        if response.status_code == 200:
            return response.json()['access_token']

    return None


def search_trending_topics(category: str, count: int = 10):
    """
    Search X (Twitter) for trending topics in a category

    Args:
        category: Category to search
        count: Number of results

    Returns:
        list: Trending tweets/topics
    """

    bearer_token = get_x_bearer_token()

    if not bearer_token:
        print(f"⚠️  X API not configured, using fallback topics")
        return generate_fallback_topics(category)

    # X API v2 search
    url = "https://api.twitter.com/2/tweets/search/recent"

    headers = {
        "Authorization": f"Bearer {bearer_token}"
    }

    params = {
        "query": f"{category} -is:retweet lang:en",
        "max_results": count,
        "tweet.fields": "public_metrics,created_at",
        "sort_order": "relevancy"
    }

    try:
        response = requests.get(url, headers=headers, params=params, timeout=10)
        response.raise_for_status()

        data = response.json()

        if 'data' in data:
            # Sort by engagement (likes + retweets)
            tweets = data['data']
            for tweet in tweets:
                metrics = tweet.get('public_metrics', {})
                tweet['engagement'] = metrics.get('like_count', 0) + metrics.get('retweet_count', 0)

            tweets.sort(key=lambda x: x['engagement'], reverse=True)
            return tweets[:count]

        return generate_fallback_topics(category)

    except Exception as e:
        print(f"⚠️  X API search failed: {e}")
        return generate_fallback_topics(category)


def generate_fallback_topics(category: str):
    """Generate fallback topics when X API is unavailable"""

    fallback_topics = {
        "artificial intelligence": [
            "GPT-5 breakthrough in natural language understanding",
            "AI agents revolutionizing software development",
            "Multimodal AI models changing content creation",
        ],
        "machine learning": [
            "Advanced MLOps practices for production systems",
            "Federated learning for privacy-preserving AI",
            "AutoML democratizing machine learning",
        ],
        "web development": [
            "React 19 Server Components in production",
            "Modern CSS features replacing JavaScript libraries",
            "Web Performance optimization techniques 2025",
        ],
        "blockchain crypto": [
            "Ethereum scalability solutions update",
            "Real-world blockchain use cases beyond finance",
            "Zero-knowledge proofs explained",
        ],
        "cybersecurity": [
            "AI-powered threat detection systems",
            "Zero Trust security architecture guide",
            "Quantum-resistant cryptography preparation",
        ]
    }

    topics = fallback_topics.get(category, [
        f"Latest trends in {category}",
        f"Advanced {category} techniques",
        f"Future of {category} technology"
    ])

    return [{"text": topic, "engagement": 0} for topic in topics]


def generate_post_with_xai(topic: str, category: str, time_slot: str):
    """
    Generate a professional blog post using X.AI

    Args:
        topic: Topic extracted from X
        category: Category of the post
        time_slot: morning/afternoon/evening

    Returns:
        dict: Post data including title, content, code examples
    """

    if not XAI_API_KEY:
        return {
            'success': False,
            'error': 'XAI_API_KEY not configured'
        }

    prompt = f"""
You are a professional tech blogger writing for a modern tech blog.

Create a comprehensive, professional blog post about: "{topic}"

Category: {category}
Target audience: Developers and tech professionals
Length: 1500-2000 words

The post MUST include:

1. **Engaging Title** (Hebrew) - exciting and clickable
2. **Brief Introduction** (2-3 paragraphs)
3. **Main Content** with:
   - Clear structure with ## headers
   - Real-world examples
   - Best practices
   - At least 2-3 code examples (Python, JavaScript, or Bash)
   - Practical tips
4. **Conclusion** with key takeaways
5. **Description** (1-2 sentences for meta)
6. **5 relevant tags**

Format the code blocks like this:
```language
code here
```

Make it:
- Professional but accessible
- Include REAL, working code examples
- Mobile-friendly formatting
- SEO optimized
- Practical and actionable

Return in JSON format:
{{
  "title_he": "כותרת בעברית",
  "title_en": "Title in English",
  "description": "Short description",
  "content": "Full markdown content with code blocks",
  "tags": ["tag1", "tag2", "tag3", "tag4", "tag5"],
  "category": "category"
}}
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
                "content": "You are an expert tech blogger who writes professional, code-heavy technical articles in Hebrew and English."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        "temperature": 0.8,
        "max_tokens": 4000
    }

    try:
        response = requests.post(
            "https://api.x.ai/v1/chat/completions",
            headers=headers,
            json=payload,
            timeout=60
        )
        response.raise_for_status()

        data = response.json()

        if 'choices' in data and len(data['choices']) > 0:
            content = data['choices'][0]['message']['content']

            # Extract JSON from response
            json_match = re.search(r'\{[\s\S]*\}', content)
            if json_match:
                post_data = json.loads(json_match.group())
                post_data['success'] = True
                post_data['time_slot'] = time_slot
                return post_data

            return {
                'success': False,
                'error': 'Failed to parse JSON from response',
                'raw_content': content
            }

        return {
            'success': False,
            'error': 'No content generated',
            'response': data
        }

    except Exception as e:
        return {
            'success': False,
            'error': f'X.AI API error: {str(e)}'
        }


def create_jekyll_post(post_data: dict, date: datetime, time: str):
    """
    Create Jekyll blog post file

    Args:
        post_data: Post content from X.AI
        date: Post date
        time: Post time (HH:MM)

    Returns:
        str: Path to created post file
    """

    # Generate filename
    date_str = date.strftime('%Y-%m-%d')
    title_slug = re.sub(r'[^\w\s-]', '', post_data.get('title_en', 'post'))
    title_slug = re.sub(r'[-\s]+', '-', title_slug).lower()
    filename = f"{date_str}-{title_slug}.md"

    posts_dir = Path(os.environ.get('GITHUB_WORKSPACE', Path.cwd())) / '_posts'
    posts_dir.mkdir(parents=True, exist_ok=True)

    filepath = posts_dir / filename

    # Create frontmatter
    frontmatter = f"""---
layout: post-modern
title: "{post_data.get('title_he', 'פוסט חדש')}"
description: "{post_data.get('description', '')}"
date: {date_str} {time}:00 +0200
author: analist0
category: "{post_data.get('category', 'טכנולוגיה')}"
tags: {json.dumps(post_data.get('tags', []), ensure_ascii=False)}
generate_image: true
---

"""

    # Full content
    content = frontmatter + post_data.get('content', '')

    # Write file
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"✅ Created post: {filename}")
    return str(filepath)


def main():
    """
    Main function - generates 3 posts per day based on time slot
    """

    print("🚀 Daily Blog Post Generator")
    print("=" * 60)

    # Check API keys
    if not XAI_API_KEY:
        print("❌ XAI_API_KEY not set!")
        print("   Set it: export XAI_API_KEY='xai-your-key'")
        sys.exit(1)

    # Determine which time slot we're in
    now = datetime.now()
    current_time = now.strftime("%H:%M")

    # Find the next time slot
    time_slot_index = 0
    for i, (time, slot) in enumerate(POST_TIMES):
        if current_time < time:
            time_slot_index = i
            break
    else:
        time_slot_index = 0  # After evening, prepare for next morning

    selected_time, selected_slot = POST_TIMES[time_slot_index]

    print(f"📅 Date: {now.strftime('%Y-%m-%d')}")
    print(f"⏰ Time Slot: {selected_slot.upper()} ({selected_time})")
    print()

    # Select random category
    import random
    category = random.choice(SEARCH_CATEGORIES)

    print(f"🔍 Searching X for trending topics in: {category}")
    topics = search_trending_topics(category, count=5)

    if not topics:
        print("❌ No topics found")
        sys.exit(1)

    # Select top topic
    top_topic = topics[0]
    topic_text = top_topic.get('text', 'Tech trends')[:100]

    print(f"📌 Selected topic: {topic_text}")
    print(f"💬 Engagement: {top_topic.get('engagement', 0)} interactions")
    print()

    # Generate post with X.AI
    print("🤖 Generating post with X.AI...")
    post_data = generate_post_with_xai(topic_text, category, selected_slot)

    if not post_data.get('success'):
        print(f"❌ Failed to generate post: {post_data.get('error')}")
        sys.exit(1)

    print(f"✅ Post generated successfully!")
    print(f"📝 Title: {post_data.get('title_he')}")
    print(f"📊 Length: {len(post_data.get('content', ''))} characters")
    print()

    # Create Jekyll post
    print("💾 Creating Jekyll post file...")
    filepath = create_jekyll_post(post_data, now, selected_time)

    print()
    print("=" * 60)
    print(f"✅ Post created successfully: {filepath}")
    print()
    print("Next steps:")
    print("1. Generate hero image:")
    print(f"   python3 scripts/generate_ai_image.py {filepath}")
    print("2. Review and edit if needed")
    print("3. Commit and push to GitHub")
    print()
    print(f"Next post time: {POST_TIMES[(time_slot_index + 1) % 3][0]} ({POST_TIMES[(time_slot_index + 1) % 3][1]})")


if __name__ == '__main__':
    main()

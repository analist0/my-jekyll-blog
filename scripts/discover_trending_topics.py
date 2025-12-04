#!/usr/bin/env python3
"""
🔥 Trending Topics Discoverer
Uses multiple sources to find hot topics in tech RIGHT NOW
"""

import os
import json
import requests
from datetime import datetime, timedelta

# XAI API Configuration
XAI_API_KEY = os.getenv('XAI_API_KEY')
XAI_API_URL = "https://api.x.ai/v1/chat/completions"

def get_trending_from_hackernews():
    """Get trending topics from Hacker News API"""
    print("📡 Fetching from Hacker News...")

    try:
        # Get top stories
        response = requests.get(
            "https://hacker-news.firebaseio.com/v0/topstories.json",
            timeout=10
        )

        if response.status_code != 200:
            return []

        story_ids = response.json()[:30]  # Top 30 stories
        stories = []

        for story_id in story_ids[:10]:  # Get first 10 for speed
            try:
                story_response = requests.get(
                    f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json",
                    timeout=5
                )
                if story_response.status_code == 200:
                    story = story_response.json()
                    if story.get('title'):
                        stories.append(story['title'])
            except:
                continue

        print(f"  ✅ Found {len(stories)} stories from HN")
        return stories

    except Exception as e:
        print(f"  ⚠️ HN Error: {e}")
        return []

def get_trending_from_github():
    """Get trending repositories from GitHub"""
    print("📡 Fetching from GitHub Trending...")

    try:
        # Use GitHub Search API for trending repos
        today = datetime.now().strftime('%Y-%m-%d')
        week_ago = (datetime.now() - timedelta(days=7)).strftime('%Y-%m-%d')

        response = requests.get(
            "https://api.github.com/search/repositories",
            params={
                'q': f'created:>{week_ago}',
                'sort': 'stars',
                'order': 'desc',
                'per_page': 10
            },
            timeout=10
        )

        if response.status_code != 200:
            return []

        repos = response.json().get('items', [])
        topics = [repo['name'] + ': ' + repo['description'][:100] if repo.get('description') else repo['name']
                 for repo in repos]

        print(f"  ✅ Found {len(topics)} repos from GitHub")
        return topics

    except Exception as e:
        print(f"  ⚠️ GitHub Error: {e}")
        return []

def get_trending_from_reddit():
    """Get trending posts from r/programming and r/technology"""
    print("📡 Fetching from Reddit...")

    try:
        topics = []

        for subreddit in ['programming', 'technology', 'coding', 'webdev']:
            try:
                response = requests.get(
                    f"https://www.reddit.com/r/{subreddit}/hot.json",
                    headers={'User-Agent': 'TutorialBot/1.0'},
                    params={'limit': 10},
                    timeout=10
                )

                if response.status_code == 200:
                    data = response.json()
                    posts = data.get('data', {}).get('children', [])

                    for post in posts:
                        title = post.get('data', {}).get('title', '')
                        if title:
                            topics.append(title)
            except:
                continue

        print(f"  ✅ Found {len(topics)} posts from Reddit")
        return topics

    except Exception as e:
        print(f"  ⚠️ Reddit Error: {e}")
        return []

def analyze_trending_with_ai(all_sources):
    """Use XAI to analyze all sources and extract the BEST tutorial topics"""

    print("\n🤖 Analyzing trends with XAI AI...")

    # Combine all sources
    combined_text = "\n".join(all_sources)

    prompt = f"""You are a tech trend analyst. Analyze these trending topics from Hacker News, GitHub, and Reddit today:

{combined_text}

Based on this data, identify the TOP 5 HOTTEST topics in technology RIGHT NOW.

For each topic:
1. Make it tutorial-friendly (actionable, specific)
2. Focus on practical implementation
3. Include specific technologies/tools
4. Make it comprehensive enough for a 3000+ word guide

Format as a JSON array of tutorial titles:
[
  "Building X with Y: Complete Guide",
  "Advanced Z Techniques for Developers",
  ...
]

Return ONLY the JSON array, nothing else."""

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
                        "content": "You are a tech trend analyst who identifies hot topics and converts them into comprehensive tutorial titles. Always return valid JSON arrays."
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                "temperature": 0.7,
                "max_tokens": 1000,
                "stream": False
            },
            timeout=60
        )

        if response.status_code == 200:
            result = response.json()
            content = result['choices'][0]['message']['content'].strip()

            # Extract JSON from response
            if content.startswith('```'):
                # Remove code blocks if present
                content = content.split('```')[1]
                if content.startswith('json'):
                    content = content[4:]
                content = content.strip()

            # Parse JSON
            topics = json.loads(content)

            print(f"  ✅ AI identified {len(topics)} hot topics")
            return topics

        else:
            print(f"  ❌ AI Error: {response.status_code}")
            return []

    except json.JSONDecodeError as e:
        print(f"  ⚠️ Failed to parse AI response as JSON: {e}")
        print(f"  Response was: {content[:200]}")
        return []
    except Exception as e:
        print(f"  ❌ Error: {e}")
        return []

def discover_trending_topics():
    """Main function to discover trending topics"""

    print("🔥 Discovering Trending Topics in Tech")
    print("=" * 60)
    print(f"📅 Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()

    all_sources = []

    # Collect from multiple sources
    hn_topics = get_trending_from_hackernews()
    all_sources.extend(hn_topics)

    github_topics = get_trending_from_github()
    all_sources.extend(github_topics)

    reddit_topics = get_trending_from_reddit()
    all_sources.extend(reddit_topics)

    print(f"\n📊 Total sources collected: {len(all_sources)}")

    if len(all_sources) < 5:
        print("⚠️ Not enough data from sources, using fallback topics")
        return [
            "Building Modern AI Applications with Python",
            "Advanced Docker Security Best Practices",
            "Creating Real-time APIs with WebSockets"
        ]

    # Analyze with AI
    hot_topics = analyze_trending_with_ai(all_sources)

    if not hot_topics:
        print("⚠️ AI analysis failed, using fallback topics")
        return [
            "Latest Web Development Trends and Tools",
            "Building Scalable Backend Systems",
            "Modern Frontend Development with React"
        ]

    print("\n" + "=" * 60)
    print("🔥 HOT TOPICS FOR TODAY:")
    print("=" * 60)
    for i, topic in enumerate(hot_topics, 1):
        print(f"{i}. {topic}")
    print()

    return hot_topics

if __name__ == '__main__':
    topics = discover_trending_topics()

    # Save to file for use by generate_tutorial.py
    with open('trending_topics.json', 'w') as f:
        json.dump({
            'date': datetime.now().isoformat(),
            'topics': topics
        }, f, indent=2)

    print(f"✅ Saved to: trending_topics.json")

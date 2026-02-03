#!/usr/bin/env python3
"""
Content Utilities for Blog Generation
- Duplicate detection
- Sentiment analysis
- Topic relevance scoring
"""

import os
import re
import json
import requests
from pathlib import Path
from datetime import datetime, timedelta
from typing import List, Dict, Optional, Tuple

# Configuration
GOOGLE_API_KEY = os.environ.get('GOOGLE_API_KEY', '')
PERPLEXITY_API_KEY = os.environ.get('PERPLEXITY_API_KEY', '')
BLOG_DIR = Path(os.environ.get('GITHUB_WORKSPACE', Path.cwd()))
POSTS_DIR = BLOG_DIR / '_posts'


def get_existing_topics(days: int = 30) -> List[str]:
    """
    Get list of topics already covered in recent posts

    Args:
        days: Number of days to look back

    Returns:
        List of topic titles
    """
    existing_topics = []
    cutoff_date = datetime.now() - timedelta(days=days)

    if not POSTS_DIR.exists():
        return existing_topics

    for post_file in POSTS_DIR.glob('*.md'):
        try:
            # Extract date from filename (YYYY-MM-DD-title.md)
            filename = post_file.name
            date_str = filename[:10]
            post_date = datetime.strptime(date_str, '%Y-%m-%d')

            if post_date < cutoff_date:
                continue

            # Read frontmatter
            content = post_file.read_text(encoding='utf-8')
            if content.startswith('---'):
                parts = content.split('---', 2)
                if len(parts) >= 2:
                    frontmatter = parts[1]
                    for line in frontmatter.split('\n'):
                        if line.strip().startswith('title:'):
                            title = line.split(':', 1)[1].strip().strip('"\'')
                            existing_topics.append(title.lower())
                            break
        except Exception:
            continue

    return existing_topics


def is_duplicate_topic(new_topic: str, existing_topics: List[str] = None, threshold: float = 0.6) -> bool:
    """
    Check if a topic is too similar to existing posts

    Args:
        new_topic: The new topic to check
        existing_topics: List of existing topic titles (or fetch automatically)
        threshold: Similarity threshold (0-1)

    Returns:
        True if topic is duplicate, False otherwise
    """
    if existing_topics is None:
        existing_topics = get_existing_topics()

    new_topic_lower = new_topic.lower()
    new_words = set(re.findall(r'\w+', new_topic_lower))

    for existing in existing_topics:
        existing_words = set(re.findall(r'\w+', existing))

        # Jaccard similarity
        intersection = len(new_words & existing_words)
        union = len(new_words | existing_words)

        if union > 0:
            similarity = intersection / union
            if similarity >= threshold:
                print(f"⚠️  Topic '{new_topic}' is similar to existing post '{existing}' (similarity: {similarity:.2f})")
                return True

    return False


def analyze_sentiment_gemini(topic: str) -> Dict:
    """
    Analyze topic sentiment and relevance using Gemini

    Args:
        topic: Topic to analyze

    Returns:
        Dict with sentiment score, relevance, and reasoning
    """
    if not GOOGLE_API_KEY:
        return {'score': 0.7, 'relevance': 'unknown', 'reason': 'No API key'}

    prompt = f"""Analyze this tech topic for content creation potential. Return JSON only.

Topic: "{topic}"

Analyze:
1. Current relevance (is this trending NOW in 2026?)
2. Sentiment (is community excited/positive about this?)
3. Content potential (can we write valuable content?)
4. Audience interest (will readers engage?)

Return this exact JSON format:
{{
    "score": 0.0-1.0 (overall score),
    "sentiment": "positive/neutral/negative",
    "relevance": "high/medium/low",
    "trending": true/false,
    "reason": "brief explanation",
    "suggested_angle": "best angle to cover this topic"
}}

Return ONLY valid JSON, no other text."""

    try:
        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={GOOGLE_API_KEY}"

        response = requests.post(url, json={
            "contents": [{"parts": [{"text": prompt}]}],
            "generationConfig": {"temperature": 0.3, "maxOutputTokens": 500}
        }, timeout=30)

        response.raise_for_status()
        result = response.json()
        content = result['candidates'][0]['content']['parts'][0]['text']

        # Parse JSON from response
        content = content.strip()
        if content.startswith('```'):
            content = content.split('```')[1]
            if content.startswith('json'):
                content = content[4:]

        return json.loads(content)

    except Exception as e:
        print(f"⚠️  Sentiment analysis failed: {e}")
        return {'score': 0.5, 'relevance': 'unknown', 'reason': str(e)}


def get_trending_topics_gemini(category: str = "AI and Technology", count: int = 5) -> List[Dict]:
    """
    Get trending topics using Gemini's knowledge

    Args:
        category: Topic category
        count: Number of topics to generate

    Returns:
        List of topic dicts with title, description, and relevance
    """
    if not GOOGLE_API_KEY:
        return []

    prompt = f"""Generate {count} trending topics in {category} that are HOT RIGHT NOW in February 2026.

Requirements:
1. Topics must be CURRENT and RELEVANT (not outdated)
2. Focus on what tech community is excited about TODAY
3. Include both emerging and established technologies
4. Each topic should have high content potential

Return JSON array:
[
    {{
        "title": "Topic title in English",
        "title_he": "כותרת בעברית",
        "description": "Brief description",
        "relevance": "high/medium",
        "trending_reason": "Why this is trending now",
        "keywords": ["keyword1", "keyword2"]
    }}
]

Return ONLY valid JSON array, no other text."""

    try:
        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={GOOGLE_API_KEY}"

        response = requests.post(url, json={
            "contents": [{"parts": [{"text": prompt}]}],
            "generationConfig": {"temperature": 0.7, "maxOutputTokens": 1500}
        }, timeout=60)

        response.raise_for_status()
        result = response.json()
        content = result['candidates'][0]['content']['parts'][0]['text']

        # Parse JSON
        content = content.strip()
        if content.startswith('```'):
            content = content.split('```')[1]
            if content.startswith('json'):
                content = content[4:]

        topics = json.loads(content)

        # Filter out duplicates
        existing = get_existing_topics()
        filtered = []
        for topic in topics:
            if not is_duplicate_topic(topic['title'], existing):
                filtered.append(topic)

        return filtered

    except Exception as e:
        print(f"⚠️  Failed to get trending topics: {e}")
        return []


def select_best_topic(topics: List[Dict]) -> Optional[Dict]:
    """
    Select the best topic from a list based on sentiment and uniqueness

    Args:
        topics: List of topic dicts

    Returns:
        Best topic dict or None
    """
    if not topics:
        return None

    scored_topics = []

    for topic in topics:
        title = topic.get('title', topic.get('title_he', ''))

        # Check for duplicates
        if is_duplicate_topic(title):
            continue

        # Get sentiment score
        sentiment = analyze_sentiment_gemini(title)
        score = sentiment.get('score', 0.5)

        # Boost high relevance topics
        if topic.get('relevance') == 'high':
            score += 0.1
        if sentiment.get('trending'):
            score += 0.15
        if sentiment.get('sentiment') == 'positive':
            score += 0.1

        topic['final_score'] = min(score, 1.0)
        topic['sentiment_data'] = sentiment
        scored_topics.append(topic)

    if not scored_topics:
        return None

    # Sort by score and return best
    scored_topics.sort(key=lambda x: x.get('final_score', 0), reverse=True)

    best = scored_topics[0]
    print(f"✅ Selected topic: {best.get('title')} (score: {best.get('final_score', 0):.2f})")

    return best


def get_categories() -> List[str]:
    """
    Get list of blog categories for content generation

    Returns:
        List of category names
    """
    return [
        "AI & Machine Learning",
        "Web Development",
        "DevOps & Cloud",
        "Python & Automation",
        "JavaScript & Frontend",
        "Database & Backend",
        "Security & Privacy",
        "Mobile Development",
        "Data Science",
        "Emerging Tech"
    ]


if __name__ == '__main__':
    # Test the utilities
    print("🔍 Testing Content Utilities...\n")

    print("📚 Existing topics (last 30 days):")
    existing = get_existing_topics()
    for t in existing[:5]:
        print(f"  - {t}")

    print(f"\n📊 Total existing posts: {len(existing)}")

    if GOOGLE_API_KEY:
        print("\n🔥 Fetching trending topics...")
        topics = get_trending_topics_gemini("AI Technology", 3)
        for t in topics:
            print(f"  - {t.get('title')} ({t.get('relevance')})")

        if topics:
            print("\n🎯 Selecting best topic...")
            best = select_best_topic(topics)
            if best:
                print(f"  Winner: {best.get('title')}")
                print(f"  Score: {best.get('final_score', 0):.2f}")
    else:
        print("\n⚠️  GOOGLE_API_KEY not set, skipping API tests")

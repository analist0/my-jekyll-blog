#!/usr/bin/env python3
"""
Enhanced Image Generation for Jekyll Blog Posts
Uses Unsplash API for high-quality, free stock photos
"""

import os
import sys
import json
import requests
import hashlib
from datetime import datetime
from pathlib import Path

# Configuration
UNSPLASH_ACCESS_KEY = os.environ.get('UNSPLASH_ACCESS_KEY', 'YOUR_ACCESS_KEY_HERE')
UNSPLASH_API_URL = "https://api.unsplash.com/search/photos"

# Fallback: Use Picsum for placeholder images (no API key needed)
PICSUM_URL = "https://picsum.photos/1200/630"

def extract_keywords(title: str, description: str = "") -> str:
    """Extract relevant keywords for image search"""
    # Common tech keywords
    tech_keywords = {
        'ai': 'artificial intelligence technology',
        'ml': 'machine learning',
        'data': 'data science analytics',
        'code': 'programming coding',
        'web': 'web development',
        'mobile': 'mobile app smartphone',
        'cloud': 'cloud computing',
        'security': 'cybersecurity hacking',
        'blockchain': 'blockchain cryptocurrency',
        'iot': 'internet of things devices'
    }

    text = (title + " " + description).lower()

    for key, keywords in tech_keywords.items():
        if key in text:
            return keywords

    # Default keywords
    return "technology innovation digital"


def get_image_from_unsplash(title: str, description: str = "") -> dict:
    """
    Search and download image from Unsplash

    Args:
        title: Blog post title
        description: Blog post description

    Returns:
        dict: Image information (URL, photographer, etc.)
    """

    if UNSPLASH_ACCESS_KEY == 'YOUR_ACCESS_KEY_HERE':
        # Fallback to Picsum (no API needed)
        return {
            'success': True,
            'image_url': f"{PICSUM_URL}?random={hashlib.md5(title.encode()).hexdigest()[:8]}",
            'source': 'picsum',
            'photographer': 'Picsum Photos',
            'photographer_url': 'https://picsum.photos',
            'download_url': None
        }

    try:
        # Extract search keywords
        keywords = extract_keywords(title, description)

        params = {
            'query': keywords,
            'per_page': 1,
            'orientation': 'landscape',
            'content_filter': 'high'
        }

        headers = {
            'Authorization': f'Client-ID {UNSPLASH_ACCESS_KEY}'
        }

        response = requests.get(UNSPLASH_API_URL, params=params, headers=headers, timeout=10)
        response.raise_for_status()

        data = response.json()

        if data.get('results') and len(data['results']) > 0:
            photo = data['results'][0]

            return {
                'success': True,
                'image_url': photo['urls']['regular'],
                'image_download': photo['urls']['download'],
                'source': 'unsplash',
                'photographer': photo['user']['name'],
                'photographer_url': photo['user']['links']['html'],
                'description': photo.get('description', photo.get('alt_description', '')),
                'color': photo.get('color', '#000000')
            }
        else:
            # Fallback to Picsum
            return {
                'success': True,
                'image_url': f"{PICSUM_URL}?random={hashlib.md5(title.encode()).hexdigest()[:8]}",
                'source': 'picsum_fallback',
                'photographer': 'Picsum Photos',
                'photographer_url': 'https://picsum.photos'
            }

    except Exception as e:
        print(f"⚠️  Unsplash API error: {e}")
        # Fallback to Picsum
        return {
            'success': True,
            'image_url': f"{PICSUM_URL}?random={hashlib.md5(title.encode()).hexdigest()[:8]}",
            'source': 'picsum_error_fallback',
            'photographer': 'Picsum Photos',
            'photographer_url': 'https://picsum.photos',
            'error': str(e)
        }


def update_post_frontmatter(post_path: str, image_data: dict) -> bool:
    """
    Update Jekyll post frontmatter with image and SEO data

    Args:
        post_path: Path to the Jekyll post file
        image_data: Image information dictionary

    Returns:
        bool: Success status
    """

    try:
        with open(post_path, 'r', encoding='utf-8') as f:
            content = f.read()

        if not content.startswith('---'):
            print(f"❌ Invalid post format (no frontmatter): {post_path}")
            return False

        parts = content.split('---', 2)
        if len(parts) < 3:
            print(f"❌ Invalid frontmatter format: {post_path}")
            return False

        frontmatter_lines = parts[1].strip().split('\n')
        body = parts[2]

        # Update/add image field
        has_image = False
        new_lines = []

        for line in frontmatter_lines:
            if line.strip().startswith('image:'):
                new_lines.append(f'image: "{image_data["image_url"]}"')
                has_image = True
            else:
                new_lines.append(line)

        if not has_image:
            new_lines.append(f'image: "{image_data["image_url"]}"')

        # Add image credit if available
        if 'photographer' in image_data and 'image_credit:' not in '\n'.join(new_lines):
            credit = f"{image_data['photographer']} via {image_data['source'].title()}"
            new_lines.append(f'image_credit: "{credit}"')
            new_lines.append(f'image_credit_url: "{image_data.get("photographer_url", "")}"')

        # Rebuild frontmatter
        new_frontmatter = '\n'.join(new_lines)
        new_content = f'---\n{new_frontmatter}\n---{body}'

        with open(post_path, 'w', encoding='utf-8') as f:
            f.write(new_content)

        print(f"✅ Updated post: {post_path}")
        return True

    except Exception as e:
        print(f"❌ Error updating post: {e}")
        return False


def main():
    """Main function"""

    if len(sys.argv) < 2:
        print("""
╔══════════════════════════════════════════════════════════════╗
║       Enhanced Image Generator for Jekyll Posts             ║
╚══════════════════════════════════════════════════════════════╝

Usage:
  python3 generate_ai_image.py <post-file>
  python3 generate_ai_image.py --test "Title" "Description"

Features:
  ✅ High-quality images from Unsplash
  ✅ Automatic fallback to Picsum (no API key needed)
  ✅ Smart keyword extraction
  ✅ SEO-friendly image credits
  ✅ Automatic frontmatter update

Examples:
  # Generate image for existing post
  python3 generate_ai_image.py _posts/2025-12-04-my-post.md

  # Test mode
  python3 generate_ai_image.py --test "AI Revolution" "How AI changes everything"

Environment (Optional):
  UNSPLASH_ACCESS_KEY - Get free at: https://unsplash.com/developers

Current Status:
  API Key: {'✅ Set' if UNSPLASH_ACCESS_KEY != 'YOUR_ACCESS_KEY_HERE' else '⚠️  Not set (will use Picsum fallback)'}
        """)
        sys.exit(1)

    # Test mode
    if sys.argv[1] == '--test':
        title = sys.argv[2] if len(sys.argv) > 2 else "Test Blog Post About Technology"
        description = sys.argv[3] if len(sys.argv) > 3 else "An amazing technology article"

        print(f"\n🧪 Testing Image Generation...")
        print(f"📝 Title: {title}")
        print(f"📄 Description: {description}")
        print(f"🔍 Keywords: {extract_keywords(title, description)}\n")

        result = get_image_from_unsplash(title, description)
        print(json.dumps(result, indent=2, ensure_ascii=False))
        sys.exit(0)

    # Post mode
    post_path = sys.argv[1]

    if not os.path.exists(post_path):
        print(f"❌ Post file not found: {post_path}")
        sys.exit(1)

    # Parse post
    with open(post_path, 'r', encoding='utf-8') as f:
        content = f.read()

    try:
        parts = content.split('---', 2)
        frontmatter = parts[1]

        title = ""
        description = ""

        for line in frontmatter.split('\n'):
            line = line.strip()
            if line.startswith('title:'):
                title = line.split(':', 1)[1].strip().strip('"\'')
            elif line.startswith('description:'):
                description = line.split(':', 1)[1].strip().strip('"\'')

        if not title:
            print(f"❌ No title found in post frontmatter")
            sys.exit(1)

        print(f"\n🎨 Generating image for post...")
        print(f"📝 Title: {title}")
        print(f"📄 Description: {description}")
        print(f"🔍 Keywords: {extract_keywords(title, description)}\n")

        result = get_image_from_unsplash(title, description)

        if result['success']:
            print(f"✅ Image selected successfully!")
            print(f"🖼️  URL: {result['image_url']}")
            print(f"📷 Source: {result['source']}")
            print(f"👤 Credit: {result.get('photographer', 'N/A')}\n")

            if update_post_frontmatter(post_path, result):
                print(f"✅ Post updated with image and credits")
            else:
                print(f"⚠️  Please add image manually:")
                print(f"   image: \"{result['image_url']}\"")
        else:
            print(f"❌ Image generation failed")
            sys.exit(1)

    except Exception as e:
        print(f"❌ Error processing post: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()

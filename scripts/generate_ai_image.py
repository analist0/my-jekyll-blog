#!/usr/bin/env python3
"""
X.AI Image Generation Script for Jekyll Blog Posts
Automatically generates hero images for blog posts using X.AI API (Grok Vision)
"""

import os
import sys
import json
import requests
from datetime import datetime
from pathlib import Path

# Configuration
XAI_API_KEY = os.environ.get('XAI_API_KEY', '')  # Set via: export XAI_API_KEY="your-key"
XAI_API_URL = "https://api.x.ai/v1/chat/completions"

# Image generation prompt template
IMAGE_PROMPT_TEMPLATE = """
Create a professional, modern, and visually appealing hero image for a blog post titled: "{title}"

The image should be:
- High quality and eye-catching
- Relevant to the topic: {description}
- Suitable for a tech blog
- Modern and clean design
- 16:9 aspect ratio (1920x1080)

Style: Modern, minimalist, professional
"""


def generate_image_with_xai(title: str, description: str = "") -> dict:
    """
    Generate an image using X.AI API (Grok Vision)

    Args:
        title: Blog post title
        description: Blog post description/excerpt

    Returns:
        dict: Response containing image URL or error
    """

    if not XAI_API_KEY:
        return {
            'success': False,
            'error': 'XAI_API_KEY not set. Please set it via: export XAI_API_KEY="your-key"'
        }

    prompt = IMAGE_PROMPT_TEMPLATE.format(
        title=title,
        description=description or title
    )

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {XAI_API_KEY}"
    }

    payload = {
        "model": "grok-vision-beta",
        "messages": [
            {
                "role": "system",
                "content": "You are an expert graphic designer creating hero images for blog posts."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        "temperature": 0.7
    }

    try:
        response = requests.post(XAI_API_URL, headers=headers, json=payload, timeout=30)
        response.raise_for_status()

        data = response.json()

        # Extract image URL from response
        if 'choices' in data and len(data['choices']) > 0:
            content = data['choices'][0]['message']['content']

            return {
                'success': True,
                'image_url': content,  # Adjust based on actual API response
                'prompt': prompt,
                'timestamp': datetime.now().isoformat()
            }
        else:
            return {
                'success': False,
                'error': 'No image generated',
                'response': data
            }

    except requests.exceptions.RequestException as e:
        return {
            'success': False,
            'error': f'API request failed: {str(e)}'
        }
    except Exception as e:
        return {
            'success': False,
            'error': f'Unexpected error: {str(e)}'
        }


def update_post_frontmatter(post_path: str, image_url: str) -> bool:
    """
    Update Jekyll post frontmatter with generated image URL

    Args:
        post_path: Path to the Jekyll post file
        image_url: Generated image URL

    Returns:
        bool: Success status
    """

    try:
        with open(post_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Parse frontmatter
        if not content.startswith('---'):
            print(f"❌ Invalid post format (no frontmatter): {post_path}")
            return False

        parts = content.split('---', 2)
        if len(parts) < 3:
            print(f"❌ Invalid frontmatter format: {post_path}")
            return False

        frontmatter = parts[1]
        body = parts[2]

        # Add or update image field
        if 'image:' in frontmatter:
            # Update existing
            lines = frontmatter.split('\n')
            new_lines = []
            for line in lines:
                if line.strip().startswith('image:'):
                    new_lines.append(f'image: {image_url}')
                else:
                    new_lines.append(line)
            frontmatter = '\n'.join(new_lines)
        else:
            # Add new
            frontmatter += f'\nimage: {image_url}\n'

        # Write back
        new_content = f'---{frontmatter}---{body}'

        with open(post_path, 'w', encoding='utf-8') as f:
            f.write(new_content)

        print(f"✅ Updated post: {post_path}")
        return True

    except Exception as e:
        print(f"❌ Error updating post: {e}")
        return False


def main():
    """
    Main function - can be called from command line or as module
    """

    if len(sys.argv) < 2:
        print("""
╔══════════════════════════════════════════════════════════════╗
║           X.AI Image Generator for Jekyll Posts             ║
╚══════════════════════════════════════════════════════════════╝

Usage:
  python3 generate_ai_image.py <post-file> [title] [description]
  python3 generate_ai_image.py --test "My Blog Post" "Post description"

Examples:
  # Generate image for existing post
  python3 generate_ai_image.py _posts/2025-12-04-my-post.md

  # Test with custom title and description
  python3 generate_ai_image.py --test "AI Revolution" "How AI is changing the world"

Environment:
  XAI_API_KEY - Your X.AI API key (required)
  Set it: export XAI_API_KEY="xai-your-key-here"

Current Status:
  API Key: {'✅ Set' if XAI_API_KEY else '❌ Not set'}
        """)
        sys.exit(1)

    # Test mode
    if sys.argv[1] == '--test':
        title = sys.argv[2] if len(sys.argv) > 2 else "Test Blog Post"
        description = sys.argv[3] if len(sys.argv) > 3 else "This is a test description"

        print(f"\n🧪 Testing X.AI Image Generation...")
        print(f"📝 Title: {title}")
        print(f"📄 Description: {description}\n")

        result = generate_image_with_xai(title, description)

        print(json.dumps(result, indent=2, ensure_ascii=False))
        sys.exit(0 if result['success'] else 1)

    # Post mode
    post_path = sys.argv[1]

    if not os.path.exists(post_path):
        print(f"❌ Post file not found: {post_path}")
        sys.exit(1)

    # Parse post frontmatter for title and description
    with open(post_path, 'r', encoding='utf-8') as f:
        content = f.read()

    try:
        parts = content.split('---', 2)
        frontmatter = parts[1]

        title = ""
        description = ""

        for line in frontmatter.split('\n'):
            if line.strip().startswith('title:'):
                title = line.split(':', 1)[1].strip().strip('"\'')
            elif line.strip().startswith('description:'):
                description = line.split(':', 1)[1].strip().strip('"\'')

        if not title:
            print(f"❌ No title found in post frontmatter")
            sys.exit(1)

        print(f"\n🎨 Generating image for post...")
        print(f"📝 Title: {title}")
        print(f"📄 Description: {description}\n")

        result = generate_image_with_xai(title, description)

        if result['success']:
            print(f"✅ Image generated successfully!")
            print(f"🖼️  URL: {result['image_url']}\n")

            # Update post
            if update_post_frontmatter(post_path, result['image_url']):
                print(f"✅ Post updated with image URL")
            else:
                print(f"⚠️  Generated image URL: {result['image_url']}")
                print(f"   Please add it manually to your post frontmatter")
        else:
            print(f"❌ Image generation failed: {result['error']}")
            sys.exit(1)

    except Exception as e:
        print(f"❌ Error processing post: {e}")
        sys.exit(1)


if __name__ == '__main__':
    main()

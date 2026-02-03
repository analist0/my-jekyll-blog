#!/usr/bin/env python3
"""
Centralized Configuration Module
All API endpoints, model names, and shared settings in one place
"""

import os
from pathlib import Path

# =============================================================================
# ENVIRONMENT & PATHS
# =============================================================================

BLOG_DIR = Path(os.environ.get('GITHUB_WORKSPACE', Path.cwd()))
POSTS_DIR = BLOG_DIR / '_posts'
ASSETS_DIR = BLOG_DIR / 'assets'
IMAGES_DIR = ASSETS_DIR / 'images'

# =============================================================================
# API KEYS (from environment variables)
# =============================================================================

XAI_API_KEY = os.environ.get('XAI_API_KEY', '')
GOOGLE_API_KEY = os.environ.get('GOOGLE_API_KEY', '')
PERPLEXITY_API_KEY = os.environ.get('PERPLEXITY_API_KEY', '')
X_BEARER_TOKEN = os.environ.get('X_BEARER_TOKEN', '')
UNSPLASH_ACCESS_KEY = os.environ.get('UNSPLASH_ACCESS_KEY', '')
GITHUB_TOKEN = os.environ.get('GITHUB_TOKEN', '')

# =============================================================================
# XAI / GROK API
# =============================================================================

XAI_CHAT_URL = "https://api.x.ai/v1/chat/completions"
XAI_IMAGE_URL = "https://api.x.ai/v1/images/generations"

# Models
XAI_CHAT_MODEL = os.environ.get('XAI_CHAT_MODEL', 'grok-4-1-fast-reasoning')
XAI_IMAGE_MODEL = os.environ.get('XAI_IMAGE_MODEL', 'grok-2-image-1212')

# Default settings
XAI_CHAT_MAX_TOKENS = 16000
XAI_CHAT_TEMPERATURE = 0.7
XAI_CHAT_TIMEOUT = 180

# =============================================================================
# GOOGLE GEMINI API
# =============================================================================

GEMINI_MODEL = os.environ.get('GEMINI_MODEL', 'gemini-2.5-flash')
GEMINI_URL_TEMPLATE = "https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={api_key}"

def get_gemini_url(model: str = None) -> str:
    """Get Gemini API URL with model and key"""
    return GEMINI_URL_TEMPLATE.format(
        model=model or GEMINI_MODEL,
        api_key=GOOGLE_API_KEY
    )

# Default settings
GEMINI_MAX_TOKENS = 8000
GEMINI_TEMPERATURE = 0.7
GEMINI_TIMEOUT = 120

# =============================================================================
# PERPLEXITY API
# =============================================================================

PERPLEXITY_URL = "https://api.perplexity.ai/chat/completions"
PERPLEXITY_MODEL = os.environ.get('PERPLEXITY_MODEL', 'llama-3.1-sonar-large-128k-online')

# Default settings
PERPLEXITY_MAX_TOKENS = 8000
PERPLEXITY_TEMPERATURE = 0.7
PERPLEXITY_TIMEOUT = 120

# =============================================================================
# IMAGE SOURCES
# =============================================================================

UNSPLASH_API_URL = "https://api.unsplash.com/search/photos"
PICSUM_URL = "https://picsum.photos/1200/630"
PEXELS_API_URL = "https://api.pexels.com/v1/search"

# =============================================================================
# GITHUB API
# =============================================================================

GITHUB_API_URL = "https://api.github.com"

# =============================================================================
# TWITTER/X API
# =============================================================================

X_API_URL = "https://api.twitter.com/2"
X_SEARCH_URL = f"{X_API_URL}/tweets/search/recent"

# =============================================================================
# BLOG SETTINGS
# =============================================================================

DEFAULT_AUTHOR = "יוסף אלישר"
DEFAULT_LANG = "he"
DEFAULT_DIR = "rtl"
DEFAULT_LAYOUT = "post-modern"

# Categories
BLOG_CATEGORIES = [
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

# =============================================================================
# CONTENT GENERATION SETTINGS
# =============================================================================

# Minimum word counts
MIN_WORDS_TUTORIAL = 4500
MIN_WORDS_ARTICLE = 2500
MIN_WORDS_GUIDE = 3000

# Duplicate detection
DUPLICATE_CHECK_DAYS = 60
DUPLICATE_SIMILARITY_THRESHOLD = 0.6

# =============================================================================
# HELPER FUNCTIONS
# =============================================================================

def get_api_headers(api_type: str) -> dict:
    """Get standard headers for API calls"""

    if api_type == 'xai':
        return {
            "Authorization": f"Bearer {XAI_API_KEY}",
            "Content-Type": "application/json"
        }
    elif api_type == 'perplexity':
        return {
            "Authorization": f"Bearer {PERPLEXITY_API_KEY}",
            "Content-Type": "application/json"
        }
    elif api_type == 'unsplash':
        return {
            "Authorization": f"Client-ID {UNSPLASH_ACCESS_KEY}"
        }
    elif api_type == 'x':
        return {
            "Authorization": f"Bearer {X_BEARER_TOKEN}"
        }
    elif api_type == 'github':
        headers = {"Accept": "application/vnd.github.v3+json"}
        if GITHUB_TOKEN:
            headers["Authorization"] = f"token {GITHUB_TOKEN}"
        return headers
    else:
        return {"Content-Type": "application/json"}


def check_api_keys() -> dict:
    """Check which API keys are configured"""
    return {
        'xai': bool(XAI_API_KEY),
        'google': bool(GOOGLE_API_KEY),
        'perplexity': bool(PERPLEXITY_API_KEY),
        'x_bearer': bool(X_BEARER_TOKEN),
        'unsplash': bool(UNSPLASH_ACCESS_KEY),
        'github': bool(GITHUB_TOKEN)
    }


def print_config_status():
    """Print current configuration status"""
    keys = check_api_keys()
    print("📋 Configuration Status:")
    print(f"   XAI API Key: {'✅' if keys['xai'] else '❌'}")
    print(f"   Google API Key: {'✅' if keys['google'] else '❌'}")
    print(f"   Perplexity API Key: {'✅' if keys['perplexity'] else '❌'}")
    print(f"   X Bearer Token: {'✅' if keys['x_bearer'] else '❌'}")
    print(f"   Unsplash Access Key: {'✅' if keys['unsplash'] else '❌'}")
    print(f"   GitHub Token: {'✅' if keys['github'] else '❌'}")
    print(f"\n   Blog Dir: {BLOG_DIR}")
    print(f"   Posts Dir: {POSTS_DIR}")


if __name__ == '__main__':
    print_config_status()

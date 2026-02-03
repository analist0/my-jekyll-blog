#!/usr/bin/env python3
"""
Shared Text Utilities
Slug generation, YAML escaping, Liquid syntax escaping, and text processing
"""

import re
import json
import hashlib
from datetime import datetime
from typing import Optional, List


def sanitize_slug(text: str, max_length: int = 80, fallback: str = None) -> str:
    """
    Create a safe URL slug from text

    Args:
        text: Input text to convert to slug
        max_length: Maximum slug length
        fallback: Fallback value if slug is empty (default: timestamp-based)

    Returns:
        Safe URL slug string
    """
    if not text:
        return fallback or f"post-{datetime.now().strftime('%Y%m%d-%H%M%S')}"

    # Convert to lowercase
    slug = text.lower()

    # Remove special characters but keep spaces, hyphens, and alphanumeric
    slug = re.sub(r'[^\w\s-]', '', slug)

    # Replace whitespace with hyphens
    slug = re.sub(r'[-\s]+', '-', slug)

    # Strip leading/trailing hyphens
    slug = slug.strip('-')

    # Truncate to max length
    if len(slug) > max_length:
        slug = slug[:max_length].rstrip('-')

    # If empty after sanitization, use fallback
    if not slug:
        return fallback or f"post-{datetime.now().strftime('%Y%m%d-%H%M%S')}"

    return slug


def escape_yaml_string(text: str) -> str:
    """
    Escape special characters for safe YAML string values

    Args:
        text: Input text to escape

    Returns:
        YAML-safe escaped string
    """
    if not text:
        return ""

    # Replace problematic characters
    text = text.replace('\\', '\\\\')  # Backslashes first
    text = text.replace('"', '\\"')     # Double quotes
    text = text.replace('\n', '\\n')    # Newlines
    text = text.replace('\r', '\\r')    # Carriage returns
    text = text.replace('\t', '\\t')    # Tabs

    # Remove control characters
    text = re.sub(r'[\x00-\x08\x0b\x0c\x0e-\x1f\x7f]', '', text)

    return text


def escape_yaml_multiline(text: str) -> str:
    """
    Escape text for multiline YAML (preserving newlines)

    Args:
        text: Input text

    Returns:
        Escaped text safe for YAML multiline
    """
    if not text:
        return ""

    # Only escape problematic characters, keep newlines
    text = text.replace('\\', '\\\\')
    text = text.replace('"', '\\"')

    return text


def escape_liquid_syntax(content: str) -> str:
    """
    Escape Liquid template syntax in code blocks to prevent Jekyll errors

    Args:
        content: Markdown content with code blocks

    Returns:
        Content with Liquid syntax escaped in code blocks
    """
    def wrap_code_block(match):
        code_block = match.group(0)

        # Skip if already wrapped
        if '{% raw %}' in code_block or '{% endraw %}' in code_block:
            return code_block

        # Check if contains Liquid syntax
        if '{{' in code_block or '{%' in code_block:
            return '{% raw %}\n' + code_block + '\n{% endraw %}'

        return code_block

    # Find and wrap code blocks
    content = re.sub(r'```[\s\S]*?```', wrap_code_block, content, flags=re.MULTILINE)

    return content


def generate_safe_filename(title: str, date: datetime = None, extension: str = 'md') -> str:
    """
    Generate a safe Jekyll post filename

    Args:
        title: Post title
        date: Post date (default: now)
        extension: File extension (default: md)

    Returns:
        Safe filename like "2026-02-03-my-post-title.md"
    """
    if date is None:
        date = datetime.now()

    date_str = date.strftime('%Y-%m-%d')
    slug = sanitize_slug(title)

    return f"{date_str}-{slug}.{extension}"


def extract_tags_from_text(text: str, max_tags: int = 8, min_length: int = 3) -> List[str]:
    """
    Extract meaningful tags from text

    Args:
        text: Input text
        max_tags: Maximum number of tags to return
        min_length: Minimum tag length

    Returns:
        List of tag strings
    """
    # Remove special characters and split into words
    words = re.sub(r'[^\w\s]', '', text.lower()).split()

    # Filter by length and get unique
    tags = []
    seen = set()

    for word in words:
        if len(word) >= min_length and word not in seen:
            seen.add(word)
            tags.append(word)
            if len(tags) >= max_tags:
                break

    return tags


def tags_to_yaml(tags: List[str]) -> str:
    """
    Convert tags list to YAML-safe JSON array string

    Args:
        tags: List of tag strings

    Returns:
        JSON array string safe for YAML
    """
    return json.dumps(tags, ensure_ascii=False)


def truncate_text(text: str, max_length: int = 160, suffix: str = '...') -> str:
    """
    Truncate text to max length, breaking at word boundary

    Args:
        text: Input text
        max_length: Maximum length
        suffix: Suffix to add when truncated

    Returns:
        Truncated text
    """
    if not text or len(text) <= max_length:
        return text or ""

    # Find last space before max_length
    truncated = text[:max_length - len(suffix)]
    last_space = truncated.rfind(' ')

    if last_space > 0:
        truncated = truncated[:last_space]

    return truncated + suffix


def generate_content_hash(content: str) -> str:
    """
    Generate a short hash for content (useful for deduplication)

    Args:
        content: Input content

    Returns:
        Short hash string
    """
    return hashlib.md5(content.encode()).hexdigest()[:8]


def clean_markdown_frontmatter(content: str) -> str:
    """
    Remove any accidental frontmatter from AI-generated content

    Args:
        content: Content that may contain unwanted frontmatter

    Returns:
        Content with frontmatter removed
    """
    # Remove frontmatter block at the start
    content = re.sub(r'^---\n[\s\S]*?\n---\n', '', content)

    return content.strip()


def create_frontmatter(
    title: str,
    description: str = None,
    date: datetime = None,
    categories: List[str] = None,
    tags: List[str] = None,
    author: str = None,
    layout: str = "post-modern",
    lang: str = "he",
    direction: str = "rtl",
    image: str = None,
    **extra_fields
) -> str:
    """
    Create Jekyll frontmatter string

    Args:
        title: Post title
        description: SEO description
        date: Post date
        categories: Category list
        tags: Tag list
        author: Author name
        layout: Jekyll layout
        lang: Language code
        direction: Text direction
        image: Featured image URL
        **extra_fields: Additional frontmatter fields

    Returns:
        Complete frontmatter string with delimiters
    """
    if date is None:
        date = datetime.now()

    # Escape title and description for YAML
    safe_title = escape_yaml_string(title)
    safe_desc = escape_yaml_string(description or "")

    lines = [
        "---",
        f'layout: {layout}',
        f'title: "{safe_title}"',
    ]

    if description:
        lines.append(f'description: "{safe_desc}"')

    lines.append(f'date: {date.strftime("%Y-%m-%d %H:%M:%S")} +0200')

    if categories:
        lines.append(f'categories: {json.dumps(categories, ensure_ascii=False)}')

    if tags:
        lines.append(f'tags: {json.dumps(tags, ensure_ascii=False)}')

    if author:
        lines.append(f'author: "{escape_yaml_string(author)}"')

    lines.append(f'lang: {lang}')
    lines.append(f'dir: {direction}')

    if image:
        lines.append(f'image: "{image}"')

    # Add extra fields
    for key, value in extra_fields.items():
        if isinstance(value, str):
            lines.append(f'{key}: "{escape_yaml_string(value)}"')
        elif isinstance(value, (list, dict)):
            lines.append(f'{key}: {json.dumps(value, ensure_ascii=False)}')
        else:
            lines.append(f'{key}: {value}')

    lines.append("---")
    lines.append("")

    return '\n'.join(lines)


# =============================================================================
# TESTS
# =============================================================================

if __name__ == '__main__':
    print("🧪 Testing text_utils...\n")

    # Test slug sanitization
    test_cases = [
        "Hello World!",
        "מדריך Python מתקדם",
        "   spaces   and---dashes   ",
        "!@#$%^&*()",
        "",
        None
    ]

    print("📝 Slug Sanitization Tests:")
    for test in test_cases:
        result = sanitize_slug(test) if test else sanitize_slug("")
        print(f"  '{test}' -> '{result}'")

    print("\n📝 YAML Escaping Tests:")
    yaml_tests = [
        'Simple text',
        'Text with "quotes"',
        'Text with\nnewlines',
        'Text with\ttabs',
        'Text\\with\\backslashes'
    ]

    for test in yaml_tests:
        result = escape_yaml_string(test)
        print(f"  '{repr(test)}' -> '{result}'")

    print("\n📝 Frontmatter Test:")
    fm = create_frontmatter(
        title="Test Post with \"Quotes\"",
        description="A test\ndescription",
        categories=["AI", "Python"],
        tags=["test", "python", "ai"],
        author="יוסף אלישר"
    )
    print(fm)

    print("\n✅ All tests completed!")

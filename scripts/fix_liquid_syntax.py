#!/usr/bin/env python3
"""
🔧 Liquid Syntax Fixer
Fixes Jekyll posts by wrapping code blocks with {% raw %}{% endraw %}
to prevent Liquid template processing errors
"""

import os
import re
import sys
from pathlib import Path


def escape_liquid_in_content(content: str) -> str:
    """
    Wrap code blocks and inline code with {% raw %}{% endraw %}
    to prevent Liquid template errors
    
    Args:
        content: Post content (without frontmatter)
    
    Returns:
        Fixed content with proper escaping
    """
    
    # Pattern 1: Wrap fenced code blocks with {% raw %}{% endraw %}
    # Matches: ```language\ncode\n```
    def wrap_code_block(match):
        code_block = match.group(0)
        # Check if already wrapped
        if '{% raw %}' in code_block or '{% endraw %}' in code_block:
            return code_block
        return f'{{% raw %}}\n{code_block}\n{{% endraw %}}'
    
    # Find all code blocks and wrap them
    content = re.sub(
        r'```[\s\S]*?```',
        wrap_code_block,
        content,
        flags=re.MULTILINE
    )
    
    # Pattern 2: Escape inline code that contains {{ or {%
    # But only if it's not already escaped
    def escape_inline_liquid(match):
        inline_code = match.group(0)
        inner = match.group(1)
        
        # If contains Liquid syntax and not already escaped
        if ('{{' in inner or '{%' in inner) and '{% raw %}' not in inline_code:
            return f'`{{% raw %}}{inner}{{% endraw %}}`'
        return inline_code
    
    # Escape inline code with Liquid syntax
    content = re.sub(
        r'`([^`]+)`',
        escape_inline_liquid,
        content
    )
    
    return content


def fix_post_file(filepath: str) -> bool:
    """
    Fix a single post file
    
    Args:
        filepath: Path to post file
    
    Returns:
        bool: Success status
    """
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if not content.startswith('---'):
            print(f"⚠️  Skipping {filepath} (no frontmatter)")
            return False
        
        # Split frontmatter and content
        parts = content.split('---', 2)
        if len(parts) < 3:
            print(f"⚠️  Skipping {filepath} (invalid frontmatter)")
            return False
        
        frontmatter = parts[1]
        body = parts[2]
        
        # Check if needs fixing
        if '{% raw %}' in body:
            print(f"✓ Already fixed: {os.path.basename(filepath)}")
            return True
        
        # Fix content
        fixed_body = escape_liquid_in_content(body)
        
        # Check if anything changed
        if fixed_body == body:
            print(f"✓ No changes needed: {os.path.basename(filepath)}")
            return True
        
        # Rebuild file
        fixed_content = f'---{frontmatter}---{fixed_body}'
        
        # Write back
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(fixed_content)
        
        print(f"✅ Fixed: {os.path.basename(filepath)}")
        return True
    
    except Exception as e:
        print(f"❌ Error fixing {filepath}: {e}")
        return False


def main():
    """Main function"""
    
    print("🔧 Liquid Syntax Fixer for Jekyll Posts")
    print("=" * 60)
    
    # Get posts directory
    posts_dir = Path('_posts')
    
    if not posts_dir.exists():
        print(f"❌ Posts directory not found: {posts_dir}")
        sys.exit(1)
    
    # Get all markdown files
    post_files = list(posts_dir.glob('*.md'))
    
    if not post_files:
        print(f"⚠️  No posts found in {posts_dir}")
        sys.exit(0)
    
    print(f"\n📁 Found {len(post_files)} posts")
    print()
    
    # Fix each file
    fixed_count = 0
    error_count = 0
    
    for filepath in sorted(post_files):
        if fix_post_file(str(filepath)):
            fixed_count += 1
        else:
            error_count += 1
    
    # Summary
    print()
    print("=" * 60)
    print(f"✅ Successfully processed: {fixed_count}/{len(post_files)}")
    if error_count > 0:
        print(f"❌ Errors: {error_count}")
    print()
    print("🎉 Done! Posts are now safe from Liquid syntax errors.")


if __name__ == '__main__':
    main()

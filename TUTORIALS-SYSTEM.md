# 🤖 Automatic Tutorial Generation System

Complete system for generating professional technical tutorials automatically using XAI API.

## 🌟 Features

- **✍️ AI-Generated Content**: Comprehensive 3000+ word tutorials using Grok-2
- **🎨 AI-Generated Images**: Professional featured images using XAI Image API
- **📱 Responsive Design**: Perfect on all devices with unified layout
- **🔄 Automated Publishing**: GitHub Actions workflow runs daily
- **🔥 Trending Topics**: 30+ hot topics in modern development
- **📊 SEO Optimized**: Complete metadata, tags, and descriptions

## 📋 System Components

### 1. Tutorial Generator Script
**File**: `scripts/generate_tutorial.py`

Generates complete tutorials including:
- Comprehensive content (3000+ words)
- Featured images via XAI Image API
- Jekyll frontmatter with metadata
- SEO-optimized tags and descriptions

### 2. Unified Post Layout
**File**: `_layouts/unified-post.html`

Features:
- Hero section with featured image
- Responsive 3-column layout
- Automatic table of contents
- Social sharing buttons
- Related posts section
- Mobile-optimized design

### 3. GitHub Actions Workflow
**File**: `.github/workflows/daily-tutorials.yml`

Automation:
- Runs daily at 9:00 AM UTC (11:00 AM Israel)
- Generates 3 tutorials automatically
- Commits and pushes to repository
- Can be triggered manually

### 4. Helper Script
**File**: `scripts/generate-tutorials.sh`

Easy local testing and generation.

## 🚀 Quick Start

### Prerequisites

1. **XAI API Key** from [x.ai](https://x.ai)
2. **Python 3.8+**
3. **Jekyll** (optional for local testing)

### Setup

1. **Set API Key** (required):
```bash
export XAI_API_KEY='your-xai-api-key-here'
```

2. **Install Dependencies**:
```bash
pip install requests
```

3. **Generate Tutorials**:
```bash
# Generate 3 tutorials (default)
bash scripts/generate-tutorials.sh

# Generate custom number
bash scripts/generate-tutorials.sh 5
```

Or directly with Python:
```bash
cd ~/my-jekyll-blog
NUM_TUTORIALS=3 python3 scripts/generate_tutorial.py
```

## 📖 Usage

### Local Generation

```bash
# Set API key
export XAI_API_KEY='xai-...'

# Generate tutorials
cd ~/my-jekyll-blog
bash scripts/generate-tutorials.sh 3
```

### GitHub Actions (Automated)

The workflow runs automatically every day at 9:00 AM UTC.

**Manual Trigger**:
1. Go to GitHub repository → Actions tab
2. Select "🤖 Daily Tutorial Generator" workflow
3. Click "Run workflow"
4. Choose number of tutorials (default: 3)
5. Click "Run workflow" button

### Configure GitHub Secret

For automated generation, add your XAI API key as a GitHub Secret:

1. Go to repository → Settings → Secrets and variables → Actions
2. Click "New repository secret"
3. Name: `XAI_API_KEY`
4. Value: Your XAI API key
5. Click "Add secret"

## 🎯 Available Topics

30 hot topics including:

- Building Local AI Assistants with Ollama
- Advanced Docker Container Security
- Serverless APIs with Vercel
- Real-time Data with Apache Kafka
- Modern Authentication (OAuth 2.0, JWT)
- Progressive Web Apps (PWAs)
- GraphQL vs REST
- Kubernetes Deployment
- Microservices with Node.js
- Advanced Git Workflows
- ChatGPT Plugins
- WebSockets Applications
- Modern CSS (Grid, Flexbox)
- API Security
- CLI Tools with Python
- TypeScript Patterns
- Chrome Extensions
- FastAPI Development
- React Hooks
- Data Pipelines with Airflow
- Telegram Bots
- SQL Optimization
- Discord Bots
- State Management
- GitHub Actions CI/CD
- E-commerce with Next.js
- MongoDB Aggregation
- VS Code Extensions
- Real-time Dashboards
- Nginx Configuration

## 📁 File Structure

```
my-jekyll-blog/
├── _layouts/
│   └── unified-post.html          # Unified responsive layout
├── _posts/                         # Generated tutorials (auto)
│   └── YYYY-MM-DD-topic-name.md
├── scripts/
│   ├── generate_tutorial.py       # Main generator
│   └── generate-tutorials.sh      # Helper script
├── .github/
│   └── workflows/
│       └── daily-tutorials.yml    # GitHub Actions
└── TUTORIALS-SYSTEM.md            # This file
```

## 🎨 Layout Features

### Hero Section
- Full-width featured image (from XAI Image API)
- Gradient overlay for readability
- Category badge
- Title with gradient effect
- Reading time estimate
- Tags display

### Content Area
- Responsive 3-column grid (desktop)
- Main content (800px max width)
- Sticky sidebar with:
  - Auto-generated table of contents
  - Tag list
- Mobile: Collapses to single column

### Additional Sections
- Social sharing (Twitter, LinkedIn, WhatsApp)
- Author card
- Related posts grid
- Reading progress bar

## 🔧 Customization

### Modify Topics

Edit `scripts/generate_tutorial.py`:
```python
HOT_TOPICS = [
    "Your Custom Topic Here",
    "Another Topic",
    # Add more...
]
```

### Change Schedule

Edit `.github/workflows/daily-tutorials.yml`:
```yaml
schedule:
  - cron: '0 9 * * *'  # Change time here
```

Cron format: `minute hour day month weekday`

Examples:
- `0 9 * * *` - Daily at 9:00 AM UTC
- `0 */6 * * *` - Every 6 hours
- `0 9 * * 1` - Every Monday at 9:00 AM
- `0 9,15 * * *` - Twice daily (9 AM and 3 PM)

### Customize Layout

Edit `_layouts/unified-post.html` to change:
- Colors (CSS variables)
- Grid layout
- Hero image height
- Sidebar content
- Footer design

## 🧪 Testing

### Test Locally

1. **Generate a tutorial**:
```bash
bash scripts/generate-tutorials.sh 1
```

2. **Build Jekyll site**:
```bash
bundle exec jekyll build
```

3. **Serve locally**:
```bash
bundle exec jekyll serve
```

4. **Open browser**: http://localhost:4000

### Test Image Generation

```python
# Test XAI Image API
python3 << 'EOF'
import requests
import os

XAI_API_KEY = os.getenv('XAI_API_KEY')

response = requests.post(
    "https://api.x.ai/v1/images/generations",
    headers={
        "Authorization": f"Bearer {XAI_API_KEY}",
        "Content-Type": "application/json"
    },
    json={
        "model": "grok-2-vision-1212",
        "prompt": "Professional tech blog featured image: Modern AI Technology",
        "n": 1,
        "size": "1024x1024"
    }
)

print(response.json())
EOF
```

## 📊 What Gets Generated

Each tutorial includes:

### Frontmatter (Jekyll metadata):
```yaml
---
layout: unified-post
title: "Tutorial Title"
description: "SEO description..."
date: 2025-12-04 HH:MM:SS +0200
categories: [Tutorial, Development]
tags: [tag1, tag2, tag3]
author: "Tech Insights"
image: "https://..."  # XAI-generated image
image_credit: "Generated with XAI"
image_credit_url: "https://x.ai"
---
```

### Content Structure:
1. Introduction with use cases
2. Prerequisites and tools
3. Step-by-step implementation
4. Code examples (multiple languages)
5. Best practices
6. Common pitfalls
7. Advanced techniques
8. Real-world examples
9. Conclusion and next steps

## 🐛 Troubleshooting

### API Key Issues

```bash
# Check if key is set
echo $XAI_API_KEY

# Should output: xai-...
```

### Permission Issues

```bash
# Make scripts executable
chmod +x scripts/generate_tutorial.py
chmod +x scripts/generate-tutorials.sh
```

### Python Dependencies

```bash
# Reinstall
pip install --force-reinstall requests
```

### GitHub Actions Not Running

1. Check if workflow is enabled (Actions tab)
2. Verify `XAI_API_KEY` secret is set
3. Check workflow logs for errors
4. Ensure schedule syntax is correct

## 📈 Performance

- **Content Generation**: ~30-60 seconds per tutorial
- **Image Generation**: ~10-30 seconds per image
- **Total Time**: ~3-5 minutes for 3 tutorials
- **Cost**: Depends on XAI API pricing

## 🔒 Security

- API key stored as GitHub Secret (encrypted)
- Never commit API keys to repository
- Use environment variables locally
- Tokens auto-masked in git commits (via CLAUDE.md config)

## 📝 Best Practices

1. **Review Generated Content**: Always review before publishing
2. **Test Locally First**: Run `generate-tutorials.sh` locally before automating
3. **Monitor API Usage**: Keep track of XAI API costs
4. **Customize Topics**: Update `HOT_TOPICS` list regularly
5. **SEO Optimization**: Review tags and descriptions
6. **Image Quality**: Verify featured images load correctly

## 🚀 Advanced Usage

### Custom Prompts

Edit `generate_tutorial.py` to customize the AI prompt:
```python
prompt = f"""Create a tutorial about: "{topic}"

Custom requirements here...
"""
```

### Multiple Workflows

Create additional workflow files for different schedules:
- `morning-tutorials.yml` - 3 tutorials at 9 AM
- `evening-tutorials.yml` - 2 tutorials at 6 PM
- `weekend-tutorials.yml` - 5 tutorials on Sunday

### Integration with n8n

Create an n8n workflow to:
1. Trigger GitHub Actions via webhook
2. Monitor published tutorials
3. Share to social media automatically
4. Send Telegram notifications

## 📚 Resources

- [XAI API Documentation](https://docs.x.ai)
- [Jekyll Documentation](https://jekyllrb.com)
- [GitHub Actions Docs](https://docs.github.com/actions)
- [Markdown Guide](https://www.markdownguide.org)

## 🎉 Success Metrics

Track your blog growth:
- Number of tutorials published
- Total content generated (words)
- Featured images created
- Topics covered
- Automation uptime

## 📞 Support

If you encounter issues:
1. Check this documentation
2. Review error logs in GitHub Actions
3. Test locally with verbose output
4. Check XAI API status

---

**Created with ❤️ using Claude Code and XAI API**

Last Updated: 2025-12-04

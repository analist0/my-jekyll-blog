# 🚀 Workflow Upload Instructions

## בעיה

אי אפשר לדחוף workflow files דרך Git בגלל מגבלת אבטחה:
```
refusing to allow an OAuth App to create or update workflow
`.github/workflows/daily_blog_publisher.yml` without `workflow` scope
```

## פתרון: העלאה דרך GitHub Web UI

### שלב 1: פתח את ה-Repository ב-Browser

```bash
cd ~/my-jekyll-blog
gh browse
```

או גש ישירות: https://github.com/analist0/my-jekyll-blog

### שלב 2: נווט ל-Workflows Directory

1. לחץ על `.github/`
2. לחץ על `workflows/`
3. לחץ על "Add file" → "Upload files"

### שלב 3: העלה את ה-Workflow

**Workflow שצריך להעלות**: `daily_blog_publisher.yml`

**מיקום מקומי**: `~/my-jekyll-blog/.github/workflows/daily_blog_publisher.yml`

**תוכן הקובץ** (העתק את הקוד הזה):

```yaml
name: Daily Professional Blog Posts

on:
  schedule:
    # Run 3 times per day: 8 AM, 2 PM, 8 PM UTC (10 AM, 4 PM, 10 PM Israel time)
    - cron: '0 8 * * *'   # Morning post
    - cron: '0 14 * * *'  # Afternoon post
    - cron: '0 20 * * *'  # Evening post
  workflow_dispatch:      # Allow manual triggering

jobs:
  generate-blog-post:
    runs-on: ubuntu-latest

    steps:
      - name: 📥 Checkout repository
        uses: actions/checkout@v4
        with:
          token: ${{ secrets.GITHUB_TOKEN }}
          fetch-depth: 0

      - name: 🐍 Setup Python 3.11
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'
          cache: 'pip'

      - name: 📦 Install Python dependencies
        run: |
          python -m pip install --upgrade pip
          pip install requests

      - name: 🤖 Generate professional blog post
        run: |
          python3 scripts/ai_trend_publisher_v2.py
        env:
          XAI_API_KEY: ${{ secrets.XAI_API_KEY }}
          X_BEARER_TOKEN: ${{ secrets.X_BEARER_TOKEN }}

      - name: 🎨 Generate hero images (if possible)
        run: |
          # Find newly created posts (last 10 minutes)
          NEW_POSTS=$(find _posts -name "*.md" -mmin -10)

          if [ ! -z "$NEW_POSTS" ]; then
            echo "📸 Generating hero images for new posts..."
            for post in $NEW_POSTS; do
              echo "   Processing: $post"
              python3 scripts/generate_ai_image.py "$post" || echo "⚠️  Image generation skipped for $post"
            done
          else
            echo "ℹ️  No new posts found"
          fi
        env:
          XAI_API_KEY: ${{ secrets.XAI_API_KEY }}
        continue-on-error: true

      - name: 📊 Commit and push changes
        run: |
          git config --local user.name "github-actions[bot]"
          git config --local user.email "github-actions[bot]@users.noreply.github.com"

          # Add new posts
          git add _posts/

          # Check if there are changes
          if git diff --staged --quiet; then
            echo "ℹ️  No new posts to commit"
            exit 0
          fi

          # Get current time slot
          HOUR=$(date +%H)
          if [ $HOUR -lt 12 ]; then
            TIME_SLOT="🌅 Morning"
          elif [ $HOUR -lt 18 ]; then
            TIME_SLOT="☀️ Afternoon"
          else
            TIME_SLOT="🌙 Evening"
          fi

          # Count new posts
          POST_COUNT=$(git diff --staged --name-only | grep "_posts/" | wc -l)

          # Create commit message
          COMMIT_MSG="${TIME_SLOT} Blog Update: ${POST_COUNT} new professional post(s)

🤖 Auto-generated with X.AI Grok
📅 $(date +'%Y-%m-%d %H:%M:%S %Z')
🔍 Topics from X trending searches

[skip ci]"

          git commit -m "$COMMIT_MSG"
          git push

          echo "✅ Successfully published ${POST_COUNT} new post(s)!"

      - name: 📢 Summary
        if: always()
        run: |
          echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
          echo "📊 Workflow Summary"
          echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
          echo "Date: $(date +'%Y-%m-%d %H:%M:%S %Z')"
          echo "Posts directory: $(ls -1 _posts/*.md 2>/dev/null | wc -l) total posts"
          echo "Latest posts:"
          ls -lt _posts/*.md | head -3 | awk '{print "  - " $NF}'
          echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
```

### שלב 4: Commit Message

```
🤖 Add daily blog publisher workflow

- Automated blog post generation 3x per day
- Uses X.AI Grok for content generation
- Integrates with X trending topics
- Automatic commit and push
```

---

## שלב הבא: הוספת Secrets

אחרי העלאת ה-workflow, צריך להוסיף secrets:

### נדרשים:
1. **XAI_API_KEY** - חובה לייצור תוכן
2. **X_BEARER_TOKEN** - אופציונלי (לטרנדים אמיתיים)

### איך להוסיף:

1. Repository → **Settings** → **Secrets and variables** → **Actions**
2. לחץ **"New repository secret"**
3. הוסף:
   - Name: `XAI_API_KEY`
   - Value: `xai-...` (המפתח שלך)
4. חזור על זה ל-`X_BEARER_TOKEN` (אם יש לך)

---

## בדיקה

אחרי ההעלאה:

```bash
# בדוק שה-workflow קיים
cd ~/my-jekyll-blog
gh workflow list

# הרץ ידנית
gh workflow run "Daily Professional Blog Posts"

# בדוק סטטוס
gh run list --workflow="Daily Professional Blog Posts" --limit 3
```

---

## לקריאה נוספת

- `AUTO-BLOG-SETUP.md` - מדריך התקנה מלא
- `MODERN-BLOG-GUIDE.md` - מדריך למערכת הבלוג
- `scripts/ai_trend_publisher_v2.py` - הסקריפט שמייצר פוסטים

---

✅ **סטטוס נוכחי**:
- ✅ כל הקוד נדחף ל-GitHub
- ⏳ רק ה-workflow צריך העלאה ידנית
- ⏳ אחרי זה להוסיף secrets

📅 עודכן: 2025-12-04

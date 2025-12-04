#!/bin/bash
# 🤖 Tutorial Generator Runner Script

set -e

# Colors
GREEN='\033[0;32m'
BLUE='\033[0;34m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo -e "${BLUE}🤖 Tutorial Generator with XAI API${NC}"
echo "========================================"
echo ""

# Check for XAI_API_KEY
if [ -z "$XAI_API_KEY" ]; then
    echo -e "${RED}❌ XAI_API_KEY not set!${NC}"
    echo ""
    echo "Set it with:"
    echo "  export XAI_API_KEY='your-key-here'"
    echo ""
    exit 1
fi

# Get number of tutorials (default: 3)
NUM_TUTORIALS=${1:-3}

echo -e "${GREEN}📝 Generating $NUM_TUTORIALS tutorials...${NC}"
echo ""

# Navigate to blog directory
cd ~/my-jekyll-blog

# Step 1: Discover trending topics
echo -e "${BLUE}🔍 Step 1: Discovering trending topics...${NC}"
python3 scripts/discover_trending_topics.py

if [ $? -ne 0 ]; then
    echo -e "${RED}⚠️ Failed to discover trending topics, will use fallback${NC}"
fi

echo ""

# Step 2: Generate tutorials
echo -e "${BLUE}🤖 Step 2: Generating tutorials...${NC}"
export NUM_TUTORIALS=$NUM_TUTORIALS
python3 scripts/generate_tutorial.py

# Check if successful
if [ $? -eq 0 ]; then
    echo ""
    echo -e "${GREEN}✅ Success!${NC}"
    echo ""
    echo "📁 New posts created in: _posts/"
    echo ""
    echo "Next steps:"
    echo "  1. Review the generated posts"
    echo "  2. Build Jekyll: bundle exec jekyll build"
    echo "  3. Test locally: bundle exec jekyll serve"
    echo "  4. Commit and push to GitHub"
    echo ""
else
    echo ""
    echo -e "${RED}❌ Failed to generate tutorials${NC}"
    exit 1
fi

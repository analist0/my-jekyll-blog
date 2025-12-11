#!/usr/bin/env python3
"""
AI Content Generator - Modular System
Uses one AI API key for everything: trends, sentiment, images, content
"""

import os
import json
import datetime
import requests
from pathlib import Path


class AIContentGenerator:
    """Main AI content generator using single API key"""

    def __init__(self, api_key=None, api_provider="xai"):
        """
        Initialize with single API key

        Args:
            api_key: Your AI API key (xAI, Gemini, Perplexity)
            api_provider: "xai", "gemini", "perplexity"
        """
        self.api_key = api_key or os.environ.get('AI_API_KEY')
        self.api_provider = api_provider.lower()

        if not self.api_key:
            raise ValueError("AI_API_KEY environment variable must be set")

    def analyze_trends(self, topic=None, location="worldwide"):
        """
        Module 1: Analyze current trends using AI
        No Twitter API needed - AI generates relevant trending topics
        """
        prompt = f"""
        Generate a list of 10 current trending topics for {location}.
        Focus on: technology, AI, social media, current events.

        Return as JSON array: ["topic1", "topic2", ...]
        """

        return self._call_ai(prompt, response_format="json")

    def analyze_sentiment(self, topic, tweets_sample=None):
        """
        Module 2: Analyze sentiment using AI
        """
        prompt = f"""
        Analyze the sentiment around this topic: "{topic}"

        Consider:
        - Public opinion
        - Emotional tone (positive/negative/neutral)
        - Key concerns or excitement

        Return JSON with:
        {{
            "sentiment": "positive/negative/neutral",
            "score": 0.0-1.0,
            "summary": "brief summary",
            "key_points": ["point1", "point2"]
        }}
        """

        return self._call_ai(prompt, response_format="json")

    def generate_article(self, topic, sentiment_data):
        """
        Module 3: Generate blog article using AI
        """
        prompt = f"""
        Write a blog post about: "{topic}"

        Sentiment: {sentiment_data.get('sentiment', 'neutral')}
        Key points: {', '.join(sentiment_data.get('key_points', []))}

        Write in Hebrew. Include:
        - Catchy title
        - Introduction
        - Main content (3-4 paragraphs)
        - Conclusion

        Format as Jekyll markdown with front matter.
        """

        return self._call_ai(prompt)

    def generate_image(self, topic, description=None):
        """
        Module 4: Generate image using AI
        Note: xAI, Gemini, Perplexity don't have image generation yet
        """
        print(f"⚠️ Image generation not supported for {self.api_provider}")
        return None

    def _call_ai(self, prompt, response_format="text"):
        """
        Internal: Call AI API based on provider
        """
        if self.api_provider == "xai":
            return self._call_xai(prompt, response_format)
        elif self.api_provider == "gemini":
            return self._call_gemini(prompt, response_format)
        elif self.api_provider == "perplexity":
            return self._call_perplexity(prompt, response_format)
        else:
            raise ValueError(f"Unsupported provider: {self.api_provider}")

    def _call_xai(self, prompt, response_format="text"):
        """xAI (Grok) API call"""
        url = "https://api.x.ai/v1/chat/completions"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        # Add JSON instruction if needed
        if response_format == "json":
            prompt += "\n\nReturn ONLY valid JSON, no other text."

        data = {
            "model": "grok-2-latest",
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.7,
            "max_tokens": 4096
        }

        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()

        result = response.json()
        content = result['choices'][0]['message']['content']

        if response_format == "json":
            # Extract JSON from markdown code blocks if present
            content = content.strip()
            if content.startswith("```json"):
                content = content.split("```json")[1].split("```")[0].strip()
            elif content.startswith("```"):
                content = content.split("```")[1].split("```")[0].strip()
            return json.loads(content)
        return content

    def _call_gemini(self, prompt, response_format="text"):
        """Google Gemini API call"""
        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key={self.api_key}"

        # Add JSON instruction if needed
        if response_format == "json":
            prompt += "\n\nReturn ONLY valid JSON, no other text."

        data = {
            "contents": [{"parts": [{"text": prompt}]}],
            "generationConfig": {
                "temperature": 0.7,
                "maxOutputTokens": 4096
            }
        }

        response = requests.post(url, json=data)
        response.raise_for_status()

        result = response.json()
        content = result['candidates'][0]['content']['parts'][0]['text']

        if response_format == "json":
            # Extract JSON from markdown code blocks if present
            content = content.strip()
            if content.startswith("```json"):
                content = content.split("```json")[1].split("```")[0].strip()
            elif content.startswith("```"):
                content = content.split("```")[1].split("```")[0].strip()
            return json.loads(content)
        return content

    def _call_perplexity(self, prompt, response_format="text"):
        """Perplexity API call"""
        url = "https://api.perplexity.ai/chat/completions"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        # Add JSON instruction if needed
        if response_format == "json":
            prompt += "\n\nReturn ONLY valid JSON, no other text."

        data = {
            "model": "llama-3.1-sonar-large-128k-online",
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.7,
            "max_tokens": 4096
        }

        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()

        result = response.json()
        content = result['choices'][0]['message']['content']

        if response_format == "json":
            # Extract JSON from markdown code blocks if present
            content = content.strip()
            if content.startswith("```json"):
                content = content.split("```json")[1].split("```")[0].strip()
            elif content.startswith("```"):
                content = content.split("```")[1].split("```")[0].strip()
            return json.loads(content)
        return content


def main():
    """Main workflow"""
    print("🤖 AI Content Generator Started")

    # Initialize generator
    api_provider = os.environ.get('AI_PROVIDER', 'xai')
    print(f"Using provider: {api_provider}")
    generator = AIContentGenerator(api_provider=api_provider)

    # Module 1: Get trends
    print("📊 Analyzing trends...")
    trends = generator.analyze_trends()
    print(f"Found {len(trends)} trending topics")

    # Pick top trend
    top_trend = trends[0] if trends else "AI Technology"
    print(f"Selected topic: {top_trend}")

    # Module 2: Analyze sentiment
    print("💭 Analyzing sentiment...")
    sentiment = generator.analyze_sentiment(top_trend)
    print(f"Sentiment: {sentiment['sentiment']} ({sentiment['score']})")

    # Module 3: Generate article
    print("✍️ Generating article...")
    article = generator.generate_article(top_trend, sentiment)

    # Save article
    date_str = datetime.datetime.now().strftime("%Y-%m-%d")
    filename = f"_posts/{date_str}-{top_trend.lower().replace(' ', '-')[:50]}.md"

    Path("_posts").mkdir(exist_ok=True)
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(article)

    print(f"✅ Article saved: {filename}")

    # Module 4: Generate image (optional)
    if os.environ.get('GENERATE_IMAGE', 'false').lower() == 'true':
        print("🎨 Generating image...")
        try:
            image_url = generator.generate_image(
                top_trend,
                f"A modern, professional image representing {top_trend}"
            )
            print(f"Image URL: {image_url}")
        except Exception as e:
            print(f"Image generation skipped: {e}")

    print("🎉 Done!")


if __name__ == "__main__":
    main()

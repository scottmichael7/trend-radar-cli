import json
import urllib.request
from collections import Counter
import re

# Simulate fetching GitHub trending repos data (replace with actual API in production)
def fetch_trending():
    # Mock data based on provided repos
    return [
        {"name": "folkbench", "desc": "AI API relay benchmark"},
        {"name": "solid-glass", "desc": "Design system for AI apps"},
        {"name": "new-term-radar", "desc": "Daily radar for new AI terms"},
        {"name": "indra", "desc": "1M param OCR model"},
        {"name": "motionmaxxing", "desc": "Looksmaxxing for motion graphics"}
    ]

def extract_terms(repos):
    # Simple keyword extraction (split alphanumeric)
    terms = []
    for r in repos:
        text = (r["name"] + " " + r["desc"]).lower()
        words = re.findall(r'[a-z0-9]+', text)
        terms.extend(words)
    return terms

def main():
    repos = fetch_trending()
    terms = extract_terms(repos)
    # Count frequency (simple trend detection)
    counter = Counter(terms)
    # Filter stopwords (very basic)
    stopwords = {"a", "an", "the", "for", "and", "of", "in", "on", "to", "with", "new", "ai", "app"}
    trending = {k: v for k, v in counter.items() if k not in stopwords and len(k) > 3}
    # Output top 5
    print("Top trending terms from GitHub repos:")
    for term, count in sorted(trending.items(), key=lambda x: -x[1])[:5]:
        print(f"  {term}: {count}")

if __name__ == "__main__":
    main()

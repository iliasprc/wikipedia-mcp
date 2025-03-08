#!/usr/bin/env python3
"""
Example script demonstrating how to use the Wikipedia MCP server.
"""

import asyncio
import json
import sys
import os

# Add the parent directory to the path so we can import the wikipedia_mcp package
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from wikipedia_mcp.wikipedia_client import WikipediaClient

async def main():
    """Run the example."""
    # Create a Wikipedia client
    client = WikipediaClient()
    
    # Get a search query from the command line or use a default
    query = sys.argv[1] if len(sys.argv) > 1 else "Artificial Intelligence"
    
    print(f"Searching Wikipedia for: {query}")
    
    # Search for articles
    results = client.search(query, limit=5)
    
    print(f"Found {len(results)} results:")
    for i, result in enumerate(results):
        print(f"{i+1}. {result['title']} - {result.get('wordcount', 0)} words")
    
    if results:
        # Get the first article
        title = results[0]['title']
        print(f"\nGetting summary for: {title}")
        
        # Get the summary
        summary = client.get_summary(title)
        
        print("\nSummary:")
        print(summary[:500] + "..." if len(summary) > 500 else summary)
        
        # Get related topics
        print("\nRelated topics:")
        related = client.get_related_topics(title, limit=5)
        
        for i, topic in enumerate(related):
            print(f"{i+1}. {topic['title']} ({topic['type']})")
            if topic['type'] == 'link' and 'summary' in topic:
                print(f"   {topic['summary'][:100]}...")

if __name__ == "__main__":
    asyncio.run(main()) 
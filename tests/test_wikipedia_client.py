"""
Tests for the Wikipedia client.
"""

import unittest
import sys
import os

# Add the parent directory to the path so we can import the wikipedia_mcp package
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from wikipedia_mcp.wikipedia_client import WikipediaClient

class TestWikipediaClient(unittest.TestCase):
    """Tests for the Wikipedia client."""

    def setUp(self):
        """Set up the test case."""
        self.client = WikipediaClient()

    def test_search(self):
        """Test searching Wikipedia."""
        results = self.client.search("Python programming language", limit=5)
        self.assertIsInstance(results, list)
        self.assertLessEqual(len(results), 5)
        if results:
            self.assertIn('title', results[0])
            self.assertIn('snippet', results[0])

    def test_get_summary(self):
        """Test getting a Wikipedia article summary."""
        summary = self.client.get_summary("Python (programming language)")
        self.assertIsInstance(summary, str)
        self.assertGreater(len(summary), 0)

    def test_get_article(self):
        """Test getting a Wikipedia article."""
        article = self.client.get_article("Python (programming language)")
        self.assertIsInstance(article, dict)
        self.assertIn('title', article)
        self.assertIn('summary', article)
        self.assertIn('text', article)
        self.assertIn('url', article)
        self.assertIn('exists', article)
        self.assertTrue(article['exists'])

    def test_get_sections(self):
        """Test getting Wikipedia article sections."""
        sections = self.client.get_sections("Python (programming language)")
        self.assertIsInstance(sections, list)
        if sections:
            self.assertIn('title', sections[0])
            self.assertIn('text', sections[0])
            self.assertIn('level', sections[0])

    def test_get_links(self):
        """Test getting Wikipedia article links."""
        links = self.client.get_links("Python (programming language)")
        self.assertIsInstance(links, list)
        self.assertGreater(len(links), 0)

    def test_get_related_topics(self):
        """Test getting related topics."""
        related = self.client.get_related_topics("Python (programming language)", limit=5)
        self.assertIsInstance(related, list)
        self.assertLessEqual(len(related), 5)
        if related:
            self.assertIn('title', related[0])
            self.assertIn('type', related[0])

    def test_nonexistent_page(self):
        """Test handling of nonexistent pages."""
        article = self.client.get_article("ThisPageDoesNotExistOnWikipedia12345")
        self.assertIsInstance(article, dict)
        self.assertIn('exists', article)
        self.assertFalse(article['exists'])

if __name__ == '__main__':
    unittest.main() 
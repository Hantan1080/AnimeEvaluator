# test_animeevaluator.py
"""
Tests for AnimeEvaluator module.
"""

import unittest
from animeevaluator import AnimeEvaluator

class TestAnimeEvaluator(unittest.TestCase):
    """Test cases for AnimeEvaluator class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = AnimeEvaluator()
        self.assertIsInstance(instance, AnimeEvaluator)
        
    def test_run_method(self):
        """Test the run method."""
        instance = AnimeEvaluator()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()

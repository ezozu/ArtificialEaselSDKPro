# test_artificialeaselsdkpro.py
"""
Tests for ArtificialEaselSDKPro module.
"""

import unittest
from artificialeaselsdkpro import ArtificialEaselSDKPro

class TestArtificialEaselSDKPro(unittest.TestCase):
    """Test cases for ArtificialEaselSDKPro class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ArtificialEaselSDKPro()
        self.assertIsInstance(instance, ArtificialEaselSDKPro)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ArtificialEaselSDKPro()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()

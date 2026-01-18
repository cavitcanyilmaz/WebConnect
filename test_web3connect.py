# test_web3connect.py
"""
Tests for Web3Connect module.
"""

import unittest
from web3connect import Web3Connect

class TestWeb3Connect(unittest.TestCase):
    """Test cases for Web3Connect class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = Web3Connect()
        self.assertIsInstance(instance, Web3Connect)
        
    def test_run_method(self):
        """Test the run method."""
        instance = Web3Connect()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()

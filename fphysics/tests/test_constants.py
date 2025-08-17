"""
Test constants module for verifying physical constants.
"""

import unittest
import sys
import os
from constants import SPEED_OF_LIGHT, PLANCK_CONSTANT, GRAVITATIONAL_CONSTANT

class TestConstants(unittest.TestCase):
    """Test physical constants"""
    
    def test_speed_of_light(self):
        """Test speed of light value"""
        self.assertAlmostEqual(SPEED_OF_LIGHT, 2.99792458e8, places=5)
    
    def test_planck_constant(self):
        """Test Planck constant value"""
        self.assertAlmostEqual(PLANCK_CONSTANT, 6.62607015e-34, places=40)
    
    def test_gravitational_constant(self):
        """Test gravitational constant value"""
        self.assertAlmostEqual(GRAVITATIONAL_CONSTANT, 6.67430e-11, places=15)

if __name__ == '__main__':
    unittest.main()

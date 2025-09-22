import unittest
import sys
import os
from ..constants import REDUCED_PLANCK

class TestHarmonicOscillator(unittest.TestCase):
    
    def test_energy_levels(self):
        # E_n = ħω(n + 1/2)
        omega = 1e14  # angular frequency
        n = 0  # ground state
        
        energy_ground = REDUCED_PLANCK * omega * (n + 0.5)
        self.assertGreater(energy_ground, 0)
    
    def test_zero_point_energy(self):
        """Test zero-point energy"""
        omega = 1e14
        zero_point_energy = 0.5 * REDUCED_PLANCK * omega
        self.assertGreater(zero_point_energy, 0)

if __name__ == '__main__':
    unittest.main()


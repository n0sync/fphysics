"""
Test electromagnetism electrostatics module.
"""

import unittest
import sys
import os
from constants import COULOMB_CONSTANT, ELEMENTARY_CHARGE

class TestElectrostatics(unittest.TestCase):
    """Test electrostatics functions"""
    
    def test_coulomb_force(self):
        """Test Coulomb's law force calculation"""
        charge1 = ELEMENTARY_CHARGE
        charge2 = ELEMENTARY_CHARGE
        distance = 1e-10  # 1 Angstrom
        
        force = COULOMB_CONSTANT * charge1 * charge2 / distance**2
        self.assertGreater(force, 0)
    
    def test_electric_field(self):
        """Test electric field calculation"""
        charge = ELEMENTARY_CHARGE
        distance = 1e-9  # 1 nm
        
        electric_field = COULOMB_CONSTANT * charge / distance**2
        self.assertGreater(electric_field, 0)

if __name__ == '__main__':
    unittest.main()

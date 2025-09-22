import unittest
import sys
import os
from ..constants import COULOMB_CONSTANT, ELEMENTARY_CHARGE

class TestElectrostatics(unittest.TestCase):
    
    def test_coulomb_force(self):
        charge1 = ELEMENTARY_CHARGE
        charge2 = ELEMENTARY_CHARGE
        distance = 1e-10
        
        force = COULOMB_CONSTANT * charge1 * charge2 / distance**2
        self.assertGreater(force, 0)
    
    def test_electric_field(self):
        charge = ELEMENTARY_CHARGE
        distance = 1e-9
        
        electric_field = COULOMB_CONSTANT * charge / distance**2
        self.assertGreater(electric_field, 0)

if __name__ == '__main__':
    unittest.main()

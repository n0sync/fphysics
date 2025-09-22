import unittest
import sys
import os
from ..constants import GAS_CONSTANT

class TestThermodynamicsLaws(unittest.TestCase):
    
    def test_ideal_gas_law(self):
        """Test ideal gas law PV = nRT"""
        pressure = 101325  # Pa
        volume = 0.0224  # m³
        n_moles = 1  # mol
        temperature = pressure * volume / (n_moles * GAS_CONSTANT)
        self.assertAlmostEqual(temperature, 273.15, places=0)
    
    def test_first_law_energy_conservation(self):
        # ΔU = Q - W (change in internal energy = heat - work)
        heat_added = 1000  # J
        work_done = 400  # J
        delta_internal_energy = heat_added - work_done
        self.assertEqual(delta_internal_energy, 600)

if __name__ == '__main__':
    unittest.main()


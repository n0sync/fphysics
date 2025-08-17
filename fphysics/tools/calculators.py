"""
Interactive calculators for performing physics computations.
"""

from constants import GRAVITATIONAL_CONSTANT, ELEMENTARY_CHARGE

class PhysicsCalculator:
    """Basic physics calculator"""
    
    def calculate_force_gravity(self, mass1, mass2, distance):
        """Calculate gravitational force between two masses"""
        return GRAVITATIONAL_CONSTANT * (mass1 * mass2) / distance**2

    def calculate_coulomb_force(self, charge1, charge2, distance):
        """Calculate electrostatic force between two charges"""
        return ELEMENTARY_CHARGE * (charge1 * charge2) / distance**2

class UnitConverter:
    """Converter for units"""
    
    def joules_to_calories(self, joules):
        """Convert joules to calories"""
        CALORIE_TO_JOULE = 4.184
        return joules / CALORIE_TO_JOULE

    def meters_to_kilometers(self, meters):
        """Convert meters to kilometers"""
        return meters / 1000

class FormulaCalculator:
    """Calculator for physics formulas"""
    
    def calculate_energy(self, mass, velocity):
        """Calculate kinetic energy of a moving object"""
        return 0.5 * mass * velocity**2

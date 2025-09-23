from ..constants import GRAVITATIONAL_CONSTANT, ELEMENTARY_CHARGE

class PhysicsCalculator:
    def calculate_force_gravity(self, mass1, mass2, distance):
        return GRAVITATIONAL_CONSTANT * (mass1 * mass2) / distance**2

    def calculate_coulomb_force(self, charge1, charge2, distance):
        return ELEMENTARY_CHARGE * (charge1 * charge2) / distance**2

class UnitConverter:
    def joules_to_calories(self, joules):
        CALORIE_TO_JOULE = 4.184
        return joules / CALORIE_TO_JOULE

    def meters_to_kilometers(self, meters):
        return meters / 1000

class FormulaCalculator:
    def calculate_energy(self, mass, velocity):
        return 0.5 * mass * velocity**2

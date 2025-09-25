from ..constants import GRAVITATIONAL_CONSTANT, COULOMB_CONSTANT

def calculate_gravitational_force(mass1, mass2, distance):
    if distance <= 0:
        raise ValueError("Distance must be positive")
    
    return GRAVITATIONAL_CONSTANT * (mass1 * mass2) / distance**2

def calculate_coulomb_force(charge1, charge2, distance):
    if distance <= 0:
        raise ValueError("Distance must be positive")
        
    return COULOMB_CONSTANT * abs(charge1 * charge2) / distance**2

def joules_to_calories(joules):
    JOULE_TO_CALORIE = 0.239006
    return joules * JOULE_TO_CALORIE

def meters_to_kilometers(meters):
    return meters / 1000

def calculate_kinetic_energy(mass, velocity):
    if mass < 0:
        raise ValueError("Mass cannot be negative")
        
    return 0.5 * mass * velocity**2

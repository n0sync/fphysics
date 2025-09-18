import math
from ..constants import *

def lorentz_factor(velocity):
    return 1 / math.sqrt(1 - (velocity / SPEED_OF_LIGHT)**2)

def time_dilation(proper_time, velocity):
    return proper_time * lorentz_factor(velocity)

def length_contraction(proper_length, velocity):
    return proper_length / lorentz_factor(velocity)

def relativistic_momentum(mass, velocity):
    return mass * velocity * lorentz_factor(velocity)

def relativistic_energy(mass, velocity):
    return mass * SPEED_OF_LIGHT**2 * lorentz_factor(velocity)

def kinetic_energy(mass, velocity):
    return mass * SPEED_OF_LIGHT**2 * (lorentz_factor(velocity) - 1)

def velocity_addition(v1, v2):
    return (v1 + v2) / (1 + (v1 * v2) / SPEED_OF_LIGHT**2)

def doppler_shift(frequency, velocity):
    beta = velocity / SPEED_OF_LIGHT
    return frequency * math.sqrt((1 + beta) / (1 - beta))

def mass_energy_equivalence(mass):
    return mass * SPEED_OF_LIGHT**2

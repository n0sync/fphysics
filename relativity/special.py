"""Special relativity calculations"""

import math
from constants import *


def lorentz_factor(velocity):
    """Calculate Lorentz factor γ"""
    return 1 / math.sqrt(1 - (velocity / SPEED_OF_LIGHT)**2)


def time_dilation(proper_time, velocity):
    """Calculate dilated time"""
    return proper_time * lorentz_factor(velocity)


def length_contraction(proper_length, velocity):
    """Calculate contracted length"""
    return proper_length / lorentz_factor(velocity)


def relativistic_momentum(mass, velocity):
    """Calculate relativistic momentum"""
    return mass * velocity * lorentz_factor(velocity)


def relativistic_energy(mass, velocity):
    """Calculate total relativistic energy"""
    return mass * SPEED_OF_LIGHT**2 * lorentz_factor(velocity)


def kinetic_energy(mass, velocity):
    """Calculate relativistic kinetic energy"""
    return mass * SPEED_OF_LIGHT**2 * (lorentz_factor(velocity) - 1)


def velocity_addition(v1, v2):
    """Calculate relativistic velocity addition"""
    return (v1 + v2) / (1 + (v1 * v2) / SPEED_OF_LIGHT**2)


def doppler_shift(frequency, velocity):
    """Calculate relativistic Doppler shift"""
    beta = velocity / SPEED_OF_LIGHT
    return frequency * math.sqrt((1 + beta) / (1 - beta))


def mass_energy_equivalence(mass):
    """Calculate energy from mass (E=mc²)"""
    return mass * SPEED_OF_LIGHT**2

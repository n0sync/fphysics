import math
import numpy as np
from constants import *

def hubble_law(distance):
    """Calculate recession velocity using Hubble's law"""
    return HUBBLE_CONSTANT * distance


def critical_density():
    """Return critical density of the universe"""
    return CRITICAL_DENSITY_UNIVERSE


def age_of_universe(h0=HUBBLE_CONSTANT):
    """Estimate age of universe (flat, matter-dominated)"""
    return 2 / (3 * h0)


def comoving_distance(redshift, h0=HUBBLE_CONSTANT):
    """Calculate comoving distance from redshift"""
    return SPEED_OF_LIGHT * redshift / h0


def luminosity_distance(redshift):
    """Calculate luminosity distance"""
    return comoving_distance(redshift) * (1 + redshift)


def angular_diameter_distance(redshift):
    """Calculate angular diameter distance"""
    return comoving_distance(redshift) / (1 + redshift)**2


def scale_factor_evolution(time, matter_density=0.3):
    """Scale factor evolution in matter-dominated universe"""
    return (time / age_of_universe())**(2/3)


def friedmann_equation(scale_factor, matter_density=0.3, lambda_density=0.7):
    """Friedmann equation for expanding universe"""
    h_squared = (8 * math.pi * GRAVITATIONAL_CONSTANT / 3) * (
        matter_density / scale_factor**3 + lambda_density
    )
    return math.sqrt(h_squared)


def deceleration_parameter(matter_density=0.3, lambda_density=0.7):
    """Calculate deceleration parameter"""
    return matter_density / 2 - lambda_density


def cosmic_microwave_background_temp(redshift):
    """CMB temperature at given redshift"""
    return COSMIC_MICROWAVE_BACKGROUND_TEMP * (1 + redshift)


def jeans_length(temperature, density, mean_molecular_weight=1):
    """Calculate Jeans length for gravitational instability"""
    from ..constants import BOLTZMANN_CONSTANT, ATOMIC_MASS_UNIT
    cs = math.sqrt(BOLTZMANN_CONSTANT * temperature / (mean_molecular_weight * ATOMIC_MASS_UNIT))
    return math.sqrt(math.pi * cs**2 / (GRAVITATIONAL_CONSTANT * density))


def schwarzschild_horizon_cosmology(mass):
    """Schwarzschild radius in cosmological context"""
    return 2 * GRAVITATIONAL_CONSTANT * mass / SPEED_OF_LIGHT**2


def redshift_to_lookback_time(redshift, h0=HUBBLE_CONSTANT):
    """Convert redshift to lookback time (simplified)"""
    return (2 / (3 * h0)) * (1 - 1/math.sqrt(1 + redshift))


def density_parameter(density_type, critical_density=CRITICAL_DENSITY_UNIVERSE):
    """Calculate density parameter Omega"""
    return density_type / critical_density


def sound_horizon(redshift_recombination=1100):
    """Calculate sound horizon at recombination"""
    return SPEED_OF_LIGHT / (3 * HUBBLE_CONSTANT * math.sqrt(redshift_recombination))

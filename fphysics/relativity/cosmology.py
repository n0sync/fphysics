import math
import numpy as np
from ..constants import *

def hubble_law(distance):
    return HUBBLE_CONSTANT * distance

def critical_density():
    return CRITICAL_DENSITY_UNIVERSE

def age_of_universe(h0=HUBBLE_CONSTANT):
    return 2 / (3 * h0)

def comoving_distance(redshift, h0=HUBBLE_CONSTANT):
    return SPEED_OF_LIGHT * redshift / h0

def luminosity_distance(redshift):
    return comoving_distance(redshift) * (1 + redshift)

def angular_diameter_distance(redshift):
    return comoving_distance(redshift) / (1 + redshift)**2

def scale_factor_evolution(time, matter_density=0.3):
    return (time / age_of_universe())**(2/3)

def friedmann_equation(scale_factor, matter_density=0.3, lambda_density=0.7):
    h_squared = (8 * math.pi * GRAVITATIONAL_CONSTANT / 3) * (
        matter_density / scale_factor**3 + lambda_density
    )
    return math.sqrt(h_squared)

def deceleration_parameter(matter_density=0.3, lambda_density=0.7):
    return matter_density / 2 - lambda_density

def cosmic_microwave_background_temp(redshift):
    return COSMIC_MICROWAVE_BACKGROUND_TEMP * (1 + redshift)

def jeans_length(temperature, density, mean_molecular_weight=1):
    from ..constants import BOLTZMANN_CONSTANT, ATOMIC_MASS_UNIT
    cs = math.sqrt(BOLTZMANN_CONSTANT * temperature / (mean_molecular_weight * ATOMIC_MASS_UNIT))
    return math.sqrt(math.pi * cs**2 / (GRAVITATIONAL_CONSTANT * density))

def schwarzschild_horizon_cosmology(mass):
    return 2 * GRAVITATIONAL_CONSTANT * mass / SPEED_OF_LIGHT**2

def redshift_to_lookback_time(redshift, h0=HUBBLE_CONSTANT):
    return (2 / (3 * h0)) * (1 - 1/math.sqrt(1 + redshift))

def density_parameter(density_type, critical_density=CRITICAL_DENSITY_UNIVERSE):
    return density_type / critical_density

def sound_horizon(redshift_recombination=1100):
    return SPEED_OF_LIGHT / (3 * HUBBLE_CONSTANT * math.sqrt(redshift_recombination))

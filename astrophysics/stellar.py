import math
from constants import *

def stellar_luminosity(mass, temperature, radius):
    """
    Calculate stellar luminosity using Stefan-Boltzmann law.
    
    Args:
        mass (float): Stellar mass (kg)
        temperature (float): Surface temperature (K)
        radius (float): Stellar radius (m)
    
    Returns:
        float: Luminosity (W)
    """
    surface_area = 4 * PI * radius**2
    return STEFAN_BOLTZMANN_CONSTANT * surface_area * temperature**4


def stellar_radius(mass, temperature, luminosity):
    """
    Calculate stellar radius from luminosity and temperature.
    
    Args:
        mass (float): Stellar mass (kg)
        temperature (float): Surface temperature (K)
        luminosity (float): Luminosity (W)
    
    Returns:
        float: Stellar radius (m)
    """
    return math.sqrt(luminosity / (4 * PI * STEFAN_BOLTZMANN_CONSTANT * temperature**4))


def main_sequence_lifetime(mass):
    """
    Estimate main sequence lifetime using mass-luminosity relation.
    
    Args:
        mass (float): Stellar mass (kg)
    
    Returns:
        float: Main sequence lifetime (years)
    """
    mass_solar = mass / SOLAR_MASS
    # Approximate formula: t ~ M/L ~ M^(-2.5) for M > 0.43 M_sun
    if mass_solar > 0.43:
        lifetime_ratio = mass_solar**(-2.5)
    else:
        # Lower mass stars have longer lifetimes
        lifetime_ratio = mass_solar**(-1.0)
    
    solar_lifetime = 10e9  # years
    return lifetime_ratio * solar_lifetime


def eddington_luminosity(mass):
    """
    Calculate Eddington luminosity limit.
    
    Args:
        mass (float): Object mass (kg)
    
    Returns:
        float: Eddington luminosity (W)
    """
    return (4 * PI * GRAVITATIONAL_CONSTANT * mass * PROTON_MASS * SPEED_OF_LIGHT) / THOMSON_CROSS_SECTION


def schwarzschild_radius(mass):
    """
    Calculate Schwarzschild radius (event horizon).
    
    Args:
        mass (float): Object mass (kg)
    
    Returns:
        float: Schwarzschild radius (m)
    """
    return (2 * GRAVITATIONAL_CONSTANT * mass) / SPEED_OF_LIGHT**2


def virial_temperature(mass, radius):
    """
    Calculate virial temperature for gravitationally bound system.
    
    Args:
        mass (float): Total mass (kg)
        radius (float): System radius (m)
    
    Returns:
        float: Virial temperature (K)
    """
    return (GRAVITATIONAL_CONSTANT * mass * PROTON_MASS) / (2 * BOLTZMANN_CONSTANT * radius)


def jeans_mass(temperature, density):
    """
    Calculate Jeans mass for gravitational instability.
    
    Args:
        temperature (float): Temperature (K)
        density (float): Density (kg/m³)
    
    Returns:
        float: Jeans mass (kg)
    """
    jeans_length = math.sqrt((15 * BOLTZMANN_CONSTANT * temperature) / 
                            (4 * PI * GRAVITATIONAL_CONSTANT * PROTON_MASS * density))
    return (PI / 6) * density * jeans_length**3


def chandrasekhar_mass():
    """
    Calculate Chandrasekhar mass limit for white dwarfs.
    
    Returns:
        float: Chandrasekhar mass (kg)
    """
    # Approximate value: 1.4 solar masses
    return 1.4 * SOLAR_MASS


def stellar_surface_gravity(mass, radius):
    """
    Calculate surface gravitational acceleration.
    
    Args:
        mass (float): Stellar mass (kg)
        radius (float): Stellar radius (m)
    
    Returns:
        float: Surface gravity (m/s²)
    """
    return GRAVITATIONAL_CONSTANT * mass / radius**2


def stellar_escape_velocity(mass, radius):
    """
    Calculate escape velocity from stellar surface.
    
    Args:
        mass (float): Stellar mass (kg)
        radius (float): Stellar radius (m)
    
    Returns:
        float: Escape velocity (m/s)
    """
    return math.sqrt(2 * GRAVITATIONAL_CONSTANT * mass / radius)

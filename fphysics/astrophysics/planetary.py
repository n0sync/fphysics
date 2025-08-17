import math
from constants import *

def orbital_velocity(central_mass, orbital_radius):
    """
    Calculate circular orbital velocity.
    
    Args:
        central_mass (float): Mass of central body (kg)
        orbital_radius (float): Orbital radius (m)
    
    Returns:
        float: Orbital velocity (m/s)
    """
    return math.sqrt(GRAVITATIONAL_CONSTANT * central_mass / orbital_radius)


def escape_velocity(mass, radius):
    """
    Calculate escape velocity from planetary surface.
    
    Args:
        mass (float): Planetary mass (kg)
        radius (float): Planetary radius (m)
    
    Returns:
        float: Escape velocity (m/s)
    """
    return math.sqrt(2 * GRAVITATIONAL_CONSTANT * mass / radius)


def kepler_third_law(semi_major_axis, central_mass):
    """
    Calculate orbital period using Kepler's third law.
    
    Args:
        semi_major_axis (float): Semi-major axis (m)
        central_mass (float): Central body mass (kg)
    
    Returns:
        float: Orbital period (s)
    """
    return 2 * PI * math.sqrt(semi_major_axis**3 / (GRAVITATIONAL_CONSTANT * central_mass))


def tidal_force(primary_mass, secondary_mass, distance, radius):
    """
    Calculate tidal force gradient.
    
    Args:
        primary_mass (float): Primary body mass (kg)
        secondary_mass (float): Secondary body mass (kg)
        distance (float): Distance between centers (m)
        radius (float): Radius of affected body (m)
    
    Returns:
        float: Tidal acceleration gradient (m/s²/m)
    """
    return (2 * GRAVITATIONAL_CONSTANT * primary_mass * radius) / distance**3


def hill_sphere_radius(primary_mass, secondary_mass, orbital_distance):
    """
    Calculate Hill sphere radius (gravitational sphere of influence).
    
    Args:
        primary_mass (float): Primary body mass (kg)
        secondary_mass (float): Secondary body mass (kg)
        orbital_distance (float): Distance between bodies (m)
    
    Returns:
        float: Hill sphere radius (m)
    """
    mass_ratio = secondary_mass / (3 * primary_mass)
    return orbital_distance * (mass_ratio)**(1/3)


def roche_limit(primary_mass, primary_radius, secondary_density):
    """
    Calculate Roche limit for tidal disruption.
    
    Args:
        primary_mass (float): Primary body mass (kg)
        primary_radius (float): Primary body radius (m)
        secondary_density (float): Secondary body density (kg/m³)
    
    Returns:
        float: Roche limit distance (m)
    """
    primary_density = primary_mass / ((4/3) * PI * primary_radius**3)
    density_ratio = primary_density / secondary_density
    return 2.44 * primary_radius * (density_ratio)**(1/3)


def synodic_period(period1, period2):
    """
    Calculate synodic period between two orbiting bodies.
    
    Args:
        period1 (float): Orbital period of first body (s)
        period2 (float): Orbital period of second body (s)
    
    Returns:
        float: Synodic period (s)
    """
    if period1 == period2:
        return float('inf')  # Same period = no synodic period
    
    return abs(1 / (1/period1 - 1/period2))


def orbital_energy(mass, central_mass, semi_major_axis):
    """
    Calculate total orbital energy.
    
    Args:
        mass (float): Orbiting body mass (kg)
        central_mass (float): Central body mass (kg)
        semi_major_axis (float): Semi-major axis (m)
    
    Returns:
        float: Total orbital energy (J)
    """
    return -GRAVITATIONAL_CONSTANT * mass * central_mass / (2 * semi_major_axis)


def lagrange_points(primary_mass, secondary_mass, separation):
    """
    Calculate approximate positions of L1, L2, L3 Lagrange points.
    
    Args:
        primary_mass (float): Primary body mass (kg)
        secondary_mass (float): Secondary body mass (kg)
        separation (float): Distance between bodies (m)
    
    Returns:
        dict: Lagrange point distances from primary (m)
    """
    mass_ratio = secondary_mass / primary_mass
    mu = mass_ratio / (1 + mass_ratio)
    
    # Approximate distances from primary
    l1_approx = separation * (1 - (mu/3)**(1/3))
    l2_approx = separation * (1 + (mu/3)**(1/3))
    l3_approx = separation * (-1 + 5*mu/12)
    
    return {
        'L1': l1_approx,
        'L2': l2_approx,
        'L3': l3_approx,
        'L4': separation,  # L4 and L5 form equilateral triangles
        'L5': separation
    }


def planetary_surface_gravity(mass, radius):
    """
    Calculate surface gravitational acceleration.
    
    Args:
        mass (float): Planetary mass (kg)
        radius (float): Planetary radius (m)
    
    Returns:
        float: Surface gravity (m/s²)
    """
    return GRAVITATIONAL_CONSTANT * mass / radius**2


def angular_momentum(mass, velocity, radius):
    """
    Calculate orbital angular momentum.
    
    Args:
        mass (float): Orbiting body mass (kg)
        velocity (float): Orbital velocity (m/s)
        radius (float): Orbital radius (m)
    
    Returns:
        float: Angular momentum (kg⋅m²/s)
    """
    return mass * velocity * radius


def vis_viva_equation(central_mass, orbital_radius, semi_major_axis):
    """
    Calculate orbital velocity using vis-viva equation.
    
    Args:
        central_mass (float): Central body mass (kg)
        orbital_radius (float): Current orbital radius (m)
        semi_major_axis (float): Semi-major axis (m)
    
    Returns:
        float: Orbital velocity (m/s)
    """
    return math.sqrt(GRAVITATIONAL_CONSTANT * central_mass * (2/orbital_radius - 1/semi_major_axis))

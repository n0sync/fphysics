import math
from constants import SPEED_OF_LIGHT, GRAVITATIONAL_CONSTANT


def schwarzschild_radius(mass):
    """Calculate Schwarzschild radius"""
    return 2 * GRAVITATIONAL_CONSTANT * mass / SPEED_OF_LIGHT**2


def gravitational_time_dilation(time, mass, radius):
    """Calculate gravitational time dilation"""
    rs = schwarzschild_radius(mass)
    return time / math.sqrt(1 - rs / radius)


def escape_velocity(mass, radius):
    """Calculate escape velocity"""
    return math.sqrt(2 * GRAVITATIONAL_CONSTANT * mass / radius)


def orbital_velocity(mass, radius):
    """Calculate circular orbital velocity"""
    return math.sqrt(GRAVITATIONAL_CONSTANT * mass / radius)


def tidal_acceleration(mass, radius, height):
    """Calculate tidal acceleration difference"""
    return 2 * GRAVITATIONAL_CONSTANT * mass * height / radius**3


def gravitational_redshift(frequency, mass, radius):
    """Calculate gravitational redshift"""
    rs = schwarzschild_radius(mass)
    return frequency * math.sqrt(1 - rs / radius)


def einstein_field_tensor(mass, radius):
    """Simplified Einstein field tensor component (00)"""
    rs = schwarzschild_radius(mass)
    return -(1 - rs / radius)


def ricci_scalar(mass, radius):
    """Calculate Ricci scalar for Schwarzschild metric"""
    return 0  # Vacuum solution


def christoffel_symbol_time(mass, radius):
    """Christoffel symbol Γ^t_rr for Schwarzschild metric"""
    rs = schwarzschild_radius(mass)
    return rs / (2 * radius**2 * (1 - rs / radius))


def proper_time_factor(mass, radius):
    """Factor relating proper time to coordinate time"""
    rs = schwarzschild_radius(mass)
    return math.sqrt(1 - rs / radius)

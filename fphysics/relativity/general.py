import math
from ..constants import *

def schwarzschild_radius(mass):
    return 2 * GRAVITATIONAL_CONSTANT * mass / SPEED_OF_LIGHT**2

def gravitational_time_dilation(time, mass, radius):
    rs = schwarzschild_radius(mass)
    return time / math.sqrt(1 - rs / radius)

def escape_velocity(mass, radius):
    return math.sqrt(2 * GRAVITATIONAL_CONSTANT * mass / radius)

def orbital_velocity(mass, radius):
    return math.sqrt(GRAVITATIONAL_CONSTANT * mass / radius)

def tidal_acceleration(mass, radius, height):
    return 2 * GRAVITATIONAL_CONSTANT * mass * height / radius**3

def gravitational_redshift(frequency, mass, radius):
    rs = schwarzschild_radius(mass)
    return frequency * math.sqrt(1 - rs / radius)

def einstein_field_tensor(mass, radius):
    rs = schwarzschild_radius(mass)
    return -(1 - rs / radius)

def ricci_scalar(mass, radius):
    return 0

def christoffel_symbol_time(mass, radius):
    rs = schwarzschild_radius(mass)
    return rs / (2 * radius**2 * (1 - rs / radius))

def proper_time_factor(mass, radius):
    rs = schwarzschild_radius(mass)
    return math.sqrt(1 - rs / radius)

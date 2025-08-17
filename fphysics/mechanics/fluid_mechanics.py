import math
from constants import *

def pressure(force, area):
    return force / area

def hydrostatic_pressure(density, height, gravity=EARTH_GRAVITY):
    return density * gravity * height

def gauge_pressure(absolute_pressure, atmospheric_pressure=ATMOSPHERIC_PRESSURE):
    return absolute_pressure - atmospheric_pressure

def buoyant_force(fluid_density, displaced_volume, gravity=EARTH_GRAVITY):
    return fluid_density * gravity * displaced_volume

def flow_rate_volume(cross_sectional_area, velocity):
    return cross_sectional_area * velocity

def flow_rate_mass(density, volume_flow_rate):
    return density * volume_flow_rate

def continuity_equation_velocity(area1, velocity1, area2):
    return area1 * velocity1 / area2

def bernoulli_equation_pressure(density, velocity1, velocity2, height1, height2, gravity=EARTH_GRAVITY):
    return 0.5 * density * (velocity1**2 - velocity2**2) + density * gravity * (height1 - height2)

def reynolds_number(density, velocity, length, viscosity):
    return density * velocity * length / viscosity

def stokes_drag_force(viscosity, radius, velocity):
    return 6 * PI * viscosity * radius * velocity

def terminal_velocity_sphere(mass, radius, fluid_density, gravity=EARTH_GRAVITY, drag_coefficient=0.47):
    return math.sqrt(2 * mass * gravity / (fluid_density * PI * radius**2 * drag_coefficient))

def poiseuille_flow_rate(pressure_difference, radius, length, viscosity):
    return PI * radius**4 * pressure_difference / (8 * viscosity * length)

def venturi_velocity(pressure1, pressure2, density):
    return math.sqrt(2 * (pressure1 - pressure2) / density)

def surface_tension_force(surface_tension, length):
    return surface_tension * length

def capillary_rise(surface_tension, contact_angle, density, radius, gravity=EARTH_GRAVITY):
    return 2 * surface_tension * math.cos(contact_angle) / (density * gravity * radius)

def torricellis_law(height, gravity=EARTH_GRAVITY):
    return math.sqrt(2 * gravity * height)

def viscosity_poiseuille(flow_rate, pressure_diff, radius, length):
    return (math.pi * radius**4 * pressure_diff) / (8 * flow_rate * length)

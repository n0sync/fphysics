import math
from constants import *

def force_from_mass_acceleration(mass, acceleration):
    return mass * acceleration

def weight(mass, gravity=EARTH_GRAVITY):
    return mass * gravity

def friction_force(normal_force, coefficient_of_friction):
    return coefficient_of_friction * normal_force

def gravitational_force(mass1, mass2, distance):
    return GRAVITATIONAL_CONSTANT * mass1 * mass2 / distance**2

def centripetal_force(mass, velocity, radius):
    return mass * velocity**2 / radius

def spring_force(spring_constant, displacement):
    return -spring_constant * displacement

def drag_force(drag_coefficient, density, velocity, area):
    return 0.5 * drag_coefficient * density * velocity**2 * area

def tension_pulley_system(mass1, mass2, gravity=EARTH_GRAVITY):
    return 2 * mass1 * mass2 * gravity / (mass1 + mass2)

def acceleration_pulley_system(mass1, mass2, gravity=EARTH_GRAVITY):
    return (mass1 - mass2) * gravity / (mass1 + mass2)

def normal_force_incline(mass, angle, gravity=EARTH_GRAVITY):
    return mass * gravity * math.cos(angle)

def force_down_incline(mass, angle, gravity=EARTH_GRAVITY):
    return mass * gravity * math.sin(angle)

def banked_curve_velocity(radius, bank_angle, gravity=EARTH_GRAVITY):
    return math.sqrt(radius * gravity * math.tan(bank_angle))

def maximum_unbanked_speed(radius, friction_coeff, gravity=EARTH_GRAVITY):
    return math.sqrt(radius * gravity * friction_coeff)

def critical_speed_banked_friction(radius, bank_angle, friction_coeff, gravity=EARTH_GRAVITY):
    tan_theta = math.tan(bank_angle)
    mu = friction_coeff
    return math.sqrt(radius * gravity * (tan_theta + mu) / (1 - mu * tan_theta))

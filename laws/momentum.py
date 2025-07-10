import math
from constants import *

def momentum(mass, velocity):
    return mass * velocity

def impulse(force, time):
    return force * time

def impulse_momentum_theorem(mass, initial_velocity, final_velocity):
    return mass * (final_velocity - initial_velocity)

def conservation_of_momentum_1d(mass1, mass2, initial_velocity1, initial_velocity2, final_velocity1):
    return (mass1 * initial_velocity1 + mass2 * initial_velocity2 - mass1 * final_velocity1) / mass2

def reduced_mass(mass1, mass2):
    return (mass1 * mass2) / (mass1 + mass2)

def center_of_mass_position(masses, positions):
    total_mass = sum(masses)
    weighted_position = sum(m * p for m, p in zip(masses, positions))
    return weighted_position / total_mass

def center_of_mass_velocity(masses, velocities):
    total_mass = sum(masses)
    weighted_velocity = sum(m * v for m, v in zip(masses, velocities))
    return weighted_velocity / total_mass

def rocket_thrust(exhaust_velocity, mass_flow_rate):
    return exhaust_velocity * mass_flow_rate

def thrust_acceleration(thrust, mass, gravity=EARTH_GRAVITY):
    return thrust / mass - gravity
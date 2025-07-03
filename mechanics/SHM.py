import math
from constants import *

def simple_harmonic_position(amplitude, angular_frequency, time, phase=0):
    return amplitude * math.cos(angular_frequency * time + phase)

def simple_harmonic_velocity(amplitude, angular_frequency, time, phase=0):
    return -amplitude * angular_frequency * math.sin(angular_frequency * time + phase)

def simple_harmonic_acceleration(amplitude, angular_frequency, time, phase=0):
    return -amplitude * angular_frequency**2 * math.cos(angular_frequency * time + phase)

def angular_frequency_spring_mass(spring_constant, mass):
    return math.sqrt(spring_constant / mass)

def period_spring_mass(spring_constant, mass):
    return 2 * PI * math.sqrt(mass / spring_constant)

def angular_frequency_pendulum(length, gravity=EARTH_GRAVITY):
    return math.sqrt(gravity / length)

def period_pendulum(length, gravity=EARTH_GRAVITY):
    return 2 * PI * math.sqrt(length / gravity)

def period_physical_pendulum(moment_of_inertia, mass, distance, gravity=EARTH_GRAVITY):
    return 2 * PI * math.sqrt(moment_of_inertia / (mass * gravity * distance))

def energy_simple_harmonic(mass, angular_frequency, amplitude):
    return 0.5 * mass * angular_frequency**2 * amplitude**2

def damped_oscillation_amplitude(initial_amplitude, damping_coefficient, time):
    return initial_amplitude * math.exp(-damping_coefficient * time)

def damped_angular_frequency(natural_frequency, damping_coefficient):
    return math.sqrt(natural_frequency**2 - damping_coefficient**2)

def quality_factor(natural_frequency, damping_coefficient):
    return natural_frequency / (2 * damping_coefficient)

def resonance_amplitude(driving_amplitude, damping_coefficient, frequency_difference):
    return driving_amplitude / math.sqrt(damping_coefficient**2 + frequency_difference**2)
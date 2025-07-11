import math
from constants import *

def restoring_force(spring_constant,displacement):
    return -spring_constant * displacement

def acceleration_in_linearSHM(spring_constant,displacement,mass):
    return -(spring_constant/mass) * displacement

def velocity_in_linearSHM(angular_frequency,amplitude,displacement):
    root_term = angular_frequency * math.sqrt(amplitude**2 - displacement **2)
    velocity = angular_frequency * root_term
    return (+velocity,-velocity)

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

def max_velocity(amplitude, angular_frequency):
    return amplitude * angular_frequency

def max_acceleration(amplitude, angular_frequency):
    return amplitude * angular_frequency**2

def total_energy_shm(mass, angular_frequency, amplitude):
    return 0.5 * mass * (angular_frequency**2) * (amplitude**2)

def kinetic_energy_shm(mass, angular_frequency, displacement, amplitude):
    velocity = angular_frequency * math.sqrt(amplitude**2 - displacement**2)
    return 0.5 * mass * velocity**2

def potential_energy_shm(mass, angular_frequency, displacement):
    return 0.5 * mass * angular_frequency**2 * displacement**2

def phase_difference_displacement_velocity():
    return PI / 2

def displacement_from_energy(total_energy, mass, angular_frequency, kinetic_energy):
    pe = total_energy - kinetic_energy
    return math.sqrt((2 * pe) / (mass * angular_frequency**2))

def damped_oscillator_position(amplitude, damping_coefficient, angular_frequency, time):
    return amplitude * math.exp(-damping_coefficient * time) * math.cos(angular_frequency * time)

def shm_position_sine(amplitude, angular_frequency, time, phase=0):
    return amplitude * math.sin(angular_frequency * time + phase)

def shm_differential_equation(angular_frequency, displacement):
    return -angular_frequency**2 * displacement

def shm_position_combined(amplitude_cos, amplitude_sin, angular_frequency, time):
    return amplitude_cos * math.cos(angular_frequency * time) + amplitude_sin * math.sin(angular_frequency * time)

def velocity_displacement_shm(angular_frequency, amplitude, displacement):
    return angular_frequency * math.sqrt(amplitude**2 - displacement**2)

def acceleration_displacement_shm(angular_frequency, displacement):
    return -angular_frequency**2 * displacement

def displacement_from_velocity(velocity, angular_frequency, amplitude):
    return math.sqrt(amplitude**2 - (velocity / angular_frequency)**2)

def number_of_oscillations(time, period):
    return time / period
    
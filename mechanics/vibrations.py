import math
from constants import *

def natural_frequencies(num_modes, material_properties, geometry):
    E, density = material_properties
    L = geometry['length']
    
    freqs = []
    for n in range(1, num_modes + 1):
        freq = (n * math.pi / L)**2 * math.sqrt(E / density)
        freqs.append(freq)
    return freqs

def mode_shapes(num_modes, geometry, position):
    L = geometry['length']
    shapes = []
    for n in range(1, num_modes + 1):
        shape = math.sin(n * math.pi * position / L)
        shapes.append(shape)
    return shapes

def damping_ratio(critical_damping, actual_damping):
    return actual_damping / critical_damping

def quality_factor_from_damping(damping_ratio):
    return 1 / (2 * damping_ratio)

def critical_damping_coefficient(mass, stiffness):
    return 2 * math.sqrt(mass * stiffness)

def system_response_natural(frequency, initial_conditions, time):
    A, phi = initial_conditions
    return A * math.sin(frequency * time + phi)

def system_response_damped(frequency, damping_ratio, initial_conditions, time):
    A, phi = initial_conditions
    damped_freq = frequency * math.sqrt(1 - damping_ratio**2)
    return A * math.exp(-damping_ratio * frequency * time) * math.sin(damped_freq * time + phi)

def response_under_forcing(forcing_frequency, natural_frequency, damping_ratio, force_amplitude, mass, time):
    omega_diff = forcing_frequency - natural_frequency
    denom = (natural_frequency**2 - forcing_frequency**2)**2 + (2 * damping_ratio * natural_frequency * forcing_frequency)**2
    response = force_amplitude * (natural_frequency / mass) / math.sqrt(denom)
    return response * math.sin(forcing_frequency * time)

def transient_response(natural_frequency, damping_ratio, initial_conditions, time):
    return system_response_damped(natural_frequency, damping_ratio, initial_conditions, time)

def steady_state_response(amplitude_ratio, forcing_frequency, time):
    return amplitude_ratio * math.sin(forcing_frequency * time)

def transient_steady_state_combined(natural_frequency, damping_ratio, initial_conditions, forcing_amplitude, forcing_frequency, time):
    transient = transient_response(natural_frequency, damping_ratio, initial_conditions, time)
    steady = steady_state_response(forcing_amplitude, forcing_frequency, time)
    return transient + steady


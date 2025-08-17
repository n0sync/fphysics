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

def beam_vibration_frequency(n, length, elastic_modulus, second_moment, density, area):
    return (n * math.pi / length)**2 * math.sqrt(elastic_modulus * second_moment / (density * area))

def torsional_vibration_frequency(shear_modulus, polar_moment, length, density):
    return math.sqrt(shear_modulus * polar_moment / (density * length**2))

def string_vibration_frequency(n, length, tension, linear_density):
    return (n / (2 * length)) * math.sqrt(tension / linear_density)

def membrane_vibration_frequency(m, n, length_x, length_y, tension, surface_density):
    return (math.pi / 2) * math.sqrt(tension / surface_density) * math.sqrt((m / length_x)**2 + (n / length_y)**2)

def plate_vibration_frequency(m, n, length_x, length_y, thickness, elastic_modulus, density, poissons_ratio):
    D = elastic_modulus * thickness**3 / (12 * (1 - poissons_ratio**2))
    return (math.pi**2 / 2) * math.sqrt(D / (density * thickness)) * ((m / length_x)**2 + (n / length_y)**2)

def rayleigh_quotient(mass_matrix, stiffness_matrix, displacement_vector):
    numerator = sum(k * d**2 for k, d in zip(stiffness_matrix, displacement_vector))
    denominator = sum(m * d**2 for m, d in zip(mass_matrix, displacement_vector))
    return numerator / denominator

def modal_mass(mode_shape, mass_matrix):
    return sum(m * phi**2 for m, phi in zip(mass_matrix, mode_shape))

def modal_stiffness(mode_shape, stiffness_matrix):
    return sum(k * phi**2 for k, phi in zip(stiffness_matrix, mode_shape))

def orthogonality_condition(mode_i, mode_j, mass_matrix):
    return sum(m * phi_i * phi_j for m, phi_i, phi_j in zip(mass_matrix, mode_i, mode_j))

def modal_participation_factor(mode_shape, mass_matrix, excitation_vector):
    numerator = sum(m * phi * f for m, phi, f in zip(mass_matrix, mode_shape, excitation_vector))
    denominator = sum(m * phi**2 for m, phi in zip(mass_matrix, mode_shape))
    return numerator / denominator

def effective_modal_mass(participation_factor, modal_mass):
    return participation_factor**2 * modal_mass

def frequency_response_function(omega, natural_frequency, damping_ratio):
    return 1 / ((natural_frequency**2 - omega**2) + 1j * 2 * damping_ratio * natural_frequency * omega)

def random_vibration_rms(power_spectral_density, frequency_bandwidth):
    return math.sqrt(power_spectral_density * frequency_bandwidth)

def fatigue_damage_palmgren_miner(stress_cycles, stress_limits):
    return sum(n / N for n, N in zip(stress_cycles, stress_limits))

def shock_response_spectrum(acceleration_time_history, natural_frequency, damping_ratio):
    max_response = 0
    for a in acceleration_time_history:
        response = a / (natural_frequency**2 * (1 - damping_ratio**2))
        max_response = max(max_response, abs(response))
    return max_response

def isolation_transmissibility(frequency_ratio, damping_ratio):
    return math.sqrt((1 + (2 * damping_ratio * frequency_ratio)**2) / ((1 - frequency_ratio**2)**2 + (2 * damping_ratio * frequency_ratio)**2))

def vibration_absorber_tuning(primary_frequency, absorber_mass, primary_mass):
    mass_ratio = absorber_mass / primary_mass
    return primary_frequency / math.sqrt(1 + mass_ratio)


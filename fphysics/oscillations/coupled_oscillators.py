import math
from constants import *

def coupled_pendulum_normal_modes(length, coupling_constant, gravity=EARTH_GRAVITY):
    omega0 = math.sqrt(gravity / length)
    omega1 = omega0 * math.sqrt(1 - coupling_constant)
    omega2 = omega0 * math.sqrt(1 + coupling_constant)
    return omega1, omega2

def beat_period_coupled_oscillators(frequency1, frequency2):
    return 2 / abs(frequency1 - frequency2)

def normal_mode_frequency(mass, spring_constant, coupling_constant):
    omega0 = math.sqrt(spring_constant / mass)
    omega_plus = omega0 * math.sqrt(1 + 2 * coupling_constant)
    omega_minus = omega0
    return omega_minus, omega_plus

def energy_transfer_time(frequency1, frequency2):
    return PI / abs(frequency1 - frequency2)

def coupling_strength(coupled_frequency, uncoupled_frequency):
    return (coupled_frequency**2 - uncoupled_frequency**2) / uncoupled_frequency**2

def symmetric_mode_amplitude(initial_amplitude1, initial_amplitude2):
    return (initial_amplitude1 + initial_amplitude2) / math.sqrt(2)

def antisymmetric_mode_amplitude(initial_amplitude1, initial_amplitude2):
    return (initial_amplitude1 - initial_amplitude2) / math.sqrt(2)

def coupled_oscillator_displacement(amplitude, frequency, phase, time):
    return amplitude * math.cos(frequency * time + phase)

def normal_coordinate_transformation(q1, q2):
    Q1 = (q1 + q2) / math.sqrt(2)
    Q2 = (q1 - q2) / math.sqrt(2)
    return Q1, Q2

def spring_coupled_masses_frequency(mass1, mass2, spring1, spring2, coupling_spring):
    reduced_mass = (mass1 * mass2) / (mass1 + mass2)
    effective_spring = spring1 + spring2 + 2 * coupling_spring
    return math.sqrt(effective_spring / reduced_mass)

def weakly_coupled_oscillators_frequency(frequency0, coupling_matrix_element):
    return frequency0 + coupling_matrix_element / (2 * frequency0)

def mode_splitting(coupling_strength, detuning):
    return math.sqrt(coupling_strength**2 + detuning**2)

def rabi_frequency(coupling_strength):
    return 2 * coupling_strength

def avoided_crossing_gap(coupling_strength):
    return 2 * coupling_strength

def coherent_energy_transfer_efficiency(coupling_strength, detuning, time):
    rabi_freq = math.sqrt(coupling_strength**2 + detuning**2)
    return (coupling_strength / rabi_freq)**2 * math.sin(rabi_freq * time)**2

def parametric_oscillator_frequency(driving_frequency):
    return driving_frequency / 2

def subharmonic_instability_threshold(damping_coefficient, parametric_amplitude):
    return parametric_amplitude > 2 * damping_coefficient

def mathieu_equation_stability(a_parameter, q_parameter):
    return a_parameter, q_parameter

def floquet_multiplier(characteristic_exponent, period):
    return math.exp(characteristic_exponent * period)

def arnold_tongue_width(coupling_strength, frequency_ratio):
    return 2 * coupling_strength / frequency_ratio

def synchronization_range(coupling_strength, natural_frequency):
    return 2 * coupling_strength / natural_frequency

def phase_locking_range(coupling_strength, quality_factor):
    return 2 * coupling_strength / quality_factor

def mutual_synchronization_frequency(frequency1, frequency2, coupling12, coupling21):
    return (frequency1 + frequency2 + coupling12 + coupling21) / 2

def entrainment_frequency(driving_frequency, coupling_strength, detuning):
    return driving_frequency + coupling_strength * detuning / math.sqrt(detuning**2 + coupling_strength**2)

def chimera_state_parameter(coupling_strength, phase_lag):
    return coupling_strength * math.cos(phase_lag)

def kuramoto_order_parameter(phases):
    real_part = sum(math.cos(phase) for phase in phases) / len(phases)
    imag_part = sum(math.sin(phase) for phase in phases) / len(phases)
    return math.sqrt(real_part**2 + imag_part**2)

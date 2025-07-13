import math
from constants import *

def canonical_partition_function(energies, temperature):
    beta = 1 / (BOLTZMANN_CONSTANT * temperature)
    return sum(math.exp(-beta * energy) for energy in energies)

def grand_canonical_partition_function(energies, chemical_potential, temperature):
    beta = 1 / (BOLTZMANN_CONSTANT * temperature)
    return sum(math.exp(-beta * (energy - chemical_potential)) for energy in energies)

def microcanonical_partition_function(number_of_microstates):
    return number_of_microstates

def classical_partition_function_translation(mass, temperature, volume):
    thermal_wavelength = PLANCK_CONSTANT / math.sqrt(2 * PI * mass * BOLTZMANN_CONSTANT * temperature)
    return volume / thermal_wavelength**3

def quantum_harmonic_oscillator_partition(frequency, temperature):
    beta = 1 / (BOLTZMANN_CONSTANT * temperature)
    x = beta * PLANCK_CONSTANT * frequency
    return 1 / (2 * math.sinh(x / 2))

def classical_harmonic_oscillator_partition(frequency, temperature):
    return BOLTZMANN_CONSTANT * temperature / (PLANCK_CONSTANT * frequency)

def rotational_partition_function_linear(moment_of_inertia, temperature):
    return BOLTZMANN_CONSTANT * temperature / (PLANCK_CONSTANT**2 / (8 * PI**2 * moment_of_inertia))

def rotational_partition_function_nonlinear(moments_of_inertia, temperature, symmetry_number):
    product = math.prod(moments_of_inertia)
    return (math.sqrt(PI) / symmetry_number) * (8 * PI**2 * BOLTZMANN_CONSTANT * temperature / PLANCK_CONSTANT**2)**(3/2) * math.sqrt(product)

def vibrational_partition_function(frequency, temperature):
    x = PLANCK_CONSTANT * frequency / (BOLTZMANN_CONSTANT * temperature)
    return 1 / (1 - math.exp(-x))

def electronic_partition_function(degeneracy, excitation_energy, temperature):
    return degeneracy * math.exp(-excitation_energy / (BOLTZMANN_CONSTANT * temperature))

def ideal_gas_partition_function(mass, temperature, volume, number_of_particles):
    single_particle_z = classical_partition_function_translation(mass, temperature, volume)
    return single_particle_z**number_of_particles / math.factorial(number_of_particles)

def diatomic_molecule_partition_function(mass, moment_of_inertia, vibrational_frequency, temperature):
    z_trans = classical_partition_function_translation(mass, temperature, 1)  # per unit volume
    z_rot = rotational_partition_function_linear(moment_of_inertia, temperature)
    z_vib = vibrational_partition_function(vibrational_frequency, temperature)
    return z_trans * z_rot * z_vib

def polyatomic_molecule_partition_function(mass, moments_of_inertia, vibrational_frequencies, temperature, symmetry_number):
    z_trans = classical_partition_function_translation(mass, temperature, 1)
    z_rot = rotational_partition_function_nonlinear(moments_of_inertia, temperature, symmetry_number)
    z_vib = math.prod(vibrational_partition_function(freq, temperature) for freq in vibrational_frequencies)
    return z_trans * z_rot * z_vib

def einstein_solid_partition_function(frequency, temperature, number_of_oscillators):
    single_oscillator_z = quantum_harmonic_oscillator_partition(frequency, temperature)
    return single_oscillator_z**number_of_oscillators

def debye_solid_partition_function(debye_frequency, temperature, number_of_modes):
    integral_result = 3 * (BOLTZMANN_CONSTANT * temperature / (PLANCK_CONSTANT * debye_frequency))**3
    return math.exp(-integral_result)

def two_level_system_partition(energy_gap, temperature):
    beta = 1 / (BOLTZMANN_CONSTANT * temperature)
    return 1 + math.exp(-beta * energy_gap)

def spin_system_partition_function(magnetic_field, magnetic_moment, temperature, spin):
    beta = 1 / (BOLTZMANN_CONSTANT * temperature)
    x = beta * magnetic_moment * magnetic_field
    if spin == 0.5:
        return 2 * math.cosh(x)
    else:
        return math.sinh((2 * spin + 1) * x / 2) / math.sinh(x / 2)

def ising_model_partition_1d(number_of_spins, coupling_constant, temperature):
    beta = 1 / (BOLTZMANN_CONSTANT * temperature)
    k = beta * coupling_constant
    eigenvalue_plus = math.exp(k) + math.exp(-k)
    return eigenvalue_plus**number_of_spins

def lattice_gas_partition_function(number_of_sites, number_of_particles, interaction_energy, temperature):
    beta = 1 / (BOLTZMANN_CONSTANT * temperature)
    combinatorial_factor = math.comb(number_of_sites, number_of_particles)
    interaction_factor = math.exp(-beta * interaction_energy * number_of_particles * (number_of_particles - 1) / 2)
    return combinatorial_factor * interaction_factor

def classical_ideal_gas_fugacity(chemical_potential, mass, temperature):
    thermal_wavelength = PLANCK_CONSTANT / math.sqrt(2 * PI * mass * BOLTZMANN_CONSTANT * temperature)
    return math.exp(chemical_potential / (BOLTZMANN_CONSTANT * temperature)) / thermal_wavelength**3

def quantum_ideal_gas_fugacity(chemical_potential, temperature):
    return math.exp(chemical_potential / (BOLTZMANN_CONSTANT * temperature))

def virial_expansion_second_coefficient(temperature, interaction_potential):
    beta = 1 / (BOLTZMANN_CONSTANT * temperature)
    return -0.5 * (math.exp(-beta * interaction_potential) - 1)

def cluster_expansion_coefficient(order, temperature, interaction_energies):
    beta = 1 / (BOLTZMANN_CONSTANT * temperature)
    return sum(math.exp(-beta * energy) for energy in interaction_energies) / order

def configurational_partition_function(positions, interaction_energies, temperature):
    beta = 1 / (BOLTZMANN_CONSTANT * temperature)
    total_energy = sum(interaction_energies)
    return math.exp(-beta * total_energy)

def classical_system_phase_space_volume(coordinates, momenta):
    return math.prod(coordinates) * math.prod(momenta) / PLANCK_CONSTANT**(len(coordinates))

def quantum_partition_function_path_integral(action, temperature, time_slices):
    beta = 1 / (BOLTZMANN_CONSTANT * temperature)
    return math.exp(-beta * action / time_slices)

def anharmonic_oscillator_partition(frequency, anharmonicity, temperature):
    x = PLANCK_CONSTANT * frequency / (BOLTZMANN_CONSTANT * temperature)
    harmonic_part = 1 / (1 - math.exp(-x))
    anharmonic_correction = 1 + anharmonicity * x**2 / 24
    return harmonic_part * anharmonic_correction

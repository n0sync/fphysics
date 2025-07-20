import numpy as np
from constants import *

def fermi_dirac_distribution(E, mu, T):
    beta = 1 / (BOLTZMANN_CONSTANT * T)
    return 1 / (np.exp(beta * (E - mu)) + 1)

def bose_einstein_distribution(E, mu, T):
    beta = 1 / (BOLTZMANN_CONSTANT * T)
    return 1 / (np.exp(beta * (E - mu)) - 1)

def quantum_partition_function(energies, T):
    beta = 1 / (BOLTZMANN_CONSTANT * T)
    return np.sum(np.exp(-beta * energies))

def quantum_grand_partition_function(energies, mu, T):
    beta = 1 / (BOLTZMANN_CONSTANT * T)
    return np.sum(np.exp(-beta * (energies - mu)))

def fermi_energy(n, m=ELECTRON_MASS):
    return (PLANCK_CONSTANT**2 / (2 * m)) * (3 * PI**2 * n)**(2/3)

def debye_temperature(omega_D):
    return PLANCK_CONSTANT * omega_D / BOLTZMANN_CONSTANT

def einstein_temperature(omega):
    return PLANCK_CONSTANT * omega / BOLTZMANN_CONSTANT

def density_of_states_3d(E, m, V):
    return (V / (2 * PI**2)) * (2 * m / PLANCK_CONSTANT**2)**(3/2) * np.sqrt(E)

def density_of_states_2d(m, V):
    return (V * m) / (PI * PLANCK_CONSTANT**2)

def density_of_states_1d(E, m, L):
    return (L / PI) * np.sqrt(2 * m / PLANCK_CONSTANT**2) / np.sqrt(E)

def chemical_potential(n, T, m=ELECTRON_MASS):
    return BOLTZMANN_CONSTANT * T * np.log(n * (2 * PI * PLANCK_CONSTANT**2 / (m * BOLTZMANN_CONSTANT * T))**(3/2))

def quantum_ideal_gas_pressure(n, T, m=ELECTRON_MASS):
    return (2/3) * n * BOLTZMANN_CONSTANT * T

def quantum_ideal_gas_energy(n, T, m=ELECTRON_MASS):
    return (3/2) * n * BOLTZMANN_CONSTANT * T

def pauli_exclusion_principle(n_max):
    return n_max == 1

def bose_einstein_condensation_temperature(n, m):
    return (2 * PI * PLANCK_CONSTANT**2 / (m * BOLTZMANN_CONSTANT)) * (n / 2.612)**(2/3)

def photon_energy_density(T):
    return (8 * PI**5 * BOLTZMANN_CONSTANT**4 * T**4) / (15 * PLANCK_CONSTANT**3 * SPEED_OF_LIGHT**3)

def planck_distribution(omega, T):
    return (PLANCK_CONSTANT * omega) / (np.exp(PLANCK_CONSTANT * omega / (BOLTZMANN_CONSTANT * T)) - 1)

def quantum_heat_capacity(T, omega):
    x = PLANCK_CONSTANT * omega / (BOLTZMANN_CONSTANT * T)
    return BOLTZMANN_CONSTANT * x**2 * np.exp(x) / (np.exp(x) - 1)**2

def debye_heat_capacity(T, theta_D):
    x = theta_D / T
    return 9 * BOLTZMANN_CONSTANT * (T / theta_D)**3 * np.exp(x) / (np.exp(x) - 1)**2

def einstein_heat_capacity(T, theta_E):
    x = theta_E / T
    return BOLTZMANN_CONSTANT * x**2 * np.exp(x) / (np.exp(x) - 1)**2

def quantum_gas_fugacity(mu, T):
    return np.exp(mu / (BOLTZMANN_CONSTANT * T))

def quantum_virial_expansion(z, lambda_thermal):
    return z - z**2 / (2**(3/2)) + z**3 / (3**(3/2))

def thermal_de_broglie_wavelength(m, T):
    return PLANCK_CONSTANT / np.sqrt(2 * PI * m * BOLTZMANN_CONSTANT * T)

def quantum_degeneracy_parameter(n, lambda_thermal):
    return n * lambda_thermal**3

def fermi_sphere_radius(n):
    return (3 * PI**2 * n)**(1/3)

def quantum_pressure_degenerate(n, m=ELECTRON_MASS):
    return (PLANCK_CONSTANT**2 / (5 * m)) * (3 * PI**2)**(2/3) * n**(5/3)

def quantum_energy_degenerate(n, m=ELECTRON_MASS):
    return (3 * PLANCK_CONSTANT**2 / (10 * m)) * (3 * PI**2)**(2/3) * n**(5/3)

def landau_quantization(n, B, m=ELECTRON_MASS):
    return (n + 0.5) * ELEMENTARY_CHARGE * B / m

def quantum_hall_conductivity(n):
    return n * ELEMENTARY_CHARGE**2 / PLANCK_CONSTANT

def quantum_oscillator_partition_function(omega, T):
    beta = 1 / (BOLTZMANN_CONSTANT * T)
    return np.exp(-beta * PLANCK_CONSTANT * omega / 2) / (1 - np.exp(-beta * PLANCK_CONSTANT * omega))

def quantum_rotor_partition_function(B, T):
    beta = 1 / (BOLTZMANN_CONSTANT * T)
    return BOLTZMANN_CONSTANT * T / (2 * B)

def quantum_entropy(energies, T):
    beta = 1 / (BOLTZMANN_CONSTANT * T)
    Z = quantum_partition_function(energies, T)
    return BOLTZMANN_CONSTANT * (np.log(Z) + beta * np.sum(energies * np.exp(-beta * energies)) / Z)

def quantum_free_energy(energies, T):
    Z = quantum_partition_function(energies, T)
    return -BOLTZMANN_CONSTANT * T * np.log(Z)

def quantum_internal_energy(energies, T):
    beta = 1 / (BOLTZMANN_CONSTANT * T)
    Z = quantum_partition_function(energies, T)
    return np.sum(energies * np.exp(-beta * energies)) / Z

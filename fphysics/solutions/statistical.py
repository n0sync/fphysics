import numpy as np


def fermi_dirac_occupation(energy, chemical_potential, temperature):
    k_B = 1.381e-23
    beta = 1 / (k_B * temperature)
    return 1 / (np.exp(beta * (energy - chemical_potential)) + 1)


def fermi_energy(electron_density):
    h = 6.626e-34
    m_e = 9.109e-31
    return (h**2 / (2 * m_e)) * (3 * np.pi**2 * electron_density)**(2/3)


def fermi_average_energy(energy_levels, degeneracies, chemical_potential, temperature):
    k_B = 1.381e-23
    total_energy = 0
    total_particles = 0
    for E, g in zip(energy_levels, degeneracies):
        f = fermi_dirac_occupation(E, chemical_potential, temperature)
        total_energy += g * f * E
        total_particles += g * f
    return total_energy / total_particles if total_particles > 0 else 0


def electronic_heat_capacity(energy_levels, degeneracies, chemical_potential, temperature):
    k_B = 1.381e-23
    beta = 1 / (k_B * temperature)
    heat_capacity = 0
    for E, g in zip(energy_levels, degeneracies):
        f = fermi_dirac_occupation(E, chemical_potential, temperature)
        derivative = beta**2 * (E - chemical_potential)**2 * f * (1 - f)
        heat_capacity += g * derivative
    return k_B * heat_capacity


def bose_einstein_occupation(energy, chemical_potential, temperature):
    k_B = 1.381e-23
    beta = 1 / (k_B * temperature)
    return 1 / (np.exp(beta * (energy - chemical_potential)) - 1)


def planck_distribution(frequency, temperature):
    h = 6.626e-34
    k_B = 1.381e-23
    energy = h * frequency
    beta = 1 / (k_B * temperature)
    return 1 / (np.exp(beta * energy) - 1)


def bose_einstein_condensation_temperature(particle_density):
    h = 6.626e-34
    m = 9.109e-31
    k_B = 1.381e-23
    return (h**2 / (2 * np.pi * m * k_B)) * (particle_density / 2.612)**(2/3)


def bose_average_occupation(energy_levels, degeneracies, chemical_potential, temperature):
    total_occupation = 0
    for E, g in zip(energy_levels, degeneracies):
        n = bose_einstein_occupation(E, chemical_potential, temperature)
        total_occupation += g * n
    return total_occupation


def maxwell_boltzmann_velocity(v, mass, temperature):
    k_B = 1.381e-23
    beta = mass / (2 * k_B * temperature)
    normalization = (beta / np.pi)**(3/2)
    return 4 * np.pi * normalization * v**2 * np.exp(-beta * v**2)


def maxwell_boltzmann_energy(energy, temperature):
    k_B = 1.381e-23
    beta = 1 / (k_B * temperature)
    return 2 * np.sqrt(energy / np.pi) * beta**(3/2) * np.exp(-beta * energy)


def most_probable_speed(mass, temperature):
    k_B = 1.381e-23
    return np.sqrt(2 * k_B * temperature / mass)


def average_kinetic_energy(temperature):
    k_B = 1.381e-23
    return 3/2 * k_B * temperature


def partition_function(energy_levels, degeneracies, temperature):
    k_B = 1.381e-23
    beta = 1 / (k_B * temperature)
    Z = 0
    for E, g in zip(energy_levels, degeneracies):
        Z += g * np.exp(-beta * E)
    return Z


def helmholtz_free_energy(energy_levels, degeneracies, temperature):
    k_B = 1.381e-23
    Z = partition_function(energy_levels, degeneracies, temperature)
    return -k_B * temperature * np.log(Z)


def internal_energy(energy_levels, degeneracies, temperature):
    k_B = 1.381e-23
    beta = 1 / (k_B * temperature)
    Z = partition_function(energy_levels, degeneracies, temperature)
    U = 0
    for E, g in zip(energy_levels, degeneracies):
        U += g * E * np.exp(-beta * E)
    return U / Z


def entropy(energy_levels, degeneracies, temperature):
    U = internal_energy(energy_levels, degeneracies, temperature)
    F = helmholtz_free_energy(energy_levels, degeneracies, temperature)
    return (U - F) / temperature


def heat_capacity(energy_levels, degeneracies, temperature):
    k_B = 1.381e-23
    beta = 1 / (k_B * temperature)
    Z = partition_function(energy_levels, degeneracies, temperature)
    avg_energy = internal_energy(energy_levels, degeneracies, temperature)
    avg_energy_squared = 0
    for E, g in zip(energy_levels, degeneracies):
        avg_energy_squared += g * E**2 * np.exp(-beta * E)
    avg_energy_squared /= Z
    return k_B * beta**2 * (avg_energy_squared - avg_energy**2)


def thermal_de_broglie_wavelength(mass, temperature):
    h = 6.626e-34
    k_B = 1.381e-23
    return h / np.sqrt(2 * np.pi * mass * k_B * temperature)


def quantum_concentration(mass, temperature):
    lambda_th = thermal_de_broglie_wavelength(mass, temperature)
    return 1 / lambda_th**3


def degeneracy_parameter(density, mass, temperature):
    n_q = quantum_concentration(mass, temperature)
    return density / n_q


def pressure_virial_expansion(density, mass, temperature, particle_type):
    k_B = 1.381e-23
    lambda_th = thermal_de_broglie_wavelength(mass, temperature)
    pressure = density * k_B * temperature
    
    if particle_type == 'fermion':
        correction = -1/(2**(5/2)) * (density * lambda_th**3)
    elif particle_type == 'boson':
        correction = 1/(2**(5/2)) * (density * lambda_th**3)
    else:
        correction = 0
        
    return pressure * (1 + correction)


def debye_function(x, n):
    def integrand(t):
        return t**n / (np.exp(t) - 1)
    
    integral = 0
    dt = x / 1000
    for i in range(1000):
        t = i * dt
        if t > 0:
            integral += integrand(t) * dt
    return (n / x**n) * integral


def debye_heat_capacity(temperature, debye_temperature, num_atoms):
    k_B = 1.381e-23
    x = debye_temperature / temperature
    debye_3 = debye_function(x, 3)
    return 9 * num_atoms * k_B * (temperature / debye_temperature)**3 * debye_3


def debye_internal_energy(temperature, debye_temperature, num_atoms):
    k_B = 1.381e-23
    x = debye_temperature / temperature
    debye_3 = debye_function(x, 3)
    return 9 * num_atoms * k_B * temperature * debye_3

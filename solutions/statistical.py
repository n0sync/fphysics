import numpy as np

class FermiDiracDistribution:
    def __init__(self, chemical_potential, temperature):
        self.mu = chemical_potential
        self.T = temperature
        self.k_B = 1.381e-23

    def occupation_probability(self, energy):
        beta = 1 / (self.k_B * self.T)
        return 1 / (np.exp(beta * (energy - self.mu)) + 1)

    def fermi_energy(self, electron_density):
        h = 6.626e-34
        m_e = 9.109e-31
        return (h**2 / (2 * m_e)) * (3 * np.pi**2 * electron_density)**(2/3)

    def average_energy(self, energy_levels, degeneracies):
        total_energy = 0
        total_particles = 0
        for E, g in zip(energy_levels, degeneracies):
            f = self.occupation_probability(E)
            total_energy += g * f * E
            total_particles += g * f
        return total_energy / total_particles if total_particles > 0 else 0

    def electronic_heat_capacity(self, energy_levels, degeneracies):
        beta = 1 / (self.k_B * self.T)
        heat_capacity = 0
        for E, g in zip(energy_levels, degeneracies):
            f = self.occupation_probability(E)
            derivative = beta**2 * (E - self.mu)**2 * f * (1 - f)
            heat_capacity += g * derivative
        return self.k_B * heat_capacity

class BoseEinsteinDistribution:
    def __init__(self, chemical_potential, temperature):
        self.mu = chemical_potential
        self.T = temperature
        self.k_B = 1.381e-23

    def occupation_number(self, energy):
        beta = 1 / (self.k_B * self.T)
        return 1 / (np.exp(beta * (energy - self.mu)) - 1)

    def planck_distribution(self, frequency):
        h = 6.626e-34
        energy = h * frequency
        beta = 1 / (self.k_B * self.T)
        return 1 / (np.exp(beta * energy) - 1)

    def bose_einstein_condensation_temperature(self, particle_density):
        h = 6.626e-34
        m = 9.109e-31
        return (h**2 / (2 * np.pi * m * self.k_B)) * (particle_density / 2.612)**(2/3)

    def average_occupation(self, energy_levels, degeneracies):
        total_occupation = 0
        for E, g in zip(energy_levels, degeneracies):
            n = self.occupation_number(E)
            total_occupation += g * n
        return total_occupation

class MaxwellBoltzmannDistribution:
    def __init__(self, temperature):
        self.T = temperature
        self.k_B = 1.381e-23

    def velocity_distribution(self, v, mass):
        beta = mass / (2 * self.k_B * self.T)
        normalization = (beta / np.pi)**(3/2)
        return 4 * np.pi * normalization * v**2 * np.exp(-beta * v**2)

    def energy_distribution(self, energy):
        beta = 1 / (self.k_B * self.T)
        return 2 * np.sqrt(energy / np.pi) * beta**(3/2) * np.exp(-beta * energy)

    def most_probable_speed(self, mass):
        return np.sqrt(2 * self.k_B * self.T / mass)

    def average_kinetic_energy(self):
        return 3/2 * self.k_B * self.T

class QuantumEnsemble:
    def __init__(self, hamiltonian, temperature):
        self.hamiltonian = hamiltonian
        self.T = temperature
        self.k_B = 1.381e-23
        self.beta = 1 / (self.k_B * self.T)

    def partition_function(self, energy_levels, degeneracies):
        Z = 0
        for E, g in zip(energy_levels, degeneracies):
            Z += g * np.exp(-self.beta * E)
        return Z

    def helmholtz_free_energy(self, energy_levels, degeneracies):
        Z = self.partition_function(energy_levels, degeneracies)
        return -self.k_B * self.T * np.log(Z)

    def internal_energy(self, energy_levels, degeneracies):
        Z = self.partition_function(energy_levels, degeneracies)
        U = 0
        for E, g in zip(energy_levels, degeneracies):
            U += g * E * np.exp(-self.beta * E)
        return U / Z

    def entropy(self, energy_levels, degeneracies):
        Z = self.partition_function(energy_levels, degeneracies)
        U = self.internal_energy(energy_levels, degeneracies)
        F = self.helmholtz_free_energy(energy_levels, degeneracies)
        return (U - F) / self.T

    def heat_capacity(self, energy_levels, degeneracies):
        Z = self.partition_function(energy_levels, degeneracies)
        avg_energy = self.internal_energy(energy_levels, degeneracies)
        avg_energy_squared = 0
        for E, g in zip(energy_levels, degeneracies):
            avg_energy_squared += g * E**2 * np.exp(-self.beta * E)
        avg_energy_squared /= Z
        return self.k_B * self.beta**2 * (avg_energy_squared - avg_energy**2)

class QuantumGas:
    def __init__(self, particle_type, density, temperature):
        self.particle_type = particle_type
        self.density = density
        self.temperature = temperature
        self.k_B = 1.381e-23
        self.h = 6.626e-34

    def thermal_de_broglie_wavelength(self, mass):
        return self.h / np.sqrt(2 * np.pi * mass * self.k_B * self.temperature)

    def quantum_concentration(self, mass):
        lambda_th = self.thermal_de_broglie_wavelength(mass)
        return 1 / lambda_th**3

    def degeneracy_parameter(self, mass):
        n_q = self.quantum_concentration(mass)
        return self.density / n_q

    def pressure_virial_expansion(self, mass, terms=3):
        lambda_th = self.thermal_de_broglie_wavelength(mass)
        pressure = self.density * self.k_B * self.temperature
        
        if self.particle_type == 'fermion':
            correction = -1/(2**(5/2)) * (self.density * lambda_th**3)
        elif self.particle_type == 'boson':
            correction = 1/(2**(5/2)) * (self.density * lambda_th**3)
        else:
            correction = 0
            
        return pressure * (1 + correction)

class DebyeModel:
    def __init__(self, debye_temperature, num_atoms):
        self.theta_D = debye_temperature
        self.N = num_atoms
        self.k_B = 1.381e-23

    def debye_function(self, x, n):
        def integrand(t):
            return t**n / (np.exp(t) - 1)
        
        integral = 0
        dt = x / 1000
        for i in range(1000):
            t = i * dt
            if t > 0:
                integral += integrand(t) * dt
        return (n / x**n) * integral

    def heat_capacity(self, temperature):
        x = self.theta_D / temperature
        debye_3 = self.debye_function(x, 3)
        return 9 * self.N * self.k_B * (temperature / self.theta_D)**3 * debye_3

    def internal_energy(self, temperature):
        x = self.theta_D / temperature
        debye_3 = self.debye_function(x, 3)
        return 9 * self.N * self.k_B * temperature * debye_3

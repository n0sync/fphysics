import math
from constants import *

def bose_einstein_distribution(energy, chemical_potential, temperature):
    exponent = (energy - chemical_potential) / (BOLTZMANN_CONSTANT * temperature)
    return 1 / (math.exp(exponent) - 1)

def fermi_dirac_distribution(energy, chemical_potential, temperature):
    exponent = (energy - chemical_potential) / (BOLTZMANN_CONSTANT * temperature)
    return 1 / (math.exp(exponent) + 1)

def planck_distribution(frequency, temperature):
    hf_kt = PLANCK_CONSTANT * frequency / (BOLTZMANN_CONSTANT * temperature)
    return (2 * PLANCK_CONSTANT * frequency**3 / SPEED_OF_LIGHT**2) / (math.exp(hf_kt) - 1)

# Additional Functions
def bose_einstein_photon_distribution(energy, temperature):
    exponent = energy / (BOLTZMANN_CONSTANT * temperature)
    return 1 / (math.exp(exponent) - 1)

def thermal_de_broglie_wavelength(mass, temperature):
    return PLANCK_CONSTANT / math.sqrt(2 * math.pi * mass * BOLTZMANN_CONSTANT * temperature)

def bose_einstein_critical_temperature(mass, particle_density):
    return (2 * math.pi * PLANCK_CONSTANT**2 / (BOLTZMANN_CONSTANT * mass)) * (particle_density)**(2/3)

def stefan_boltzmann_law(temperature):
    return STEFAN_BOLTZMANN_CONSTANT * temperature**4

def bose_partition_function(volume, thermal_wavelength):
    return (volume / thermal_wavelength**3) / (1 - math.exp(-1))

def boltzmann_distribution(energy, temperature, partition_function):
    return math.exp(-energy / (BOLTZMANN_CONSTANT * temperature)) / partition_function

def fermi_dirac_high_temperature(energy, temperature, chemical_potential):
    exponent = (energy - chemical_potential) / (BOLTZMANN_CONSTANT * temperature)
    return 1 / (math.exp(exponent) + 1)

def planck_radiation_law(frequency, temperature):
    exponent = (PLANCK_CONSTANT * frequency) / (BOLTZMANN_CONSTANT * temperature)
    return (8 * math.pi * PLANCK_CONSTANT * frequency**3) / (SPEED_OF_LIGHT**3 * (math.exp(exponent) - 1))


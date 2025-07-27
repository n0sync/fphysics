"""Electronic properties"""

import numpy as np
from constants import *

class BandStructure:
    def __init__(self, k_points, energies):
        self.k_points = k_points
        self.energies = energies
    
    def effective_mass(self, band_index, k_point):
        # Calculate effective mass using second derivative
        dk = 1e-6
        d2E_dk2 = np.gradient(np.gradient(self.energies[band_index]))
        return REDUCED_PLANCK**2 / (d2E_dk2[k_point] * ELECTRON_VOLT)
    
    def fermi_velocity(self, band_index, k_point):
        dE_dk = np.gradient(self.energies[band_index])
        return dE_dk[k_point] * ELECTRON_VOLT / REDUCED_PLANCK

class DensityOfStates:
    def __init__(self, energies, dos):
        self.energies = energies
        self.dos = dos
    
    def fermi_level(self, n_electrons):
        # Find Fermi level for given electron density
        cumulative = np.cumsum(self.dos)
        fermi_index = np.searchsorted(cumulative, n_electrons)
        return self.energies[fermi_index]
    
    def carrier_density(self, fermi_energy, temperature):
        kT = BOLTZMANN_CONSTANT * temperature
        f_fermi = 1 / (1 + np.exp((self.energies - fermi_energy) / kT))
        return np.trapz(self.dos * f_fermi, self.energies)

class FermiSurface:
    def __init__(self, k_mesh, energies, fermi_energy):
        self.k_mesh = k_mesh
        self.energies = energies
        self.fermi_energy = fermi_energy
    
    def cyclotron_frequency(self, magnetic_field):
        # Simplified cyclotron frequency calculation
        return ELEMENTARY_CHARGE * magnetic_field / ELECTRON_MASS
    
    def hall_coefficient(self, carrier_density):
        return 1 / (ELEMENTARY_CHARGE * carrier_density)

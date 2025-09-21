import numpy as np
from ..constants import *

class BCSTheory:
    def __init__(self, fermi_energy, coupling_constant):
        self.fermi_energy = fermi_energy
        self.coupling_constant = coupling_constant
    
    def energy_gap(self, temperature=0):
        if temperature == 0:
            # Zero temperature gap
            return 2 * REDUCED_PLANCK * self.debye_frequency() * np.exp(-1/self.coupling_constant)
        else:
            # Temperature dependent gap (simplified)
            Tc = self.critical_temperature()
            if temperature >= Tc:
                return 0
            return self.energy_gap(0) * np.sqrt(1 - (temperature/Tc)**2)
    
    def critical_temperature(self):
        # BCS critical temperature
        ω_D = self.debye_frequency()
        return 1.14 * REDUCED_PLANCK * ω_D / BOLTZMANN_CONSTANT * np.exp(-1/self.coupling_constant)
    
    def debye_frequency(self):
        # Estimate Debye frequency from Fermi energy
        return self.fermi_energy / REDUCED_PLANCK
    
    def coherence_length(self, temperature=0):
        gap = self.energy_gap(temperature)
        if gap == 0:
            return np.inf
        vF = np.sqrt(2 * self.fermi_energy / ELECTRON_MASS)
        return REDUCED_PLANCK * vF / (PI * gap)
    
    def penetration_depth(self, carrier_density):
        return np.sqrt(ELECTRON_MASS / (VACUUM_PERMEABILITY * carrier_density * ELEMENTARY_CHARGE**2))

class CooperPair:
    def __init__(self, momentum_k):
        self.momentum_k = momentum_k
    
    def binding_energy(self, coupling_strength, fermi_energy):
        # Simplified Cooper pair binding energy
        return 2 * REDUCED_PLANCK * fermi_energy * np.exp(-1/coupling_strength)
    
    def pair_wavefunction(self, r, coherence_length):
        # Simplified pair wavefunction
        return np.exp(-r / coherence_length) / np.sqrt(coherence_length**3)
    
    def josephson_frequency(self, voltage):
        return 2 * ELEMENTARY_CHARGE * voltage / REDUCED_PLANCK


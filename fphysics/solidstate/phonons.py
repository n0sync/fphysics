"""Phonons"""

import numpy as np
from constants import *

class PhononDispersion:
    def __init__(self, q_points, frequencies):
        self.q_points = q_points
        self.frequencies = frequencies
    
    def group_velocity(self, branch_index, q_point):
        dω_dq = np.gradient(self.frequencies[branch_index])
        return dω_dq[q_point]
    
    def debye_frequency(self, n_atoms, volume):
        # Debye cutoff frequency
        v_avg = np.mean([self.sound_velocity(i) for i in range(3)])
        return v_avg * (6 * PI**2 * n_atoms / volume)**(1/3)

    def sound_velocity(self, branch_index):
        # Linear phonon velocity near q=0
        return np.gradient(self.frequencies[branch_index])[0]

class PhononDOS:
    def __init__(self, frequencies, dos):
        self.frequencies = frequencies
        self.dos = dos
    
    def heat_capacity(self, temperature):
        kT = BOLTZMANN_CONSTANT * temperature
        x = REDUCED_PLANCK * self.frequencies / kT
        # Avoid division by zero
        x = np.where(x > 0, x, 1e-10)
        cv = BOLTZMANN_CONSTANT * x**2 * np.exp(x) / (np.exp(x) - 1)**2
        return np.trapz(cv * self.dos, self.frequencies)
    
    def debye_temperature(self):
        # Estimate Debye temperature
        ω_max = np.max(self.frequencies)
        return REDUCED_PLANCK * ω_max / BOLTZMANN_CONSTANT
    
    def average_phonon_number(self, temperature):
        kT = BOLTZMANN_CONSTANT * temperature
        x = REDUCED_PLANCK * self.frequencies / kT
        n_bose = 1 / (np.exp(x) - 1)
        return np.trapz(n_bose * self.dos, self.frequencies)

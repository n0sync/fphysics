"""Magnetic materials"""

import numpy as np
from ..constants import *

class MagneticMoment:
    def __init__(self, spin, orbital_moment=0):
        self.spin = spin
        self.orbital_moment = orbital_moment
    
    def total_moment(self):
        return np.sqrt(self.spin**2 + self.orbital_moment**2)
    
    def gyromagnetic_ratio(self):
        return ELEMENTARY_CHARGE / (2 * ELECTRON_MASS)
    
    def magnetic_moment(self):
        return self.spin * BOHR_MAGNETON

class SpinModel:
    def __init__(self, spins, coupling_matrix):
        self.spins = spins
        self.coupling_matrix = coupling_matrix
    
    def heisenberg_energy(self):
        # Classical Heisenberg model energy
        energy = 0
        for i in range(len(self.spins)):
            for j in range(i+1, len(self.spins)):
                energy -= self.coupling_matrix[i,j] * np.dot(self.spins[i], self.spins[j])
        return energy
    
    def exchange_field(self, site_index):
        # Mean field approximation
        field = np.zeros(3)
        for j in range(len(self.spins)):
            if j != site_index:
                field += self.coupling_matrix[site_index,j] * self.spins[j]
        return field
    
    def magnetization(self):
        return np.mean(self.spins, axis=0)
    
    def curie_temperature(self, avg_coupling, coordination):
        # Mean field estimate
        return avg_coupling * coordination * self.spin**2 / (3 * BOLTZMANN_CONSTANT)
    
    def susceptibility(self, temperature):
        # Curie-Weiss law
        C = self.spin * (self.spin + 1) * BOHR_MAGNETON**2 / (3 * BOLTZMANN_CONSTANT)
        return C / temperature

"""Crystallography"""

import numpy as np
from constants import *

class CrystalLattice:
    def __init__(self, a, b, c, alpha, beta, gamma):
        self.a, self.b, self.c = a, b, c
        self.alpha, self.beta, self.gamma = np.radians([alpha, beta, gamma])
    
    def volume(self):
        cos_alpha, cos_beta, cos_gamma = np.cos([self.alpha, self.beta, self.gamma])
        return self.a * self.b * self.c * np.sqrt(1 + 2*cos_alpha*cos_beta*cos_gamma - 
                                                   cos_alpha**2 - cos_beta**2 - cos_gamma**2)
    
    def reciprocal_lattice(self):
        V = self.volume()
        b1 = 2*PI * np.cross(self.b_vec, self.c_vec) / V
        b2 = 2*PI * np.cross(self.c_vec, self.a_vec) / V
        b3 = 2*PI * np.cross(self.a_vec, self.b_vec) / V
        return b1, b2, b3

class UnitCell:
    def __init__(self, lattice, atoms):
        self.lattice = lattice
        self.atoms = atoms
    
    def structure_factor(self, hkl):
        h, k, l = hkl
        F = 0
        for atom in self.atoms:
            r_dot_k = 2*PI * (h*atom['x'] + k*atom['y'] + l*atom['z'])
            F += atom['f'] * np.exp(1j * r_dot_k)
        return F

class BravaisLattice:
    def __init__(self, lattice_type):
        self.lattice_type = lattice_type
    
    def get_lattice_vectors(self, a, b=None, c=None):
        if b is None: b = a
        if c is None: c = a
        
        if self.lattice_type == 'cubic':
            return np.array([[a, 0, 0], [0, a, 0], [0, 0, a]])
        elif self.lattice_type == 'fcc':
            return np.array([[0, a/2, a/2], [a/2, 0, a/2], [a/2, a/2, 0]])
        elif self.lattice_type == 'bcc':
            return np.array([[-a/2, a/2, a/2], [a/2, -a/2, a/2], [a/2, a/2, -a/2]])
        elif self.lattice_type == 'hexagonal':
            return np.array([[a, 0, 0], [-a/2, a*np.sqrt(3)/2, 0], [0, 0, c]])
        else:
            raise ValueError(f"Unknown lattice type: {self.lattice_type}")

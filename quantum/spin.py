import numpy as np
from constants import *

def spin_matrices():
    sigma_x = np.array([[0, 1], [1, 0]])
    sigma_y = np.array([[0, -1j], [1j, 0]])
    sigma_z = np.array([[1, 0], [0, -1]])
    return sigma_x, sigma_y, sigma_z

def spin_eigenvalues(s):
    return np.array([-s, s])

def spin_eigenvectors():
    up = np.array([1, 0])
    down = np.array([0, 1])
    return up, down

def spin_angular_momentum(s):
    return REDUCED_PLANCK * s

def magnetic_moment(g, s):
    return g * BOHR_MAGNETON * s

def zeeman_energy(B, mu):
    return -mu * B

def spin_orbit_coupling(j, l, s):
    return 0.5 * (j * (j + 1) - l * (l + 1) - s * (s + 1))

def total_angular_momentum(l, s):
    return np.sqrt((l + s) * (l + s + 1)) * REDUCED_PLANCK

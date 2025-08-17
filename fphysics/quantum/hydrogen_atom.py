import numpy as np
from constants import *

def hydrogen_energy_levels(n):
    return -RYDBERG_CONSTANT * PLANCK_CONSTANT * SPEED_OF_LIGHT / n**2

def bohr_radius():
    return BOHR_RADIUS

def hydrogen_wavefunction(n, l, m, r, theta, phi):
    R_nl = radial_wavefunction(n, l, r)
    Y_lm = spherical_harmonics(l, m, theta, phi)
    return R_nl * Y_lm

def radial_wavefunction(n, l, r):
    a0 = BOHR_RADIUS
    rho = 2 * r / (n * a0)
    return np.sqrt((2 / (n * a0))**3 * np.math.factorial(n - l - 1) / (2 * n * np.math.factorial(n + l))) * np.exp(-rho/2) * rho**l * laguerre_polynomial(n - l - 1, 2*l + 1, rho)

def spherical_harmonics(l, m, theta, phi):
    return associated_legendre(l, m, np.cos(theta)) * np.exp(1j * m * phi)

def associated_legendre(l, m, x):
    # Simplified implementation
    if l == 0:
        return 1
    elif l == 1:
        if m == 0:
            return x
        elif m == 1:
            return -np.sqrt(1 - x**2)
    return 0  # Simplified

def laguerre_polynomial(n, alpha, x):
    # Simplified implementation
    if n == 0:
        return 1
    elif n == 1:
        return 1 + alpha - x
    return 0  # Simplified

def hydrogen_binding_energy():
    return 13.6 * ELECTRON_VOLT

def fine_structure_constant():
    return FINE_STRUCTURE_CONSTANT

def quantum_numbers_hydrogen(n, l, m, s):
    return n, l, m, s

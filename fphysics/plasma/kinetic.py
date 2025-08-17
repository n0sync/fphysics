"""Kinetic theory and distribution functions for plasma."""

import numpy as np
from constants import *

def maxwell_boltzmann(v, T, mass):
    """Maxwell-Boltzmann velocity distribution."""
    v_th = np.sqrt(BOLTZMANN_CONSTANT * T / mass)
    return (4 * np.pi * v**2) * (mass / (2 * np.pi * BOLTZMANN_CONSTANT * T))**(3/2) * np.exp(-mass * v**2 / (2 * BOLTZMANN_CONSTANT * T))

def maxwellian_3d(vx, vy, vz, T, mass):
    """3D Maxwellian distribution."""
    v_th = np.sqrt(BOLTZMANN_CONSTANT * T / mass)
    normalization = (mass / (2 * np.pi * BOLTZMANN_CONSTANT * T))**(3/2)
    return normalization * np.exp(-mass * (vx**2 + vy**2 + vz**2) / (2 * BOLTZMANN_CONSTANT * T))

def drift_maxwellian(v, v_drift, T, mass):
    """Drifting Maxwellian distribution."""
    v_th = np.sqrt(BOLTZMANN_CONSTANT * T / mass)
    return (4 * np.pi * v**2) * (mass / (2 * np.pi * BOLTZMANN_CONSTANT * T))**(3/2) * np.exp(-mass * (v - v_drift)**2 / (2 * BOLTZMANN_CONSTANT * T))

def collision_frequency(n, T, mass, charge, ln_lambda):
    """Coulomb collision frequency."""
    v_th = np.sqrt(BOLTZMANN_CONSTANT * T / mass)
    return np.sqrt(2) * n * charge**4 * ln_lambda / (12 * np.pi**(3/2) * VACUUM_PERMITTIVITY**2 * mass**2 * v_th**3)

def coulomb_logarithm(T, n):
    """Coulomb logarithm for electron-ion collisions."""
    lambda_d = np.sqrt(VACUUM_PERMITTIVITY * BOLTZMANN_CONSTANT * T / (n * ELEMENTARY_CHARGE**2))
    b_min = ELEMENTARY_CHARGE**2 / (4 * np.pi * VACUUM_PERMITTIVITY * BOLTZMANN_CONSTANT * T)
    return np.log(lambda_d / b_min)

def spitzer_resistivity(T, Z, ln_lambda):
    """Spitzer resistivity."""
    return (np.sqrt(np.pi) * ELECTRON_MASS * ELEMENTARY_CHARGE * ln_lambda) / (
        12 * np.pi**(3/2) * VACUUM_PERMITTIVITY**2 * BOLTZMANN_CONSTANT**(3/2) * T**(3/2)
    )

def landau_damping_rate(k, omega_p, T, mass):
    """Landau damping rate for electron plasma waves."""
    v_th = np.sqrt(BOLTZMANN_CONSTANT * T / mass)
    xi = omega_p / (k * v_th)
    return np.sqrt(np.pi / 8) * omega_p * (1 / xi**3) * np.exp(-xi**2 / 2)

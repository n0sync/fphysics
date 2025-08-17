"""Basic plasma properties and parameters."""

import numpy as np
from constants import *

def plasma_frequency(n_e):
    """Calculate electron plasma frequency."""
    return np.sqrt(n_e * ELEMENTARY_CHARGE**2 / (ELECTRON_MASS * VACUUM_PERMITTIVITY))

def debye_length(T_e, n_e):
    """Calculate Debye length."""
    return np.sqrt(VACUUM_PERMITTIVITY * BOLTZMANN_CONSTANT * T_e / (n_e * ELEMENTARY_CHARGE**2))

def debye_number(T_e, n_e):
    """Calculate number of particles in Debye sphere."""
    lambda_d = debye_length(T_e, n_e)
    return (4/3) * np.pi * lambda_d**3 * n_e

def cyclotron_frequency(B, mass, charge):
    """Calculate cyclotron frequency."""
    return abs(charge * B / mass)

def gyroradius(v_perp, B, mass, charge):
    """Calculate gyroradius (Larmor radius)."""
    omega_c = cyclotron_frequency(B, mass, charge)
    return v_perp / omega_c

def thermal_velocity(T, mass):
    """Calculate thermal velocity."""
    return np.sqrt(BOLTZMANN_CONSTANT * T / mass)

def plasma_beta(n, T, B):
    """Calculate plasma beta parameter."""
    p_thermal = n * BOLTZMANN_CONSTANT * T
    p_magnetic = B**2 / (2 * VACUUM_PERMEABILITY)
    return p_thermal / p_magnetic

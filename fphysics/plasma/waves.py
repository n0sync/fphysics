import numpy as np
from ..constants import *


def langmuir_frequency(n_e):
    """Calculate Langmuir (electron plasma) frequency."""
    return np.sqrt(n_e * ELEMENTARY_CHARGE**2 / (ELECTRON_MASS * VACUUM_PERMITTIVITY))

def ion_plasma_frequency(n_i, Z, mass_i):
    """Calculate ion plasma frequency."""
    return np.sqrt(n_i * (Z * ELEMENTARY_CHARGE)**2 / (mass_i * VACUUM_PERMITTIVITY))

def upper_hybrid_frequency(omega_pe, omega_ce):
    """Calculate upper hybrid frequency."""
    return np.sqrt(omega_pe**2 + omega_ce**2)

def lower_hybrid_frequency(omega_pi, omega_ce, omega_ci):
    """Calculate lower hybrid frequency."""
    return np.sqrt(omega_pi**2 * omega_ce / (omega_ce + omega_ci))

def plasma_dispersion_cold(k, omega_pe, omega_ce=0):
    """Cold plasma dispersion relation."""
    return omega_pe**2 + omega_ce**2 - k**2 * SPEED_OF_LIGHT**2

def bohm_gross_dispersion(k, omega_pe, v_th):
    """Bohm-Gross dispersion relation for electron plasma waves."""
    return omega_pe**2 + 3 * k**2 * v_th**2

def ion_acoustic_dispersion(k, T_e, T_i, mass_i, Z=1):
    """Ion acoustic wave dispersion relation."""
    c_s = np.sqrt(BOLTZMANN_CONSTANT * (T_e + Z * T_i) / mass_i)
    return k * c_s

def alfven_wave_dispersion(k, B, density):
    """Alfvén wave dispersion relation."""
    v_a = B / np.sqrt(VACUUM_PERMEABILITY * density)
    return k * v_a

def magnetosonic_dispersion(k, B, T, density, mass, gamma=5/3):
    """Magnetosonic wave dispersion relation."""
    v_a = B / np.sqrt(VACUUM_PERMEABILITY * density)
    c_s = np.sqrt(gamma * BOLTZMANN_CONSTANT * T / mass)
    return k * np.sqrt(v_a**2 + c_s**2)

def cyclotron_harmonic(n, omega_c):
    """Calculate cyclotron harmonic frequencies."""
    return n * omega_c

def wave_energy_density(E, B):
    """Calculate electromagnetic wave energy density."""
    return 0.5 * (VACUUM_PERMITTIVITY * E**2 + B**2 / VACUUM_PERMEABILITY)

def group_velocity(omega, k):
    """Calculate group velocity dω/dk."""
    # For numerical calculation, this would require derivative computation
    pass

def phase_velocity(omega, k):
    """Calculate phase velocity."""
    return omega / k


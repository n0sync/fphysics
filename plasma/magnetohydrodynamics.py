"""Magnetohydrodynamics (MHD) equations and calculations."""

import numpy as np
from constants import *


def alfven_velocity(B, density):
    """Calculate Alfvén velocity."""
    return B / np.sqrt(VACUUM_PERMEABILITY * density)

def sound_velocity(T, mass, gamma=5/3):
    """Calculate sound velocity in plasma."""
    return np.sqrt(gamma * BOLTZMANN_CONSTANT * T / mass)

def magnetosonic_velocity(B, T, density, mass, gamma=5/3):
    """Calculate magnetosonic velocity."""
    v_a = alfven_velocity(B, density)
    c_s = sound_velocity(T, mass, gamma)
    return np.sqrt(v_a**2 + c_s**2)

def magnetic_pressure(B):
    """Calculate magnetic pressure."""
    return B**2 / (2 * VACUUM_PERMEABILITY)

def magnetic_reynolds_number(velocity, length, conductivity):
    """Calculate magnetic Reynolds number."""
    return VACUUM_PERMEABILITY * conductivity * velocity * length

def magnetic_diffusivity(conductivity):
    """Calculate magnetic diffusivity."""
    return 1 / (VACUUM_PERMEABILITY * conductivity)

def current_density(B, permeability=VACUUM_PERMEABILITY):
    """Calculate current density from magnetic field (∇ × B)."""
    # For numerical calculation, this would require gradient computation
    # This is a placeholder for the curl operation
    pass

def magnetic_tension(B, curvature_radius):
    """Calculate magnetic tension force per unit volume."""
    return B**2 / (VACUUM_PERMEABILITY * curvature_radius)

def plasma_displacement_current(E_dot):
    """Calculate displacement current in plasma."""
    return VACUUM_PERMITTIVITY * E_dot

def ohms_law_plasma(J, conductivity, v, B, E):
    """Generalized Ohm's law for plasma."""
    return J / conductivity + np.cross(v, B) - E

def mhd_equilibrium_condition(grad_p, J, B):
    """MHD equilibrium condition: ∇p = J × B."""
    return grad_p - np.cross(J, B)

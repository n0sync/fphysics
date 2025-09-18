import numpy as np
from ..constants import *

def tunnel_probability(E, V0, a):
    if E < V0:
        kappa = np.sqrt(2 * ELECTRON_MASS * (V0 - E)) / REDUCED_PLANCK
        return np.exp(-2 * kappa * a)
    else:
        return 1

def transmission_coefficient(E, V0, a):
    if E < V0:
        kappa = np.sqrt(2 * ELECTRON_MASS * (V0 - E)) / REDUCED_PLANCK
        return 1 / (1 + (V0**2 * np.sinh(kappa * a)**2) / (4 * E * (V0 - E)))
    else:
        return 1

def reflection_coefficient(E, V0, a):
    return 1 - transmission_coefficient(E, V0, a)

def wkb_approximation(E, V, x):
    p = np.sqrt(2 * ELECTRON_MASS * (E - V))
    return np.exp(-np.trapz(p, x) / REDUCED_PLANCK)

def alpha_decay_rate(Z, A, Q):
    return np.exp(-2 * PI * Z * FINE_STRUCTURE_CONSTANT * np.sqrt(2 * ATOMIC_MASS_UNIT / Q))

def scanning_tunneling_current(V, d, phi):
    return np.exp(-2 * d * np.sqrt(2 * ELECTRON_MASS * phi) / REDUCED_PLANCK)


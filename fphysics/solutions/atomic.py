import numpy as np


def get_particle_counts(atomic_number, mass_number):
    return {
        'protons': atomic_number,
        'electrons': atomic_number,
        'neutrons': mass_number - atomic_number
    }


def bohr_radius(n=1):
    a0 = 5.29e-11
    return n**2 * a0


def energy_level(n, z=1):
    rydberg_constant = 13.6
    return -z**2 * rydberg_constant / n**2


def transition_energy(n_initial, n_final, z=1):
    return energy_level(n_final, z) - energy_level(n_initial, z)


def wavelength_from_transition(n_initial, n_final, z=1):
    h = 6.626e-34
    c = 3e8
    energy_joules = transition_energy(n_initial, n_final, z) * 1.602e-19
    return h * c / abs(energy_joules)


def rydberg_formula(n1, n2, z=1):
    rydberg_constant = 1.097e7
    return rydberg_constant * z**2 * (1/n1**2 - 1/n2**2)


def fine_structure_constant():
    return 7.297e-3


def spin_orbit_splitting(n, j, l, z):
    alpha = fine_structure_constant()
    if l == 0:
        return 0
    return (alpha**2 * z**4 / n**3) * (1/j - 1/(l + 0.5))


def laguerre_polynomial(x, n, alpha):
    if n == 0:
        return 1
    elif n == 1:
        return 1 + alpha - x
    else:
        return ((2*n - 1 + alpha - x) * laguerre_polynomial(x, n-1, alpha) - 
                (n - 1 + alpha) * laguerre_polynomial(x, n-2, alpha)) / n


def radial_wavefunction(r, n, l):
    a0 = bohr_radius()
    rho = 2 * r / (n * a0)
    normalization = np.sqrt((2/(n*a0))**3 * np.math.factorial(n-l-1)/(2*n*np.math.factorial(n+l)))
    exponential = np.exp(-rho/2)
    laguerre = laguerre_polynomial(rho, n-l-1, 2*l+1)
    return normalization * (rho**l) * exponential * laguerre

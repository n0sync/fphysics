import numpy as np
from constants import *

def first_order_correction(E_n, psi_n, H_prime):
    return np.vdot(psi_n, H_prime @ psi_n)

def second_order_correction(E_n, psi_n, H_prime, energies, wavefunctions):
    correction = 0
    for idx, (En, psin) in enumerate(zip(energies, wavefunctions)):
        if En != E_n:
            correction += np.abs(np.vdot(psin, H_prime @ psi_n))**2 / (E_n - En)
    return correction

def stark_effect(E_n, psi_n, H_prime):
    return first_order_correction(E_n, psi_n, H_prime)

def zeeman_effect(mu_B, B, g_L, j):
    return g_L * mu_B * j * B

def perturbation_matrix_element(psi_m, H_prime, psi_n):
    return np.vdot(psi_m, H_prime @ psi_n)

def degenerate_perturbation_theory(H_prime, energies, wavefunctions):
    H_prime_matrix = np.array([[perturbation_matrix_element(psi_m, H_prime, psi_n) 
                               for psi_m in wavefunctions] 
                               for psi_n in wavefunctions])
    return np.linalg.eigvals(H_prime_matrix)

def variational_method(psi_trial, H, psi_trial_prime):
    return np.vdot(psi_trial, H @ psi_trial) / np.vdot(psi_trial, psi_trial)

def hellmann_feynman_theorem(dH_dlambda, psi_n):
    return np.vdot(psi_n, dH_dlambda @ psi_n)

def fermi_golden_rule(E_initial, V, E_final):
    return 2 * PI / REDUCED_PLANCK * np.abs(np.vdot(E_final, V @ E_initial))**2

def time_independent_perturbation(psi_n, H_prime, energies):
    return np.array([first_order_correction(En, psi_n, H_prime) for En in energies])

def fine_structure_hydrogen(Z, n):
    alpha = FINE_STRUCTURE_CONSTANT
    return alpha**2 * RYDBERG_CONSTANT / n**4 * (3/4 * n - Z)

def hyperfine_splitting(A, I, J):
    return A * (J * (J + 1) - I * (I + 1) - 3/4)

def lamb_shift(n, l):
    return 1057.8 * (1/n**3 - 1/(n * (l + 1/2))) * 1e6 # Hz

def relativistic_mass(mass, v, c=SPEED_OF_LIGHT):
    return mass / np.sqrt(1 - v**2 / c**2)

def breit_wigner_resonance(E, E0, gamma):
    return gamma / ((E - E0)**2 + gamma**2 / 4)

def coherent_state_correction(alpha, N):
    return np.sum([np.abs(alpha**n)**2 / np.math.factorial(n) for n in range(N)])

def intermolecular_forces(r, A, B):
    return A / r**12 - B / r**6

def atomic_units_conversion(value, from_unit='eV', to_unit='Hartree'):
    conversion_factors = {
        'eV_to_Hartree': 0.0367493,
        'Hartree_to_eV': 27.2114
    }
    if from_unit == 'eV' and to_unit == 'Hartree':
        return value * conversion_factors['eV_to_Hartree']
    elif from_unit == 'Hartree' and to_unit == 'eV':
        return value * conversion_factors['Hartree_to_eV']
    return value

def quantum_defect(n, l, delta):
    return n - delta

def harmonic_vibration_energy(v, omega_e, omega_ex_e):
    return PLANCK_CONSTANT * omega_e * (v + 0.5) - PLANCK_CONSTANT**2 * omega_ex_e * (v + 0.5)**2

def quadratic_stark_effect(alpha, E):
    return -0.5 * alpha * E**2

def adiabatic_approximation(H, psi_n):
    return np.vdot(psi_n, H @ psi_n)

def born_oppenheimer_approximation(psi_nuc, H_electronic, psi_elect):
    return np.vdot(psi_nuc, H_electronic @ psi_elect)

def spin_orbit_interaction(l, s):
    return REDUCED_PLANCK**2 * l * s / (2 * ELECTRON_MASS**2 * SPEED_OF_LIGHT**2)

def fermi_contact_interaction(A, I, J):
    return A * (I * (I + 1) + J * (J + 1) - 1.5)

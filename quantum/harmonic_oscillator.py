import numpy as np
from constants import *

def harmonic_oscillator_energy(n, omega):
    return REDUCED_PLANCK * omega * (n + 0.5)

def harmonic_oscillator_frequency(k, m):
    return np.sqrt(k / m)

def harmonic_oscillator_wavefunction(n, x, omega, m):
    alpha = np.sqrt(m * omega / REDUCED_PLANCK)
    xi = alpha * x
    
    # Hermite polynomials
    H_n = hermite_polynomial(n, xi)
    
    # Normalization
    norm = (alpha / np.sqrt(PI))**(1/2) * (1 / np.sqrt(2**n * np.math.factorial(n)))
    
    return norm * H_n * np.exp(-xi**2 / 2)

def hermite_polynomial(n, x):
    if n == 0:
        return np.ones_like(x)
    elif n == 1:
        return 2 * x
    else:
        H_nm2 = np.ones_like(x)
        H_nm1 = 2 * x
        for i in range(2, n + 1):
            H_n = 2 * x * H_nm1 - 2 * (i - 1) * H_nm2
            H_nm2 = H_nm1
            H_nm1 = H_n
        return H_n

def zero_point_energy(omega):
    return 0.5 * REDUCED_PLANCK * omega

def classical_turning_point(n, omega, m):
    E_n = harmonic_oscillator_energy(n, omega)
    return np.sqrt(2 * E_n / (m * omega**2))

def probability_density_ho(n, x, omega, m):
    psi = harmonic_oscillator_wavefunction(n, x, omega, m)
    return np.abs(psi)**2

def expectation_value_x(n):
    return 0

def expectation_value_x_squared(n, omega, m):
    return REDUCED_PLANCK * (n + 0.5) / (m * omega)

def expectation_value_p(n):
    return 0

def expectation_value_p_squared(n, omega, m):
    return REDUCED_PLANCK * m * omega * (n + 0.5)

def uncertainty_x(n, omega, m):
    return np.sqrt(REDUCED_PLANCK * (n + 0.5) / (m * omega))

def uncertainty_p(n, omega, m):
    return np.sqrt(REDUCED_PLANCK * m * omega * (n + 0.5))

def uncertainty_product(n, omega, m):
    return uncertainty_x(n, omega, m) * uncertainty_p(n, omega, m)

def creation_operator_matrix(n_max):
    matrix = np.zeros((n_max + 1, n_max + 1))
    for n in range(n_max):
        matrix[n + 1, n] = np.sqrt(n + 1)
    return matrix

def annihilation_operator_matrix(n_max):
    matrix = np.zeros((n_max + 1, n_max + 1))
    for n in range(1, n_max + 1):
        matrix[n - 1, n] = np.sqrt(n)
    return matrix

def number_operator_matrix(n_max):
    matrix = np.zeros((n_max + 1, n_max + 1))
    for n in range(n_max + 1):
        matrix[n, n] = n
    return matrix

def position_operator_matrix(n_max, omega, m):
    a = annihilation_operator_matrix(n_max)
    a_dag = creation_operator_matrix(n_max)
    return np.sqrt(REDUCED_PLANCK / (2 * m * omega)) * (a + a_dag)

def momentum_operator_matrix(n_max, omega, m):
    a = annihilation_operator_matrix(n_max)
    a_dag = creation_operator_matrix(n_max)
    return 1j * np.sqrt(REDUCED_PLANCK * m * omega / 2) * (a_dag - a)

def hamiltonian_matrix(n_max, omega):
    matrix = np.zeros((n_max + 1, n_max + 1))
    for n in range(n_max + 1):
        matrix[n, n] = REDUCED_PLANCK * omega * (n + 0.5)
    return matrix

def coherent_state_amplitude(alpha, n):
    return np.exp(-abs(alpha)**2 / 2) * (alpha**n) / np.sqrt(np.math.factorial(n))

def coherent_state_wavefunction(alpha, x, omega, m):
    alpha_complex = alpha
    x0 = np.sqrt(2 * REDUCED_PLANCK / (m * omega)) * np.real(alpha_complex)
    p0 = np.sqrt(2 * REDUCED_PLANCK * m * omega) * np.imag(alpha_complex)
    
    # Displaced ground state
    psi_0 = harmonic_oscillator_wavefunction(0, x - x0, omega, m)
    return psi_0 * np.exp(1j * p0 * x / REDUCED_PLANCK)

def squeezed_state_parameter(r, theta):
    return r * np.exp(1j * theta)

def squeezed_state_variance_x(r, omega, m):
    return (REDUCED_PLANCK / (2 * m * omega)) * np.exp(-2 * r)

def squeezed_state_variance_p(r, omega, m):
    return (REDUCED_PLANCK * m * omega / 2) * np.exp(2 * r)

def fock_state_probability(n, alpha):
    return np.abs(coherent_state_amplitude(alpha, n))**2

def displacement_operator_matrix(alpha, n_max):
    a = annihilation_operator_matrix(n_max)
    a_dag = creation_operator_matrix(n_max)
    return np.exp(alpha * a_dag - np.conj(alpha) * a)

def squeeze_operator_matrix(r, theta, n_max):
    a = annihilation_operator_matrix(n_max)
    a_dag = creation_operator_matrix(n_max)
    xi = r * np.exp(1j * theta)
    return np.exp(0.5 * (np.conj(xi) * a @ a - xi * a_dag @ a_dag))

def wigner_function(x, p, rho, omega, m):
    # Simplified Wigner function for harmonic oscillator
    alpha = np.sqrt(m * omega / REDUCED_PLANCK)
    beta = np.sqrt(1 / (m * omega * REDUCED_PLANCK))
    
    # Phase space coordinates
    q = alpha * x
    pi = beta * p
    
    # Wigner function (simplified)
    return (2 / PI) * np.exp(-2 * (q**2 + pi**2)) * np.real(np.trace(rho))

def husimi_function(x, p, rho, omega, m):
    # Q-function for harmonic oscillator
    alpha = (np.sqrt(m * omega / (2 * REDUCED_PLANCK)) * x + 
             1j * p / np.sqrt(2 * REDUCED_PLANCK * m * omega))
    
    # Coherent state
    coherent = coherent_state_amplitude(alpha, 0)
    
    return (1 / PI) * np.abs(np.vdot(coherent, rho @ coherent))**2

def quantum_harmonic_oscillator_partition_function(omega, T):
    beta = 1 / (BOLTZMANN_CONSTANT * T)
    return 1 / (2 * np.sinh(beta * REDUCED_PLANCK * omega / 2))

def thermal_average_energy(omega, T):
    beta = 1 / (BOLTZMANN_CONSTANT * T)
    return REDUCED_PLANCK * omega / 2 * (1 + 2 / (np.exp(beta * REDUCED_PLANCK * omega) - 1))

def quantum_fluctuations(n, omega, m):
    return np.sqrt(expectation_value_x_squared(n, omega, m) - expectation_value_x(n)**2)

def vibrational_partition_function(omega, T):
    beta = 1 / (BOLTZMANN_CONSTANT * T)
    return np.exp(-beta * REDUCED_PLANCK * omega / 2) / (1 - np.exp(-beta * REDUCED_PLANCK * omega))

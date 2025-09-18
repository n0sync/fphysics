import numpy as np
from ..constants import *

def schrodinger_time_dependent(psi, H, t):
    return 1j * REDUCED_PLANCK * np.gradient(psi, t) + H @ psi

def schrodinger_time_independent(psi, H, E):
    return H @ psi - E * psi

def wave_function_normalization(psi, dx):
    return np.sqrt(np.trapz(np.abs(psi)**2, dx=dx))

def probability_density(psi):
    return np.abs(psi)**2

def probability_current(psi, psi_star, m):
    return (REDUCED_PLANCK / (2j * m)) * (psi_star * np.gradient(psi) - psi * np.gradient(psi_star))

def expectation_value(psi, operator, dx):
    return np.trapz(np.conj(psi) * operator @ psi, dx=dx)

def uncertainty(psi, operator, dx):
    avg = expectation_value(psi, operator, dx)
    avg_sq = expectation_value(psi, operator @ operator, dx)
    return np.sqrt(avg_sq - avg**2)

def free_particle_wavefunction(k, x, t):
    return np.exp(1j * (k * x - REDUCED_PLANCK * k**2 * t / (2 * ELECTRON_MASS)))

def plane_wave(k, x):
    return np.exp(1j * k * x)

def gaussian_wave_packet(x, x0, sigma, k0):
    return (1 / (2 * PI * sigma**2)**(1/4)) * np.exp(-(x - x0)**2 / (4 * sigma**2) + 1j * k0 * x)

def particle_in_box_wavefunction(n, L, x):
    return np.sqrt(2 / L) * np.sin(n * PI * x / L)

def particle_in_box_energy(n, L, m):
    return n**2 * PI**2 * REDUCED_PLANCK**2 / (2 * m * L**2)

def infinite_square_well(n, L, x):
    if 0 <= x <= L:
        return np.sqrt(2 / L) * np.sin(n * PI * x / L)
    else:
        return 0

def finite_square_well_even(x, a, V0, E):
    k = np.sqrt(2 * ELECTRON_MASS * E) / REDUCED_PLANCK
    kappa = np.sqrt(2 * ELECTRON_MASS * (V0 - E)) / REDUCED_PLANCK
    
    if abs(x) <= a:
        return np.cos(k * x)
    else:
        return np.cos(k * a) * np.exp(-kappa * (abs(x) - a))

def finite_square_well_odd(x, a, V0, E):
    k = np.sqrt(2 * ELECTRON_MASS * E) / REDUCED_PLANCK
    kappa = np.sqrt(2 * ELECTRON_MASS * (V0 - E)) / REDUCED_PLANCK
    
    if abs(x) <= a:
        return np.sin(k * x)
    else:
        return np.sin(k * a) * np.sign(x) * np.exp(-kappa * (abs(x) - a))

def step_potential_transmission(E, V0):
    if E > V0:
        k1 = np.sqrt(2 * ELECTRON_MASS * E) / REDUCED_PLANCK
        k2 = np.sqrt(2 * ELECTRON_MASS * (E - V0)) / REDUCED_PLANCK
        return 4 * k1 * k2 / (k1 + k2)**2
    else:
        return 0

def step_potential_reflection(E, V0):
    if E > V0:
        k1 = np.sqrt(2 * ELECTRON_MASS * E) / REDUCED_PLANCK
        k2 = np.sqrt(2 * ELECTRON_MASS * (E - V0)) / REDUCED_PLANCK
        return ((k1 - k2) / (k1 + k2))**2
    else:
        return 1

def barrier_transmission(E, V0, a):
    if E < V0:
        k = np.sqrt(2 * ELECTRON_MASS * E) / REDUCED_PLANCK
        kappa = np.sqrt(2 * ELECTRON_MASS * (V0 - E)) / REDUCED_PLANCK
        return 1 / (1 + (V0**2 * np.sinh(kappa * a)**2) / (4 * E * (V0 - E)))
    else:
        return step_potential_transmission(E, V0)

def wavefunction_continuity(psi1, psi2, dpsi1_dx, dpsi2_dx):
    return psi1 == psi2 and dpsi1_dx == dpsi2_dx

def time_evolution_operator(H, t):
    return np.exp(-1j * H * t / REDUCED_PLANCK)

def coherent_state(alpha, n):
    return np.exp(-abs(alpha)**2 / 2) * (alpha**n) / np.sqrt(np.math.factorial(n))

def squeezed_state(r, theta, n):
    return np.exp(r * np.cos(theta)) * coherent_state(r * np.sin(theta), n)

def entangled_state(psi1, psi2):
    return (psi1[0] * psi2[1] + psi1[1] * psi2[0]) / np.sqrt(2)

def bell_state(type='phi_plus'):
    if type == 'phi_plus':
        return np.array([1, 0, 0, 1]) / np.sqrt(2)
    elif type == 'phi_minus':
        return np.array([1, 0, 0, -1]) / np.sqrt(2)
    elif type == 'psi_plus':
        return np.array([0, 1, 1, 0]) / np.sqrt(2)
    elif type == 'psi_minus':
        return np.array([0, 1, -1, 0]) / np.sqrt(2)

def fidelity(psi1, psi2):
    return abs(np.vdot(psi1, psi2))**2

def von_neumann_entropy(rho):
    eigenvals = np.linalg.eigvals(rho)
    eigenvals = eigenvals[eigenvals > 0]
    return -np.sum(eigenvals * np.log2(eigenvals))

def density_matrix(psi):
    return np.outer(psi, np.conj(psi))

def partial_trace(rho, dims, axis):
    # Simplified partial trace for 2-qubit system
    if axis == 0:
        return rho[0:2, 0:2] + rho[2:4, 2:4]
    else:
        return rho[::2, ::2] + rho[1::2, 1::2]

def quantum_fidelity(rho1, rho2):
    sqrt_rho1 = np.sqrt(rho1)
    return (np.trace(np.sqrt(sqrt_rho1 @ rho2 @ sqrt_rho1)))**2

def concurrence(rho):
    # For 2-qubit states
    sigma_y = np.array([[0, -1j], [1j, 0]])
    sigma_y_tensor = np.kron(sigma_y, sigma_y)
    rho_tilde = sigma_y_tensor @ np.conj(rho) @ sigma_y_tensor
    eigenvals = np.linalg.eigvals(rho @ rho_tilde)
    eigenvals = np.sort(np.sqrt(eigenvals))[::-1]
    return max(0, eigenvals[0] - eigenvals[1] - eigenvals[2] - eigenvals[3])

def quantum_discord(rho_AB, rho_A, rho_B):
    # Simplified quantum discord calculation
    I_AB = von_neumann_entropy(rho_A) + von_neumann_entropy(rho_B) - von_neumann_entropy(rho_AB)
    # Classical correlation calculation would require optimization
    return I_AB  # Simplified

def bloch_sphere_coordinates(psi):
    # For single qubit state |psi> = a|0> + b|1>
    rho = density_matrix(psi)
    x = 2 * np.real(rho[0, 1])
    y = 2 * np.imag(rho[0, 1])
    z = np.real(rho[0, 0] - rho[1, 1])
    return x, y, z

def pauli_decomposition(rho):
    # Decompose 2x2 density matrix in Pauli basis
    sigma_x = np.array([[0, 1], [1, 0]])
    sigma_y = np.array([[0, -1j], [1j, 0]])
    sigma_z = np.array([[1, 0], [0, -1]])
    identity = np.eye(2)
    
    a0 = np.trace(rho @ identity) / 2
    a1 = np.trace(rho @ sigma_x) / 2
    a2 = np.trace(rho @ sigma_y) / 2
    a3 = np.trace(rho @ sigma_z) / 2
    
    return a0, a1, a2, a3


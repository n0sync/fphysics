import numpy as np
from ..constants import *

def momentum_operator(dx):
    return -1j * REDUCED_PLANCK * np.gradient(dx)

def kinetic_energy_operator(dx, m):
    return -REDUCED_PLANCK**2 / (2 * m) * np.gradient(np.gradient(dx))

def hamiltonian_operator(T, V):
    return T + V

def position_operator(x):
    return x

def angular_momentum_z(phi):
    return -1j * REDUCED_PLANCK * np.gradient(phi)

def angular_momentum_squared(theta, phi):
    return -REDUCED_PLANCK**2 * (np.sin(theta) * np.gradient(np.gradient(theta)) + np.gradient(np.gradient(phi)) / np.sin(theta)**2)

def commutator(A, B):
    return A @ B - B @ A

def anticommutator(A, B):
    return A @ B + B @ A

def uncertainty_principle(sigma_x, sigma_p):
    return sigma_x * sigma_p >= REDUCED_PLANCK / 2

def pauli_x():
    return np.array([[0, 1], [1, 0]])

def pauli_y():
    return np.array([[0, -1j], [1j, 0]])

def pauli_z():
    return np.array([[1, 0], [0, -1]])

def ladder_operator_plus(n):
    return np.sqrt(n + 1)

def ladder_operator_minus(n):
    return np.sqrt(n)

def number_operator(n):
    return n

def coherent_state_operator(alpha):
    return np.exp(alpha * ladder_operator_plus(0) - np.conj(alpha) * ladder_operator_minus(0))

def displacement_operator(alpha):
    return np.exp(alpha * ladder_operator_plus(0) - np.conj(alpha) * ladder_operator_minus(0))

def rotation_operator(theta, n):
    return np.exp(-1j * theta * n)

def time_evolution_operator(H, t):
    return np.exp(-1j * H * t / REDUCED_PLANCK)

def parity_operator(psi):
    return psi[::-1]

def translation_operator(a, p):
    return np.exp(1j * a * p / REDUCED_PLANCK)

def field_operator(x, t):
    return np.exp(1j * (x - SPEED_OF_LIGHT * t))

def creation_operator(omega, x):
    return np.sqrt(ELECTRON_MASS * omega / (2 * REDUCED_PLANCK)) * (x + 1j * momentum_operator(x) / (ELECTRON_MASS * omega))

def annihilation_operator(omega, x):
    return np.sqrt(ELECTRON_MASS * omega / (2 * REDUCED_PLANCK)) * (x - 1j * momentum_operator(x) / (ELECTRON_MASS * omega))

def squeeze_operator(r, theta):
    return np.exp(0.5 * r * (np.exp(1j * theta) * creation_operator(1, 0)**2 - np.exp(-1j * theta) * annihilation_operator(1, 0)**2))

def beam_splitter_operator(theta):
    return np.array([[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]])

def phase_shift_operator(phi):
    return np.array([[1, 0], [0, np.exp(1j * phi)]])

def hadamard_gate():
    return np.array([[1, 1], [1, -1]]) / np.sqrt(2)

def cnot_gate():
    return np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]])

def toffoli_gate():
    return np.array([[1, 0, 0, 0, 0, 0, 0, 0],
                     [0, 1, 0, 0, 0, 0, 0, 0],
                     [0, 0, 1, 0, 0, 0, 0, 0],
                     [0, 0, 0, 1, 0, 0, 0, 0],
                     [0, 0, 0, 0, 1, 0, 0, 0],
                     [0, 0, 0, 0, 0, 1, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 1],
                     [0, 0, 0, 0, 0, 0, 1, 0]])

def swap_gate():
    return np.array([[1, 0, 0, 0], [0, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, 1]])

def controlled_phase_gate(phi):
    return np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, np.exp(1j * phi)]])

def quantum_fourier_transform(n):
    N = 2**n
    qft_matrix = np.zeros((N, N), dtype=complex)
    for i in range(N):
        for j in range(N):
            qft_matrix[i, j] = np.exp(2j * PI * i * j / N) / np.sqrt(N)
    return qft_matrix

def density_matrix_operator(psi):
    return np.outer(psi, np.conj(psi))

def trace_operator(rho):
    return np.trace(rho)

def partial_trace_operator(rho, dims, subsystem):
    # Simplified for 2-qubit system
    if subsystem == 0:
        return rho[0:2, 0:2] + rho[2:4, 2:4]
    else:
        return rho[::2, ::2] + rho[1::2, 1::2]

def fidelity_operator(rho1, rho2):
    return np.trace(np.sqrt(np.sqrt(rho1) @ rho2 @ np.sqrt(rho1)))

def von_neumann_entropy_operator(rho):
    eigenvals = np.linalg.eigvals(rho)
    eigenvals = eigenvals[eigenvals > 0]
    return -np.sum(eigenvals * np.log2(eigenvals))

def measurement_operator(M, psi):
    return M @ psi

def projection_operator(psi):
    return np.outer(psi, np.conj(psi))

def born_rule_probability(M, psi):
    return np.abs(np.vdot(psi, M @ psi))**2

def kraus_operator(E, rho):
    return np.sum([E_i @ rho @ np.conj(E_i).T for E_i in E], axis=0)

def channel_fidelity(E, rho):
    return np.trace(np.sqrt(np.sqrt(rho) @ E(rho) @ np.sqrt(rho)))

def quantum_channel(E, rho):
    return np.sum([E_i @ rho @ np.conj(E_i).T for E_i in E], axis=0)

def dephasing_channel(gamma, rho):
    E0 = np.sqrt(1 - gamma) * np.eye(2)
    E1 = np.sqrt(gamma) * pauli_z()
    return E0 @ rho @ E0 + E1 @ rho @ E1

def amplitude_damping_channel(gamma, rho):
    E0 = np.array([[1, 0], [0, np.sqrt(1 - gamma)]])
    E1 = np.array([[0, np.sqrt(gamma)], [0, 0]])
    return E0 @ rho @ np.conj(E0).T + E1 @ rho @ np.conj(E1).T

def depolarizing_channel(p, rho):
    return (1 - p) * rho + p * np.eye(2) / 2

def bit_flip_channel(p, rho):
    return (1 - p) * rho + p * pauli_x() @ rho @ pauli_x()

def phase_flip_channel(p, rho):
    return (1 - p) * rho + p * pauli_z() @ rho @ pauli_z()

def bit_phase_flip_channel(p, rho):
    return (1 - p) * rho + p * pauli_y() @ rho @ pauli_y()


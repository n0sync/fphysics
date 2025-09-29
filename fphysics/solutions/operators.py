import numpy as np


def quantum_operator_operate(matrix, vector):
    result = [sum(x * y for x, y in zip(row, vector)) for row in matrix]
    return result


def commutator(operator_a, operator_b):
    ab = np.dot(operator_a, operator_b)
    ba = np.dot(operator_b, operator_a)
    return ab - ba


def anticommutator(operator_a, operator_b):
    ab = np.dot(operator_a, operator_b)
    ba = np.dot(operator_b, operator_a)
    return ab + ba


def operator_expectation_value(operator, state):
    state_conj = np.conj(state)
    operator_state = np.dot(operator, state)
    return np.dot(state_conj, operator_state)


def operator_norm(operator):
    eigenvalues = np.linalg.eigvals(operator)
    return np.max(np.abs(eigenvalues))


def operator_trace(operator):
    return np.trace(operator)


def operator_determinant(operator):
    return np.linalg.det(operator)


def is_hermitian(operator):
    return np.allclose(operator, np.conj(operator.T))


def is_unitary(operator):
    identity = np.eye(operator.shape[0])
    product = np.dot(operator, np.conj(operator.T))
    return np.allclose(product, identity)


def hermitian_conjugate(operator):
    return np.conj(operator.T)


def operator_exponential(operator, t=1.0):
    from scipy.linalg import expm
    return expm(-1j * t * operator)


def time_evolution_operator(hamiltonian, t):
    from scipy.linalg import expm
    return expm(-1j * t * hamiltonian)


def position_operator(n):
    return np.diag(np.arange(n), k=0)


def momentum_operator(n):
    diag_upper = np.ones(n-1) * 1j
    diag_lower = np.ones(n-1) * (-1j)
    return (np.diag(diag_upper, k=1) + np.diag(diag_lower, k=-1)) / 2


def creation_operator_matrix(n):
    diag = np.sqrt(np.arange(1, n))
    return np.diag(diag, k=1)


def annihilation_operator_matrix(n):
    diag = np.sqrt(np.arange(1, n))
    return np.diag(diag, k=-1)


def number_operator(n):
    return np.diag(np.arange(n))


def ladder_operator_plus(j):
    dim = int(2*j + 1)
    matrix = np.zeros((dim, dim))
    for m in range(dim-1):
        m_val = j - m
        matrix[m, m+1] = np.sqrt(j*(j+1) - m_val*(m_val-1))
    return matrix


def ladder_operator_minus(j):
    dim = int(2*j + 1)
    matrix = np.zeros((dim, dim))
    for m in range(1, dim):
        m_val = j - m
        matrix[m, m-1] = np.sqrt(j*(j+1) - m_val*(m_val+1))
    return matrix


def angular_momentum_x(j):
    j_plus = ladder_operator_plus(j)
    j_minus = ladder_operator_minus(j)
    return (j_plus + j_minus) / 2


def angular_momentum_y(j):
    j_plus = ladder_operator_plus(j)
    j_minus = ladder_operator_minus(j)
    return (j_plus - j_minus) / (2j)


def angular_momentum_z(j):
    dim = int(2*j + 1)
    m_values = np.arange(j, -j-1, -1)
    return np.diag(m_values)


def pauli_x():
    return np.array([[0, 1], [1, 0]], dtype=complex)


def pauli_y():
    return np.array([[0, -1j], [1j, 0]], dtype=complex)


def pauli_z():
    return np.array([[1, 0], [0, -1]], dtype=complex)


def pauli_identity():
    return np.eye(2, dtype=complex)


def projection_operator(state):
    state = np.array(state).reshape(-1, 1)
    return np.dot(state, np.conj(state.T))


def density_matrix(states, probabilities):
    rho = np.zeros((len(states[0]), len(states[0])), dtype=complex)
    for state, prob in zip(states, probabilities):
        rho += prob * projection_operator(state)
    return rho


def purity(density_matrix):
    return np.real(np.trace(np.dot(density_matrix, density_matrix)))


def von_neumann_entropy(density_matrix):
    eigenvalues = np.linalg.eigvalsh(density_matrix)
    eigenvalues = eigenvalues[eigenvalues > 1e-10]
    return -np.sum(eigenvalues * np.log(eigenvalues))


def fidelity(state1, state2):
    return np.abs(np.dot(np.conj(state1), state2))**2


def tensor_product(operator_a, operator_b):
    return np.kron(operator_a, operator_b)


def partial_trace(rho, dims, axis=0):
    n_dim = int(np.sqrt(rho.shape[0]))
    rho_reshaped = rho.reshape([dims[0], dims[1], dims[0], dims[1]])
    if axis == 0:
        return np.trace(rho_reshaped, axis1=0, axis2=2)
    else:
        return np.trace(rho_reshaped, axis1=1, axis2=3)


def swap_operator(dim):
    swap = np.zeros((dim**2, dim**2))
    for i in range(dim):
        for j in range(dim):
            swap[i*dim + j, j*dim + i] = 1
    return swap


def controlled_unitary(unitary):
    dim = unitary.shape[0]
    cu = np.eye(2*dim, dtype=complex)
    cu[dim:, dim:] = unitary
    return cu


def baker_campbell_hausdorff(a, b, order=3):
    result = a + b
    if order >= 2:
        result += commutator(a, b) / 2
    if order >= 3:
        result += (commutator(a, commutator(a, b)) + commutator(b, commutator(b, a))) / 12
    return result


def similarity_transform(operator, unitary):
    return np.dot(np.dot(unitary, operator), np.conj(unitary.T))


def matrix_power(operator, n):
    eigenvalues, eigenvectors = np.linalg.eig(operator)
    eigenvalues_power = eigenvalues ** n
    return np.dot(np.dot(eigenvectors, np.diag(eigenvalues_power)), np.linalg.inv(eigenvectors))


def matrix_logarithm(operator):
    eigenvalues, eigenvectors = np.linalg.eig(operator)
    log_eigenvalues = np.log(eigenvalues)
    return np.dot(np.dot(eigenvectors, np.diag(log_eigenvalues)), np.linalg.inv(eigenvectors))

import numpy as np
from scipy.linalg import expm

class Group:
    def __init__(self, elements, operation):
        self.elements = elements
        self.operation = operation
    
    def is_closed(self):
        for a in self.elements:
            for b in self.elements:
                if self.operation(a, b) not in self.elements:
                    return False
        return True
    
    def identity_element(self):
        for e in self.elements:
            if all(self.operation(e, a) == a and self.operation(a, e) == a for a in self.elements):
                return e
        return None

def pauli_matrices():
    sigma_x = np.array([[0, 1], [1, 0]], dtype=complex)
    sigma_y = np.array([[0, -1j], [1j, 0]], dtype=complex)
    sigma_z = np.array([[1, 0], [0, -1]], dtype=complex)
    return sigma_x, sigma_y, sigma_z

def rotation_matrix_2d(theta):
    return np.array([[np.cos(theta), -np.sin(theta)],
                     [np.sin(theta), np.cos(theta)]])

def rotation_matrix_3d(axis, angle):
    axis = axis / np.linalg.norm(axis)
    cos_angle = np.cos(angle)
    sin_angle = np.sin(angle)
    
    R = cos_angle * np.eye(3)
    R += sin_angle * np.array([[0, -axis[2], axis[1]],
                               [axis[2], 0, -axis[0]],
                               [-axis[1], axis[0], 0]])
    R += (1 - cos_angle) * np.outer(axis, axis)
    
    return R

def su2_generators():
    sigma_x, sigma_y, sigma_z = pauli_matrices()
    return 0.5 * sigma_x, 0.5 * sigma_y, 0.5 * sigma_z

def su3_gell_mann_matrices():
    lambda1 = np.array([[0, 1, 0], [1, 0, 0], [0, 0, 0]], dtype=complex)
    lambda2 = np.array([[0, -1j, 0], [1j, 0, 0], [0, 0, 0]], dtype=complex)
    lambda3 = np.array([[1, 0, 0], [0, -1, 0], [0, 0, 0]], dtype=complex)
    lambda4 = np.array([[0, 0, 1], [0, 0, 0], [1, 0, 0]], dtype=complex)
    lambda5 = np.array([[0, 0, -1j], [0, 0, 0], [1j, 0, 0]], dtype=complex)
    lambda6 = np.array([[0, 0, 0], [0, 0, 1], [0, 1, 0]], dtype=complex)
    lambda7 = np.array([[0, 0, 0], [0, 0, -1j], [0, 1j, 0]], dtype=complex)
    lambda8 = np.array([[1, 0, 0], [0, 1, 0], [0, 0, -2]], dtype=complex) / np.sqrt(3)
    
    return [lambda1, lambda2, lambda3, lambda4, lambda5, lambda6, lambda7, lambda8]

def lorentz_boost(v):
    gamma = 1 / np.sqrt(1 - np.dot(v, v))
    v_hat = v / np.linalg.norm(v) if np.linalg.norm(v) > 0 else np.array([0, 0, 0])
    
    boost = np.eye(4)
    boost[0, 0] = gamma
    boost[0, 1:4] = -gamma * v
    boost[1:4, 0] = -gamma * v
    boost[1:4, 1:4] = np.eye(3) + (gamma - 1) * np.outer(v_hat, v_hat)
    
    return boost

def poincare_group_element(rotation, translation, boost):
    transform = np.eye(4)
    transform[:3, :3] = rotation
    transform[:3, 3] = translation
    return np.dot(transform, boost)

def lie_bracket(A, B):
    return np.dot(A, B) - np.dot(B, A)

def structure_constants(generators):
    n = len(generators)
    f = np.zeros((n, n, n), dtype=complex)
    
    for i in range(n):
        for j in range(n):
            bracket = lie_bracket(generators[i], generators[j])
            for k in range(n):
                f[i, j, k] = np.trace(np.dot(bracket, generators[k].conj().T))
    
    return f

def representation_matrix(generator, representation_dim):
    return expm(1j * generator)

def character_table(group):
    characters = {}
    for element in group.elements:
        characters[element] = np.trace(element)
    return characters

def symmetry_operation_3d(operation_type, axis=None, angle=None):
    if operation_type == "identity":
        return np.eye(3)
    elif operation_type == "inversion":
        return -np.eye(3)
    elif operation_type == "rotation" and axis is not None and angle is not None:
        return rotation_matrix_3d(axis, angle)
    elif operation_type == "reflection" and axis is not None:
        n = axis / np.linalg.norm(axis)
        return np.eye(3) - 2 * np.outer(n, n)
    else:
        raise ValueError("Invalid operation type or missing parameters")

def young_tableau(shape):
    tableau = []
    for i, row_length in enumerate(shape):
        row = list(range(sum(shape[:i]) + 1, sum(shape[:i+1]) + 1))
        tableau.append(row)
    return tableau

def irreducible_representation_dimension(young_tableau):
    n = sum(len(row) for row in young_tableau)
    hook_lengths = []
    
    for i, row in enumerate(young_tableau):
        for j, box in enumerate(row):
            hook_length = len(row) - j + sum(1 for k in range(i+1, len(young_tableau)) if len(young_tableau[k]) > j)
            hook_lengths.append(hook_length)
    
    from math import factorial
    return factorial(n) // np.prod(hook_lengths)

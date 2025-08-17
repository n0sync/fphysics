import numpy as np


def linear_fem_1d(n_elements, length, load, boundary_conditions):
    element_length = length / n_elements
    k = np.zeros((n_elements + 1, n_elements + 1))
    f = np.zeros(n_elements + 1)

    for i in range(n_elements):
        xi = i * element_length
        xj = xi + element_length
        k_local = np.array([[1, -1],
                            [-1, 1]]) / element_length

        f_local = load(xi, xj) * element_length / 2 * np.array([1, 1])

        k[i:i+2, i:i+2] += k_local
        f[i:i+2] += f_local

    for node, value in boundary_conditions.items():
        k[node, :] = 0
        k[node, node] = 1
        f[node] = value

    u = np.linalg.solve(k, f)
    return u


def quadratic_fem_1d(n_elements, length, load, boundary_conditions):
    element_length = length / n_elements
    n_nodes = 2 * n_elements + 1
    k = np.zeros((n_nodes, n_nodes))
    f = np.zeros(n_nodes)

    for i in range(n_elements):
        xi = i * element_length
        xj = xi + element_length
        k_local = np.array([[7, -8, 1],
                            [-8, 16, -8],
                            [1, -8, 7]]) / (3 * element_length)

        f_local = load(xi, xj) * element_length / 6 * np.array([1, 4, 1])
        nodes = [2*i, 2*i+1, 2*i+2]

        for a in range(3):
            for b in range(3):
                k[nodes[a], nodes[b]] += k_local[a, b]
            f[nodes[a]] += f_local[a]

    for node, value in boundary_conditions.items():
        k[node, :] = 0
        k[node, node] = 1
        f[node] = value

    u = np.linalg.solve(k, f)
    return u


def fem_assembly(n_elements, element_matrices, global_size, boundary_conditions):
    k = np.zeros((global_size, global_size))
    f = np.zeros(global_size)

    for elem_index, (element_matrix, element_vector, mapping) in enumerate(element_matrices):
        for a, i in enumerate(mapping):
            for b, j in enumerate(mapping):
                k[i, j] += element_matrix[a, b]
            f[i] += element_vector[a]

    for node, value in boundary_conditions.items():
        k[node, :] = 0
        k[node, node] = 1
        f[node] = value

    u = np.linalg.solve(k, f)
    return u


def fem_solver_1d(length, n_elements, stiffness_matrix_func, load_vector_func, boundary_conditions):
    element_length = length / n_elements
    k_total = np.zeros((n_elements + 1, n_elements + 1))
    f_total = np.zeros(n_elements + 1)

    for i in range(n_elements):
        k_local = stiffness_matrix_func(i, element_length)
        f_local = load_vector_func(i, element_length)

        k_total[i:i+2, i:i+2] += k_local
        f_total[i:i+2] += f_local

    for node, value in boundary_conditions.items():
        k_total[node, :] = 0
        k_total[node, node] = 1
        f_total[node] = value

    displacements = np.linalg.solve(k_total, f_total)
    return displacements


def beam_2d(n_elements, length, force, support_positions):
    element_length = length / n_elements
    n_nodes = n_elements + 1
    k = np.zeros((n_nodes, n_nodes))
    f = np.zeros(n_nodes)

    for i in range(n_elements):
        xi = i * element_length
        xj = xi + element_length
        k_local = np.array([[1, -1],
                            [-1, 1]]) * 12 / element_length**3

        f_local = force(xi, xj) * element_length / 2 * np.array([1, 1])

        k[i:i+2, i:i+2] += k_local
        f[i:i+2] += f_local

    for node in support_positions:
        k[node, :] = 0
        k[node, node] = 1
        f[node] = 0

    displacements = np.linalg.solve(k, f)
    return displacements


def truss_2d(elements, nodes, forces, boundary_conditions):
    num_nodes = len(nodes)
    k_global = np.zeros((2*num_nodes, 2*num_nodes))
    f_global = np.zeros(2*num_nodes)

    for (node_i, node_j), area, youngs_modulus in elements:
        xi, yi = nodes[node_i]
        xj, yj = nodes[node_j]
        length = np.sqrt((xj - xi)**2 + (yj - yi)**2)
        c = (xj - xi) / length
        s = (yj - yi) / length
        k_local = (youngs_modulus * area / length) * np.array([[c*c, c*s, -c*c, -c*s],
                                                                 [c*s, s*s, -c*s, -s*s],
                                                                 [-c*c, -c*s, c*c, c*s],
                                                                 [-c*s, -s*s, c*s, s*s]])
        node_map = [2*node_i, 2*node_i+1, 2*node_j, 2*node_j+1]

        for a in range(4):
            for b in range(4):
                k_global[node_map[a], node_map[b]] += k_local[a, b]

    for node, values in forces.items():
        f_global[2*node:2*node+2] = values

    for node, conditions in boundary_conditions.items():
        f_global[2*node:2*node+2] = np.array(conditions)
        for i in range(2):
            dof_index = 2*node + i
            if conditions[i] is not None:
                k_global[dof_index, :] = 0
                k_global[dof_index, dof_index] = 1

    displacements = np.linalg.solve(k_global, f_global)
    return displacements

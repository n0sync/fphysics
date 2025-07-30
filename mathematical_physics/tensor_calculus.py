import numpy as np

class Tensor:
    def __init__(self, components, indices_type="covariant"):
        self.components = np.array(components)
        self.indices_type = indices_type
        self.rank = len(self.components.shape)
    
    def __add__(self, other):
        return Tensor(self.components + other.components, self.indices_type)
    
    def __sub__(self, other):
        return Tensor(self.components - other.components, self.indices_type)
    
    def __mul__(self, scalar):
        return Tensor(scalar * self.components, self.indices_type)

def metric_tensor_minkowski(dim=4):
    g = np.zeros((dim, dim))
    g[0, 0] = -1
    for i in range(1, dim):
        g[i, i] = 1
    return g

def christoffel_symbols(metric, coordinates):
    dim = len(coordinates)
    gamma = np.zeros((dim, dim, dim))
    
    for i in range(dim):
        for j in range(dim):
            for k in range(dim):
                for l in range(dim):
                    gamma[i, j, k] += 0.5 * metric[i, l] * (
                        np.gradient(metric[l, j], coordinates[k]) +
                        np.gradient(metric[l, k], coordinates[j]) -
                        np.gradient(metric[j, k], coordinates[l])
                    )
    
    return gamma

def riemann_tensor(christoffel, coordinates):
    dim = christoffel.shape[0]
    R = np.zeros((dim, dim, dim, dim))
    
    for i in range(dim):
        for j in range(dim):
            for k in range(dim):
                for l in range(dim):
                    R[i, j, k, l] = (
                        np.gradient(christoffel[i, j, l], coordinates[k]) -
                        np.gradient(christoffel[i, j, k], coordinates[l])
                    )
                    for m in range(dim):
                        R[i, j, k, l] += (
                            christoffel[i, m, k] * christoffel[m, j, l] -
                            christoffel[i, m, l] * christoffel[m, j, k]
                        )
    
    return R

def ricci_tensor(riemann_tensor):
    dim = riemann_tensor.shape[0]
    R_ij = np.zeros((dim, dim))
    
    for i in range(dim):
        for j in range(dim):
            for k in range(dim):
                R_ij[i, j] += riemann_tensor[k, i, k, j]
    
    return R_ij

def ricci_scalar(ricci_tensor, metric_inverse):
    return np.trace(np.dot(metric_inverse, ricci_tensor))

def einstein_tensor(ricci_tensor, ricci_scalar, metric):
    return ricci_tensor - 0.5 * ricci_scalar * metric

def covariant_derivative(tensor, christoffel, index_position):
    if index_position == "upper":
        return tensor + np.einsum('ijk,k->ij', christoffel, tensor)
    else:
        return tensor - np.einsum('ijk,k->ij', christoffel, tensor)

def tensor_contraction(tensor, indices):
    return np.trace(tensor, axis1=indices[0], axis2=indices[1])

def tensor_product(tensor1, tensor2):
    return np.outer(tensor1.components, tensor2.components)

def levi_civita_symbol(dim):
    epsilon = np.zeros([dim] * dim)
    for i in range(dim):
        for j in range(dim):
            for k in range(dim):
                if i != j and j != k and i != k:
                    if (i - j) * (j - k) * (k - i) > 0:
                        epsilon[i, j, k] = 1
                    else:
                        epsilon[i, j, k] = -1
    return epsilon

def metric_determinant(metric):
    return np.linalg.det(metric)

def raise_index(tensor, metric_inverse):
    return np.dot(metric_inverse, tensor)

def lower_index(tensor, metric):
    return np.dot(metric, tensor)

def parallel_transport(vector, path, christoffel):
    transported = vector.copy()
    for i in range(len(path) - 1):
        dx = path[i+1] - path[i]
        transported -= np.dot(christoffel, transported) * dx
    return transported

def geodesic_equation(christoffel, initial_position, initial_velocity, t_span, dt):
    positions = [initial_position]
    velocities = [initial_velocity]
    
    for t in np.arange(0, t_span, dt):
        pos = positions[-1]
        vel = velocities[-1]
        
        acceleration = -np.einsum('ijk,j,k->i', christoffel, vel, vel)
        
        new_vel = vel + acceleration * dt
        new_pos = pos + vel * dt
        
        positions.append(new_pos)
        velocities.append(new_vel)
    
    return np.array(positions), np.array(velocities)

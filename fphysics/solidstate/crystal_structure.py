import numpy as np
from ..constants import *

def crystal_lattice_volume(a, b, c, alpha, beta, gamma):
    alpha, beta, gamma = np.radians([alpha, beta, gamma])
    cos_alpha, cos_beta, cos_gamma = np.cos([alpha, beta, gamma])
    return a * b * c * np.sqrt(1 + 2*cos_alpha*cos_beta*cos_gamma - 
                               cos_alpha**2 - cos_beta**2 - cos_gamma**2)

def reciprocal_lattice_vectors(a_vec, b_vec, c_vec, volume):
    b1 = 2*PI * np.cross(b_vec, c_vec) / volume
    b2 = 2*PI * np.cross(c_vec, a_vec) / volume
    b3 = 2*PI * np.cross(a_vec, b_vec) / volume
    return b1, b2, b3

def structure_factor(hkl, atoms):
    h, k, l = hkl
    F = 0
    for atom in atoms:
        r_dot_k = 2*PI * (h*atom['x'] + k*atom['y'] + l*atom['z'])
        F += atom['f'] * np.exp(1j * r_dot_k)
    return F

def bravais_lattice_vectors(lattice_type, a, b=None, c=None):
    if b is None: b = a
    if c is None: c = a
    
    if lattice_type == 'cubic':
        return np.array([[a, 0, 0], [0, a, 0], [0, 0, a]])
    elif lattice_type == 'fcc':
        return np.array([[0, a/2, a/2], [a/2, 0, a/2], [a/2, a/2, 0]])
    elif lattice_type == 'bcc':
        return np.array([[-a/2, a/2, a/2], [a/2, -a/2, a/2], [a/2, a/2, -a/2]])
    elif lattice_type == 'hexagonal':
        return np.array([[a, 0, 0], [-a/2, a*np.sqrt(3)/2, 0], [0, 0, c]])
    else:
        raise ValueError(f"Unknown lattice type: {lattice_type}")

def piezoelectric_direct_effect(d_tensor, stress_tensor):
    return np.einsum('ijk,jk->i', d_tensor, stress_tensor)

def piezoelectric_converse_effect(d_tensor, electric_field):
    return np.einsum('kij,k->ij', d_tensor, electric_field)

def piezoelectric_constitutive_charge(d_tensor, stress_tensor, permittivity, electric_field):
    return np.einsum('ijk,jk->i', d_tensor, stress_tensor) + np.dot(permittivity, electric_field)

def piezoelectric_constitutive_strain(compliance, stress_tensor, d_tensor, electric_field):
    return np.einsum('ijkl,kl->ij', compliance, stress_tensor) + np.einsum('kij,k->ij', d_tensor, electric_field)

def piezoelectric_energy_density(compliance, stress_tensor, permittivity, electric_field, d_tensor):
    mechanical_energy = 0.5 * np.einsum('ijkl,ij,kl', compliance, stress_tensor, stress_tensor)
    electrical_energy = 0.5 * np.dot(electric_field, np.dot(permittivity, electric_field))
    coupling_energy = np.einsum('kij,ij,k', d_tensor, stress_tensor, electric_field)
    return mechanical_energy + electrical_energy + coupling_energy

def piezoelectric_coupling_factor(d, permittivity, compliance):
    return d**2 / (permittivity * compliance)

def quartz_oscillator_frequency(length, elastic_modulus, density):
    return np.sqrt(elastic_modulus / density) / (2 * length)

def piezoelectric_charge_constant(d_coefficient, force, area):
    stress = force / area
    return d_coefficient * stress

def piezoelectric_voltage_constant(g_coefficient, stress):
    return g_coefficient * stress

def electromechanical_coupling_matrix(d_tensor, permittivity, compliance):
    K = np.zeros((6, 6))
    K[:3, :3] = compliance[:3, :3]
    K[:3, 3:] = d_tensor.T
    K[3:, :3] = d_tensor
    K[3:, 3:] = -permittivity
    return K

def crystal_symmetry_classes():
    piezoelectric_classes = [1, 2, 3, 4, 6, 23, 222, 32, 422, 622, 
                            4, 6, 432, 3, 4, 6, 43, 6, 3, 23]
    non_piezoelectric_classes = [432, 23, 3, 4, 6]
    return piezoelectric_classes, non_piezoelectric_classes

def miller_indices_distance(hkl, lattice_vectors):
    h, k, l = hkl
    reciprocal_vectors = reciprocal_lattice_vectors(*lattice_vectors, 
                                                   crystal_lattice_volume(*lattice_vectors))
    d_spacing = 2*PI / np.linalg.norm(h*reciprocal_vectors[0] + 
                                      k*reciprocal_vectors[1] + 
                                      l*reciprocal_vectors[2])
    return d_spacing

def bragg_diffraction_condition(d_spacing, wavelength, n=1):
    theta = np.arcsin(n * wavelength / (2 * d_spacing))
    return theta

def debye_temperature(elastic_moduli, density, volume_per_atom):
    avg_velocity = np.mean(np.sqrt(elastic_moduli / density))
    return (HBAR / BOLTZMANN) * (6 * PI**2 / volume_per_atom)**(1/3) * avg_velocity

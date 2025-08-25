import numpy as np
from constants import *

def quantized_charge(n):
    return n * ELEMENTARY_CHARGE
    
# Coulomb's Law
def coulomb_force(q1, q2, r):
    return COULOMB_CONSTANT * q1 * q2 / (r**2)

def coulomb_force_vector(q1, q2, r_vec):
    r = np.linalg.norm(r_vec)
    return COULOMB_CONSTANT * q1 * q2 / (r**3) * r_vec

# Electric Field
def electric_field(q, r):
    return COULOMB_CONSTANT * q / (r**2)

def electric_field_vector(q, r_vec):
    r = np.linalg.norm(r_vec)
    return COULOMB_CONSTANT * q / (r**3) * r_vec

def electric_field_dipole(p, r, theta):
    return COULOMB_CONSTANT * p / (r**3) * np.sqrt(1 + 3 * np.cos(theta)**2)

def electric_field_ring(Q, R, z):
    return COULOMB_CONSTANT * Q * z / (R**2 + z**2)**(3/2)

def electric_field_disk(sigma, R, z):
    return sigma / (2 * VACUUM_PERMITTIVITY) * (1 - z / np.sqrt(R**2 + z**2))

def electric_field_infinite_sheet(sigma):
    return sigma / (2 * VACUUM_PERMITTIVITY)

def electric_field_sphere_inside(rho, r):
    return rho * r / (3 * VACUUM_PERMITTIVITY)

def electric_field_sphere_outside(Q, r):
    return COULOMB_CONSTANT * Q / (r**2)

def electric_field_cylinder(lambda_charge, r):
    return lambda_charge / (2 * PI * VACUUM_PERMITTIVITY * r)

# Electric Potential
def electric_potential(q, r):
    return COULOMB_CONSTANT * q / r

def electric_potential_dipole(p, r, theta):
    return COULOMB_CONSTANT * p * np.cos(theta) / (r**2)

def electric_potential_ring(Q, R, z):
    return COULOMB_CONSTANT * Q / np.sqrt(R**2 + z**2)

def electric_potential_disk(sigma, R, z):
    return sigma / (2 * VACUUM_PERMITTIVITY) * (np.sqrt(R**2 + z**2) - abs(z))

def electric_potential_sphere(Q, r, R):
    if r <= R:
        return COULOMB_CONSTANT * Q / (2 * R) * (3 - (r/R)**2)
    else:
        return COULOMB_CONSTANT * Q / r

# Potential Energy
def potential_energy(q1, q2, r):
    return COULOMB_CONSTANT * q1 * q2 / r

def potential_energy_dipole(p, E):
    return -p * E

def potential_energy_dipole_dipole(p1, p2, r):
    return COULOMB_CONSTANT * p1 * p2 / (r**3)

# Gauss's Law
def gauss_law(q_enclosed):
    return q_enclosed / VACUUM_PERMITTIVITY

def electric_flux(E, A, theta=0):
    return E * A * np.cos(theta)

# Capacitance
def capacitance_parallel_plate(A, d, epsilon_r=1):
    return epsilon_r * VACUUM_PERMITTIVITY * A / d

def capacitance_cylindrical(L, a, b, epsilon_r=1):
    return 2 * PI * epsilon_r * VACUUM_PERMITTIVITY * L / np.log(b/a)

def capacitance_spherical(a, b, epsilon_r=1):
    return 4 * PI * epsilon_r * VACUUM_PERMITTIVITY * a * b / (b - a)

def capacitance_isolated_sphere(R, epsilon_r=1):
    return 4 * PI * epsilon_r * VACUUM_PERMITTIVITY * R

def capacitance_series(C_list):
    return 1 / np.sum(1 / np.array(C_list))

def capacitance_parallel(C_list):
    return np.sum(C_list)

# Energy in Capacitors
def energy_capacitor(C, V=None, Q=None):
    if V is not None:
        return 0.5 * C * V**2
    elif Q is not None:
        return 0.5 * Q**2 / C
    else:
        raise ValueError("Either V or Q must be provided")

def energy_density_electric(E, epsilon_r=1):
    return 0.5 * epsilon_r * VACUUM_PERMITTIVITY * E**2

def energy_electric_field(E, volume, epsilon_r=1):
    return 0.5 * epsilon_r * VACUUM_PERMITTIVITY * E**2 * volume

# Dielectrics
def dielectric_constant(epsilon_r):
    return epsilon_r

def polarization(chi_e, E):
    return chi_e * VACUUM_PERMITTIVITY * E

def bound_charge_density(P):
    return -np.gradient(P)

def bound_surface_charge(P, n_hat):
    return np.dot(P, n_hat)

# Multipole Expansion
def monopole_moment(q):
    return q

def dipole_moment(q, d):
    return q * d

def quadrupole_moment(q, d):
    return q * d**2

def multipole_potential(q_l, r, theta, l):
    return COULOMB_CONSTANT * q_l / (r**(l+1)) * np.cos(l * theta)

# Force and Torque
def force_on_charge(q, E):
    return q * E

def torque_on_dipole(p, E):
    return np.cross(p, E)

def force_on_dipole(p, grad_E):
    return p * grad_E

# Breakdown and Discharge
def breakdown_field_air():
    return 3e6  # V/m

def corona_discharge_field(r):
    return 3e6 * (1 + 0.308 / np.sqrt(r))

# Image Method
def image_charge(q, d):
    return -q

def image_distance(d):
    return d

def image_force(q, d):
    return COULOMB_CONSTANT * q**2 / (16 * d**2)

# Screening and Debye Length
def debye_length(n, T, epsilon_r=1):
    return np.sqrt(epsilon_r * VACUUM_PERMITTIVITY * BOLTZMANN_CONSTANT * T / (n * ELEMENTARY_CHARGE**2))

def screened_potential(q, r, lambda_d):
    return COULOMB_CONSTANT * q / r * np.exp(-r / lambda_d)

# Electrostatic Pressure
def electrostatic_pressure(E, epsilon_r=1):
    return 0.5 * epsilon_r * VACUUM_PERMITTIVITY * E**2

# Method of Images for Sphere
def image_charge_sphere(q, a, d):
    return -q * a / d

def image_position_sphere(a, d):
    return a**2 / d

# Green's Reciprocation
def greens_reciprocation(q1, V2, q2, V1):
    return q1 * V2 - q2 * V1

# Laplace Equation Solutions
def laplace_cartesian_1d(A, B, x):
    return A * x + B

def laplace_cartesian_2d(A, B, C, D, x, y):
    return A * x + B * y + C * x * y + D

def laplace_spherical(A, B, r, l):
    return A * r**l + B * r**(-l-1)

def laplace_cylindrical(A, B, rho, m):
    return A * rho**m + B * rho**(-m)


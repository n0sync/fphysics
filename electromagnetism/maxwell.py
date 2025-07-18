import numpy as np
from constants import *

# Maxwell's Equations in Vacuum
def gauss_law(E, charge_density, epsilon=VACUUM_PERMITTIVITY):
    return np.gradient(E) - charge_density / epsilon

def gauss_law_magnetism(B):
    return np.gradient(B)

def faraday_law(E, B, t):
    return np.gradient(E) + np.gradient(B) / np.gradient(t)

def ampere_maxwell_law(B, J, E, t, mu=VACUUM_PERMEABILITY, epsilon=VACUUM_PERMITTIVITY):
    return np.gradient(B) - mu * J - mu * epsilon * np.gradient(E) / np.gradient(t)

# Maxwell's Equations in Matter
def gauss_law_matter(D, rho_free):
    return np.gradient(D) - rho_free

def gauss_law_magnetism_matter(B):
    return np.gradient(B)

def faraday_law_matter(E, B, t):
    return np.gradient(E) + np.gradient(B) / np.gradient(t)

def ampere_law_matter(H, J_free, D, t):
    return np.gradient(H) - J_free - np.gradient(D) / np.gradient(t)

# Constitutive Relations
def displacement_field(E, P, epsilon=VACUUM_PERMITTIVITY):
    return epsilon * E + P

def magnetic_field_h(B, M, mu=VACUUM_PERMEABILITY):
    return B / mu - M

def current_density_ohm(sigma, E):
    return sigma * E

def polarization_linear(chi_e, E, epsilon=VACUUM_PERMITTIVITY):
    return chi_e * epsilon * E

def magnetization_linear(chi_m, H):
    return chi_m * H

# Electromagnetic Potentials
def electric_field_from_potential(V, A, t):
    return -np.gradient(V) - np.gradient(A) / np.gradient(t)

def magnetic_field_from_potential(A):
    return np.cross(np.gradient(A), A)

def scalar_potential_coulomb(rho, r, epsilon=VACUUM_PERMITTIVITY):
    return rho / (4 * PI * epsilon * r)

def vector_potential_current(J, r, mu=VACUUM_PERMEABILITY):
    return mu * J / (4 * PI * r)

def lorenz_gauge(V, A, c=SPEED_OF_LIGHT):
    return np.gradient(V) / c**2 + np.gradient(A)

def coulomb_gauge(A):
    return np.gradient(A)

# Wave Equations
def wave_equation_electric(E, rho, J, epsilon=VACUUM_PERMITTIVITY, mu=VACUUM_PERMEABILITY):
    c = 1 / np.sqrt(epsilon * mu)
    return np.gradient(np.gradient(E)) - (1/c**2) * np.gradient(np.gradient(E)) - \
           mu * np.gradient(J) - np.gradient(rho) / epsilon

def wave_equation_magnetic(B, J, mu=VACUUM_PERMEABILITY, epsilon=VACUUM_PERMITTIVITY):
    c = 1 / np.sqrt(epsilon * mu)
    return np.gradient(np.gradient(B)) - (1/c**2) * np.gradient(np.gradient(B)) - \
           mu * np.cross(np.gradient(J), B)

def wave_equation_potential_scalar(V, rho, epsilon=VACUUM_PERMITTIVITY, mu=VACUUM_PERMEABILITY):
    c = 1 / np.sqrt(epsilon * mu)
    return np.gradient(np.gradient(V)) - (1/c**2) * np.gradient(np.gradient(V)) - rho / epsilon

def wave_equation_potential_vector(A, J, epsilon=VACUUM_PERMITTIVITY, mu=VACUUM_PERMEABILITY):
    c = 1 / np.sqrt(epsilon * mu)
    return np.gradient(np.gradient(A)) - (1/c**2) * np.gradient(np.gradient(A)) - mu * J

# Boundary Conditions
def boundary_condition_normal_e(E1_perp, E2_perp, sigma, epsilon=VACUUM_PERMITTIVITY):
    return E1_perp - E2_perp - sigma / epsilon

def boundary_condition_tangential_e(E1_tan, E2_tan):
    return E1_tan - E2_tan

def boundary_condition_normal_b(B1_perp, B2_perp):
    return B1_perp - B2_perp

def boundary_condition_tangential_b(B1_tan, B2_tan, K, mu=VACUUM_PERMEABILITY):
    return B1_tan - B2_tan - mu * K

def boundary_condition_normal_d(D1_perp, D2_perp, sigma_free):
    return D1_perp - D2_perp - sigma_free

def boundary_condition_tangential_h(H1_tan, H2_tan, K_free):
    return H1_tan - H2_tan - K_free

# Energy and Momentum
def electromagnetic_energy_density(E, B, epsilon=VACUUM_PERMITTIVITY, mu=VACUUM_PERMEABILITY):
    return 0.5 * (epsilon * E**2 + B**2 / mu)

def electromagnetic_momentum_density(E, B, c=SPEED_OF_LIGHT):
    return np.cross(E, B) / c**2

def poynting_vector(E, B, mu=VACUUM_PERMEABILITY):
    return np.cross(E, B) / mu

def maxwell_stress_tensor(E, B, epsilon=VACUUM_PERMITTIVITY, mu=VACUUM_PERMEABILITY):
    I = np.eye(3)
    return epsilon * (np.outer(E, E) - 0.5 * np.dot(E, E) * I) + \
           (1/mu) * (np.outer(B, B) - 0.5 * np.dot(B, B) * I)

# Electromagnetic Force
def lorentz_force_density(rho, E, J, B):
    return rho * E + np.cross(J, B)

def electromagnetic_force_field(E, B, epsilon=VACUUM_PERMITTIVITY, mu=VACUUM_PERMEABILITY):
    return -np.gradient(electromagnetic_energy_density(E, B, epsilon, mu))

# Radiation
def larmor_formula(q, a, c=SPEED_OF_LIGHT, epsilon=VACUUM_PERMITTIVITY):
    return q**2 * a**2 / (6 * PI * epsilon * c**3)

def radiated_power_accelerating_charge(q, a, c=SPEED_OF_LIGHT, epsilon=VACUUM_PERMITTIVITY):
    return q**2 * a**2 / (6 * PI * epsilon * c**3)

def radiation_reaction_force(q, a_dot, c=SPEED_OF_LIGHT, epsilon=VACUUM_PERMITTIVITY):
    return q**2 * a_dot / (6 * PI * epsilon * c**3)

def synchrotron_power(q, B, v, m, c=SPEED_OF_LIGHT, epsilon=VACUUM_PERMITTIVITY):
    gamma = 1 / np.sqrt(1 - v**2 / c**2)
    return q**4 * B**2 * v**2 * gamma**2 / (6 * PI * epsilon * m**2 * c**3)

# Retarded Potentials
def retarded_time(t, r, c=SPEED_OF_LIGHT):
    return t - r / c

def retarded_scalar_potential(q, r, v, c=SPEED_OF_LIGHT, epsilon=VACUUM_PERMITTIVITY):
    return q / (4 * PI * epsilon * r * (1 - np.dot(v, r) / (c * r)))

def retarded_vector_potential(q, v, r, c=SPEED_OF_LIGHT, epsilon=VACUUM_PERMITTIVITY):
    return q * v / (4 * PI * epsilon * c * r * (1 - np.dot(v, r) / (c * r)))

# Multipole Radiation
def electric_dipole_moment(q, r):
    return q * r

def magnetic_dipole_moment(I, A):
    return I * A

def electric_quadrupole_moment(q, r):
    return q * np.outer(r, r)

def dipole_radiation_power(p_dot, c=SPEED_OF_LIGHT, epsilon=VACUUM_PERMITTIVITY):
    return np.dot(p_dot, p_dot) / (6 * PI * epsilon * c**3)

def quadrupole_radiation_power(Q_ddot, c=SPEED_OF_LIGHT, epsilon=VACUUM_PERMITTIVITY):
    return np.trace(np.dot(Q_ddot, Q_ddot)) / (180 * PI * epsilon * c**5)

# Plasma Oscillations
def plasma_frequency(n, m=ELECTRON_MASS, q=ELEMENTARY_CHARGE, epsilon=VACUUM_PERMITTIVITY):
    return np.sqrt(n * q**2 / (epsilon * m))

def debye_length(n, T, q=ELEMENTARY_CHARGE, epsilon=VACUUM_PERMITTIVITY):
    return np.sqrt(epsilon * BOLTZMANN_CONSTANT * T / (n * q**2))

def plasma_parameter(n, T, q=ELEMENTARY_CHARGE, epsilon=VACUUM_PERMITTIVITY):
    lambda_d = debye_length(n, T, q, epsilon)
    return (4 * PI * n * lambda_d**3) / 3

# Dielectric Function
def dielectric_function_plasma(omega, omega_p, gamma=0):
    return 1 - omega_p**2 / (omega**2 + 1j * gamma * omega)

def dielectric_function_drude(omega, omega_p, gamma):
    return 1 - omega_p**2 / (omega**2 + 1j * gamma * omega)

def dielectric_function_lorentz(omega, omega_0, omega_p, gamma):
    return 1 + omega_p**2 / (omega_0**2 - omega**2 - 1j * gamma * omega)

# Magnetic Reconnection
def magnetic_reynolds_number(v, L, eta):
    return v * L / eta

def reconnection_rate(v_in, v_a):
    return v_in / v_a

def sweet_parker_rate(S):
    return 1 / np.sqrt(S)

# Electromagnetic Induction
def faraday_emf(B, A, t):
    return -np.gradient(B * A) / np.gradient(t)

def motional_emf(v, B, L):
    return np.dot(np.cross(v, B), L)

def transformer_emf(N, B, A, t):
    return -N * np.gradient(B * A) / np.gradient(t)

def self_induced_emf(L, I, t):
    return -L * np.gradient(I) / np.gradient(t)

def mutual_induced_emf(M, I, t):
    return -M * np.gradient(I) / np.gradient(t)

# Electromagnetic Waves in Media
def wave_equation_dielectric(E, epsilon_r, mu_r=1, c=SPEED_OF_LIGHT):
    v = c / np.sqrt(epsilon_r * mu_r)
    return np.gradient(np.gradient(E)) - (1/v**2) * np.gradient(np.gradient(E))

def wave_equation_conducting(E, sigma, epsilon=VACUUM_PERMITTIVITY, mu=VACUUM_PERMEABILITY):
    return np.gradient(np.gradient(E)) - mu * sigma * np.gradient(E) - \
           mu * epsilon * np.gradient(np.gradient(E))

def skin_depth(sigma, omega, mu=VACUUM_PERMEABILITY):
    return np.sqrt(2 / (sigma * omega * mu))

def penetration_depth(sigma, omega, mu=VACUUM_PERMEABILITY):
    return 1 / np.sqrt(sigma * omega * mu / 2)

# Metamaterial Properties
def effective_permittivity(epsilon_host, epsilon_inclusion, f):
    return epsilon_host * (1 + 2 * f * (epsilon_inclusion - epsilon_host) / 
                          (epsilon_inclusion + 2 * epsilon_host - f * (epsilon_inclusion - epsilon_host)))

def effective_permeability(mu_host, mu_inclusion, f):
    return mu_host * (1 + 2 * f * (mu_inclusion - mu_host) / 
                     (mu_inclusion + 2 * mu_host - f * (mu_inclusion - mu_host)))

def negative_index_condition(epsilon_eff, mu_eff):
    return epsilon_eff < 0 and mu_eff < 0

def metamaterial_impedance(epsilon_eff, mu_eff):
    return np.sqrt(mu_eff / epsilon_eff)

# Nonlinear Electromagnetic Effects
def ponderomotive_force(q, E, omega, m):
    return -q**2 * np.gradient(E**2) / (4 * m * omega**2)

def second_harmonic_coefficient(chi2, E):
    return chi2 * E**2

def third_harmonic_coefficient(chi3, E):
    return chi3 * E**3

def kerr_nonlinearity(n0, n2, I):
    return n0 + n2 * I

def optical_kerr_effect(n0, n2, E):
    return n0 + n2 * E**2

# Relativistic Electromagnetism
def electromagnetic_field_tensor(E, B, c=SPEED_OF_LIGHT):
    F = np.zeros((4, 4))
    F[0, 1:4] = E / c
    F[1:4, 0] = -E / c
    F[1, 2] = B[2]
    F[2, 1] = -B[2]
    F[1, 3] = -B[1]
    F[3, 1] = B[1]
    F[2, 3] = B[0]
    F[3, 2] = -B[0]
    return F

def four_current(rho, J, c=SPEED_OF_LIGHT):
    return np.array([rho * c, J[0], J[1], J[2]])

def four_potential(V, A, c=SPEED_OF_LIGHT):
    return np.array([V / c, A[0], A[1], A[2]])

def lorentz_invariant_i(E, B, c=SPEED_OF_LIGHT):
    return (E**2 / c**2 - B**2)

def lorentz_invariant_ii(E, B, c=SPEED_OF_LIGHT):
    return np.dot(E, B) / c

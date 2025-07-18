import numpy as np
from constants import *

# Magnetic Force
def magnetic_force(q, v, B):
    return q * np.cross(v, B)

def magnetic_force_current(I, L, B):
    return I * np.cross(L, B)

def magnetic_force_between_wires(I1, I2, L, d):
    return VACUUM_PERMEABILITY * I1 * I2 * L / (2 * PI * d)

def lorentz_force(q, E, v, B):
    return q * (E + np.cross(v, B))

# Biot-Savart Law
def biot_savart(I, dl, r_vec):
    r = np.linalg.norm(r_vec)
    return VACUUM_PERMEABILITY * I / (4 * PI) * np.cross(dl, r_vec) / (r**3)

def magnetic_field_straight_wire(I, r):
    return VACUUM_PERMEABILITY * I / (2 * PI * r)

def magnetic_field_infinite_wire(I, r):
    return VACUUM_PERMEABILITY * I / (2 * PI * r)

def magnetic_field_finite_wire(I, a, b, r):
    return VACUUM_PERMEABILITY * I / (4 * PI * r) * (b / np.sqrt(b**2 + r**2) - a / np.sqrt(a**2 + r**2))

def magnetic_field_circular_loop(I, R, z):
    return VACUUM_PERMEABILITY * I * R**2 / (2 * (R**2 + z**2)**(3/2))

def magnetic_field_circular_loop_center(I, R):
    return VACUUM_PERMEABILITY * I / (2 * R)

def magnetic_field_arc(I, R, theta):
    return VACUUM_PERMEABILITY * I * theta / (4 * PI * R)

# Solenoid and Coils
def magnetic_field_solenoid(n, I):
    return VACUUM_PERMEABILITY * n * I

def magnetic_field_solenoid_finite(I, N, L, r, z):
    return VACUUM_PERMEABILITY * I * N / (2 * L) * (z / np.sqrt(z**2 + r**2))

def magnetic_field_toroidal(N, I, r):
    return VACUUM_PERMEABILITY * N * I / (2 * PI * r)

def magnetic_field_helmholtz(I, R, d):
    return 8 * VACUUM_PERMEABILITY * I * R**2 / (5**(3/2) * (R**2 + d**2/4)**(3/2))

# Magnetic Dipole
def magnetic_dipole_moment(I, A):
    return I * A

def magnetic_field_dipole(m, r, theta):
    return VACUUM_PERMEABILITY * m / (4 * PI * r**3) * np.sqrt(1 + 3 * np.cos(theta)**2)

def magnetic_field_dipole_axial(m, r):
    return VACUUM_PERMEABILITY * m / (2 * PI * r**3)

def magnetic_field_dipole_equatorial(m, r):
    return VACUUM_PERMEABILITY * m / (4 * PI * r**3)

# Ampère's Law
def ampere_law(I_enclosed):
    return VACUUM_PERMEABILITY * I_enclosed

def magnetic_circulation(B, dl):
    return np.dot(B, dl)

# Magnetic Flux
def magnetic_flux(B, A, theta=0):
    return B * A * np.cos(theta)

def magnetic_flux_density(Phi, A):
    return Phi / A

# Magnetic Materials
def magnetization(chi_m, H):
    return chi_m * H

def magnetic_susceptibility(mu_r):
    return mu_r - 1

def relative_permeability(chi_m):
    return 1 + chi_m

def magnetic_field_H(B, M):
    return B / VACUUM_PERMEABILITY - M

def magnetic_field_B(H, M):
    return VACUUM_PERMEABILITY * (H + M)

# Boundary Conditions
def boundary_normal_B(B1_n, B2_n):
    return B1_n - B2_n

def boundary_tangential_H(H1_t, H2_t, K_f):
    return H1_t - H2_t - K_f

# Magnetic Energy
def magnetic_energy_density(B, mu_r=1):
    return B**2 / (2 * mu_r * VACUUM_PERMEABILITY)

def magnetic_energy_inductor(L, I):
    return 0.5 * L * I**2

def magnetic_energy_field(B, volume, mu_r=1):
    return B**2 * volume / (2 * mu_r * VACUUM_PERMEABILITY)

# Inductance
def self_inductance_solenoid(N, A, L, mu_r=1):
    return mu_r * VACUUM_PERMEABILITY * N**2 * A / L

def self_inductance_toroidal(N, A, r_mean, mu_r=1):
    return mu_r * VACUUM_PERMEABILITY * N**2 * A / (2 * PI * r_mean)

def mutual_inductance(Phi_12, I_1):
    return Phi_12 / I_1

def inductance_parallel(L_list):
    return 1 / np.sum(1 / np.array(L_list))

def inductance_series(L_list):
    return np.sum(L_list)

# Vector Potential
def vector_potential_wire(I, r):
    return -VACUUM_PERMEABILITY * I / (2 * PI) * np.log(r)

def vector_potential_dipole(m, r):
    return VACUUM_PERMEABILITY * m / (4 * PI * r**2)

# Magnetic Monopole (Hypothetical)
def magnetic_monopole_field(q_m, r):
    return q_m / (4 * PI * VACUUM_PERMEABILITY * r**2)

# Cyclotron Motion
def cyclotron_frequency(q, B, m):
    return q * B / m

def cyclotron_radius(m, v, q, B):
    return m * v / (q * B)

def cyclotron_period(m, q, B):
    return 2 * PI * m / (q * B)

# Hall Effect
def hall_voltage(I, B, t, n, q):
    return I * B / (n * q * t)

def hall_coefficient(n, q):
    return 1 / (n * q)

def hall_mobility(sigma, n, q):
    return sigma / (n * q)

# Magnetic Pressure
def magnetic_pressure(B, mu_r=1):
    return B**2 / (2 * mu_r * VACUUM_PERMEABILITY)

# Demagnetization
def demagnetization_factor_sphere():
    return 1/3

def demagnetization_factor_cylinder_transverse():
    return 1/2

def demagnetization_factor_cylinder_longitudinal():
    return 0

# Magnetic Circuits
def magnetic_reluctance(L, mu, A):
    return L / (mu * A)

def magnetomotive_force(N, I):
    return N * I

def magnetic_ohms_law(mmf, reluctance):
    return mmf / reluctance

# Hysteresis
def coercivity(H_c):
    return H_c

def remanence(B_r):
    return B_r

def saturation_magnetization(M_s):
    return M_s

def hysteresis_loss(B_max, H_c, volume):
    return 2 * B_max * H_c * volume

# Eddy Currents
def eddy_current_loss(k, B_max, f, t):
    return k * B_max**2 * f**2 * t**2

# Magnetic Shielding
def shielding_factor(mu_r, t, R):
    return mu_r * t / R

# Magnetic Levitation
def magnetic_levitation_force(m, g, B, grad_B):
    return -m * B * grad_B

# Zeeman Effect
def zeeman_splitting(mu_B, g, B):
    return mu_B * g * B

# Spin Magnetic Moment
def spin_magnetic_moment(g, mu_B, S):
    return g * mu_B * S

def orbital_magnetic_moment(mu_B, L):
    return mu_B * L

# Superconductivity
def london_penetration_depth(m, n_s, q, mu_0):
    return np.sqrt(m / (mu_0 * n_s * q**2))

def critical_field(T, T_c, B_c0):
    return B_c0 * (1 - (T/T_c)**2)

# Magnetization Curves
def langevin_function(x):
    return 1/np.tanh(x) - 1/x

def brillouin_function(J, x):
    return (2*J+1)/(2*J) * 1/np.tanh((2*J+1)*x/(2*J)) - 1/(2*J) * 1/np.tanh(x/(2*J))

# Curie Law
def curie_law(C, T):
    return C / T

def curie_weiss_law(C, T, theta):
    return C / (T - theta)

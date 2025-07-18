import numpy as np
from constants import *

# Wave Equation
def wave_equation_1d(A, k, omega, x, t, phi=0):
    return A * np.cos(k * x - omega * t + phi)

def wave_equation_3d(A, k_vec, r_vec, omega, t, phi=0):
    return A * np.cos(np.dot(k_vec, r_vec) - omega * t + phi)

def wave_number(wavelength):
    return 2 * PI / wavelength

def angular_frequency(frequency):
    return 2 * PI * frequency

def wave_velocity(wavelength, frequency):
    return wavelength * frequency

def wave_velocity_dispersion(omega, k):
    return omega / k

def group_velocity(omega, k):
    return np.gradient(omega) / np.gradient(k)

# Electromagnetic Wave Properties
def electromagnetic_wave_velocity():
    return SPEED_OF_LIGHT

def electromagnetic_wave_impedance():
    return np.sqrt(VACUUM_PERMEABILITY / VACUUM_PERMITTIVITY)

def refractive_index(epsilon_r, mu_r=1):
    return np.sqrt(epsilon_r * mu_r)

def phase_velocity(c, n):
    return c / n

def wavelength_in_medium(wavelength_vacuum, n):
    return wavelength_vacuum / n

def frequency_in_medium(frequency_vacuum):
    return frequency_vacuum

# Electric and Magnetic Fields
def electric_field_wave(E0, k, omega, x, t, phi=0):
    return E0 * np.cos(k * x - omega * t + phi)

def magnetic_field_wave(B0, k, omega, x, t, phi=0):
    return B0 * np.cos(k * x - omega * t + phi)

def field_relationship_em_wave(E0, c=SPEED_OF_LIGHT, Z0=None):
    if Z0 is None:
        Z0 = np.sqrt(VACUUM_PERMEABILITY / VACUUM_PERMITTIVITY)
    return E0 / (c * Z0)

def poynting_vector(E, B, mu=VACUUM_PERMEABILITY):
    return np.cross(E, B) / mu

def energy_density_electromagnetic(E, B, epsilon=VACUUM_PERMITTIVITY, mu=VACUUM_PERMEABILITY):
    return 0.5 * (epsilon * E**2 + B**2 / mu)

def energy_density_electric(E, epsilon=VACUUM_PERMITTIVITY):
    return 0.5 * epsilon * E**2

def energy_density_magnetic(B, mu=VACUUM_PERMEABILITY):
    return 0.5 * B**2 / mu

# Intensity and Power
def intensity_electromagnetic(E0, c=SPEED_OF_LIGHT, epsilon=VACUUM_PERMITTIVITY):
    return 0.5 * c * epsilon * E0**2

def intensity_from_poynting(S):
    return np.mean(S)

def power_transmitted(I, A):
    return I * A

def radiation_pressure(I, c=SPEED_OF_LIGHT):
    return I / c

def radiation_pressure_absorption(I, c=SPEED_OF_LIGHT):
    return I / c

def radiation_pressure_reflection(I, c=SPEED_OF_LIGHT):
    return 2 * I / c

# Polarization
def linear_polarization(E0, theta, phi=0):
    return E0 * np.array([np.cos(theta), np.sin(theta), 0])

def circular_polarization(E0, handedness=1):
    return E0 / np.sqrt(2) * np.array([1, handedness * 1j, 0])

def elliptical_polarization(E0x, E0y, delta):
    return np.array([E0x, E0y * np.exp(1j * delta), 0])

def degree_of_polarization(I_max, I_min):
    return (I_max - I_min) / (I_max + I_min)

def malus_law(I0, theta):
    return I0 * np.cos(theta)**2

def brewster_angle(n1, n2):
    return np.arctan(n2 / n1)

# Plane Wave Solutions
def plane_wave_electric(E0, k, omega, r, t, phi=0):
    return E0 * np.exp(1j * (k * r - omega * t + phi))

def plane_wave_magnetic(B0, k, omega, r, t, phi=0):
    return B0 * np.exp(1j * (k * r - omega * t + phi))

def spherical_wave(A, k, r, omega, t, phi=0):
    return A / r * np.exp(1j * (k * r - omega * t + phi))

def cylindrical_wave(A, k, rho, omega, t, phi=0):
    return A / np.sqrt(rho) * np.exp(1j * (k * rho - omega * t + phi))

# Reflection and Transmission
def reflection_coefficient_normal(n1, n2):
    return (n1 - n2) / (n1 + n2)

def transmission_coefficient_normal(n1, n2):
    return 2 * n1 / (n1 + n2)

def reflectance_normal(n1, n2):
    r = reflection_coefficient_normal(n1, n2)
    return r**2

def transmittance_normal(n1, n2):
    t = transmission_coefficient_normal(n1, n2)
    return (n2 / n1) * t**2

def fresnel_r_s(n1, n2, theta1, theta2):
    return (n1 * np.cos(theta1) - n2 * np.cos(theta2)) / (n1 * np.cos(theta1) + n2 * np.cos(theta2))

def fresnel_r_p(n1, n2, theta1, theta2):
    return (n2 * np.cos(theta1) - n1 * np.cos(theta2)) / (n2 * np.cos(theta1) + n1 * np.cos(theta2))

def fresnel_t_s(n1, n2, theta1, theta2):
    return (2 * n1 * np.cos(theta1)) / (n1 * np.cos(theta1) + n2 * np.cos(theta2))

def fresnel_t_p(n1, n2, theta1, theta2):
    return (2 * n1 * np.cos(theta1)) / (n2 * np.cos(theta1) + n1 * np.cos(theta2))

# Total Internal Reflection
def critical_angle(n1, n2):
    if n1 <= n2:
        return None
    return np.arcsin(n2 / n1)

def evanescent_wave_decay(k, n1, n2, theta, z):
    if n1 * np.sin(theta) > n2:
        gamma = k * np.sqrt((n1 * np.sin(theta))**2 - n2**2)
        return np.exp(-gamma * z)
    return 1

# Dispersion
def group_velocity_dispersion(omega, k):
    return np.gradient(np.gradient(omega)) / np.gradient(k)**2

def sellmeier_equation(wavelength, B1, B2, B3, C1, C2, C3):
    lam2 = wavelength**2
    n2 = 1 + B1 * lam2 / (lam2 - C1) + B2 * lam2 / (lam2 - C2) + B3 * lam2 / (lam2 - C3)
    return np.sqrt(n2)

def cauchy_equation(wavelength, A, B, C=0):
    return A + B / wavelength**2 + C / wavelength**4

def abbe_number(n_d, n_f, n_c):
    return (n_d - 1) / (n_f - n_c)

# Waveguides
def rectangular_waveguide_cutoff(a, b, m, n):
    return (SPEED_OF_LIGHT / 2) * np.sqrt((m / a)**2 + (n / b)**2)

def circular_waveguide_cutoff(a, x_mn):
    return SPEED_OF_LIGHT * x_mn / (2 * PI * a)

def waveguide_wavelength(lambda0, lambda_c):
    return lambda0 / np.sqrt(1 - (lambda0 / lambda_c)**2)

def waveguide_phase_velocity(c, lambda0, lambda_c):
    return c / np.sqrt(1 - (lambda0 / lambda_c)**2)

def waveguide_group_velocity(c, lambda0, lambda_c):
    return c * np.sqrt(1 - (lambda0 / lambda_c)**2)

# Antenna Theory
def dipole_radiation_pattern(theta):
    return np.sin(theta)**2

def dipole_radiation_resistance():
    return 73.1

def antenna_gain(directivity, efficiency):
    return directivity * efficiency

def friis_transmission_equation(P_t, G_t, G_r, wavelength, R):
    return P_t * G_t * G_r * (wavelength / (4 * PI * R))**2

def effective_aperture(G, wavelength):
    return G * wavelength**2 / (4 * PI)

# Blackbody Radiation
def planck_distribution(wavelength, T):
    return (2 * PLANCK_CONSTANT * SPEED_OF_LIGHT**2 / wavelength**5) / \
           (np.exp(PLANCK_CONSTANT * SPEED_OF_LIGHT / (wavelength * BOLTZMANN_CONSTANT * T)) - 1)

def wien_displacement_law(T):
    return WIEN_DISPLACEMENT_CONSTANT / T

def stefan_boltzmann_law(T):
    return STEFAN_BOLTZMANN_CONSTANT * T**4

def rayleigh_jeans_law(wavelength, T):
    return (2 * SPEED_OF_LIGHT * BOLTZMANN_CONSTANT * T) / wavelength**4

# Doppler Effect
def doppler_shift_classical(f0, v, c=SPEED_OF_LIGHT):
    return f0 * (1 + v / c)

def doppler_shift_relativistic(f0, v, c=SPEED_OF_LIGHT):
    gamma = 1 / np.sqrt(1 - v**2 / c**2)
    return f0 * gamma * (1 + v / c)

def doppler_broadening(f0, T, m):
    return f0 * np.sqrt(2 * BOLTZMANN_CONSTANT * T / (m * SPEED_OF_LIGHT**2))

# Coherence
def coherence_length(lambda0, delta_lambda):
    return lambda0**2 / delta_lambda

def coherence_time(delta_f):
    return 1 / delta_f

def visibility(I_max, I_min):
    return (I_max - I_min) / (I_max + I_min)

def degree_of_coherence(I1, I2, I12):
    return I12 / np.sqrt(I1 * I2)

# Nonlinear Optics
def second_harmonic_generation(I_fundamental, chi2, L):
    return I_fundamental**2 * chi2**2 * L**2

def third_harmonic_generation(I_fundamental, chi3, L):
    return I_fundamental**3 * chi3**2 * L**2

def kerr_effect(n0, n2, I):
    return n0 + n2 * I

def self_focusing_power(wavelength, n0, n2):
    return PI * (0.61 * wavelength)**2 / (8 * n0 * n2)

# Pulse Propagation
def pulse_broadening_gvd(tau0, beta2, z):
    return tau0 * np.sqrt(1 + (beta2 * z / tau0**2)**2)

def dispersion_length(tau0, beta2):
    return tau0**2 / abs(beta2)

def nonlinear_length(gamma, P0):
    return 1 / (gamma * P0)

def soliton_number(gamma, P0, tau0, beta2):
    return np.sqrt(gamma * P0 * tau0**2 / abs(beta2))

# Plasma Physics
def plasma_frequency(n_e, m_e=ELECTRON_MASS):
    return np.sqrt(n_e * ELEMENTARY_CHARGE**2 / (VACUUM_PERMITTIVITY * m_e))

def plasma_wavelength(n_e, m_e=ELECTRON_MASS):
    return 2 * PI * SPEED_OF_LIGHT / plasma_frequency(n_e, m_e)

def cyclotron_frequency_plasma(B, m=ELECTRON_MASS):
    return ELEMENTARY_CHARGE * B / m

def alfven_velocity(B, rho, mu=VACUUM_PERMEABILITY):
    return B / np.sqrt(mu * rho)

# Metamaterials
def negative_refractive_index(epsilon_eff, mu_eff):
    return -np.sqrt(epsilon_eff * mu_eff)

def metamaterial_impedance(mu_eff, epsilon_eff):
    return np.sqrt(mu_eff / epsilon_eff)

def backward_wave_phase_velocity(omega, k):
    return -omega / k

def backward_wave_group_velocity(omega, k):
    return np.gradient(omega) / np.gradient(k)

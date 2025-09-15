import numpy as np
from ..constants import *

# Refractive Index Functions
def sellmeier_equation(wavelength, B1, B2, B3, C1, C2, C3):
    wl2 = wavelength**2
    n2 = 1 + (B1*wl2)/(wl2-C1) + (B2*wl2)/(wl2-C2) + (B3*wl2)/(wl2-C3)
    return np.sqrt(n2)

def cauchy_equation(wavelength, A, B, C=0):
    return A + B/(wavelength**2) + C/(wavelength**4)

def temperature_coefficient_dn_dt(n0, temp, alpha, beta=0):
    return n0 + alpha*(temp - 20) + beta*(temp - 20)**2

def thermo_optic_coefficient(wavelength, temp, dn_dt_coeff):
    return dn_dt_coeff * (temp - 293.15)

def pressure_coefficient_dn_dp(n0, pressure, gamma):
    return n0 * (1 + gamma * pressure)

# Dispersion Properties
def group_velocity_dispersion(wavelength, d2n_dlambda2):
    return -(wavelength**3 * d2n_dlambda2) / (2*np.pi*SPEED_OF_LIGHT)

def material_dispersion(wavelength, n, dn_dlambda, d2n_dlambda2):
    return -(wavelength / SPEED_OF_LIGHT) * d2n_dlambda2

def chromatic_dispersion(wavelength, n_blue, n_red, lambda_blue, lambda_red):
    return (n_blue - n_red) / (lambda_blue - lambda_red)

def abbe_number(n_d, n_f, n_c):
    return (n_d - 1) / (n_f - n_c)

def partial_dispersion_ratio(n_g, n_f, n_c):
    return (n_g - n_f) / (n_f - n_c)

# Absorption and Transmission
def beer_lambert_law(intensity_0, absorption_coeff, thickness):
    return intensity_0 * np.exp(-absorption_coeff * thickness)

def absorption_coefficient(transmittance, thickness):
    return -np.log(transmittance) / thickness

def extinction_coefficient(absorption_coeff, wavelength):
    return absorption_coeff * wavelength / (4 * np.pi)

def penetration_depth(absorption_coeff):
    return 1 / absorption_coeff

def optical_density(transmittance):
    return -np.log10(transmittance)

# Mechanical Properties
def youngs_modulus_temperature(E0, temp, alpha_E):
    return E0 * (1 + alpha_E * (temp - 293.15))

def poisson_ratio_stress(nu0, stress, beta_nu):
    return nu0 + beta_nu * stress

def thermal_expansion_coefficient(length, temp, alpha_thermal):
    return alpha_thermal * (temp - 293.15)

def stress_optic_coefficient(delta_n, stress):
    return delta_n / stress

def photoelastic_constant(n0, stress_optic_coeff):
    return stress_optic_coeff / n0

# Thermal Properties
def thermal_conductivity_temperature(k0, temp, alpha_k):
    return k0 * (1 + alpha_k * (temp - 293.15))

def specific_heat_temperature(cp0, temp, alpha_cp):
    return cp0 * (1 + alpha_cp * (temp - 293.15))

def thermal_diffusivity(thermal_conductivity, density, specific_heat):
    return thermal_conductivity / (density * specific_heat)

def thermal_shock_parameter(thermal_conductivity, tensile_strength, 
                          thermal_expansion, youngs_modulus):
    return (thermal_conductivity * tensile_strength) / \
           (thermal_expansion * youngs_modulus)

def coefficient_thermal_expansion(strain, delta_temp):
    return strain / delta_temp

# Electrical Properties
def electrical_conductivity_temperature(sigma0, temp, alpha_sigma):
    return sigma0 * (1 + alpha_sigma * (temp - 293.15))

def dielectric_constant_frequency(eps_inf, eps_s, freq, tau):
    omega = 2 * np.pi * freq
    return eps_inf + (eps_s - eps_inf) / (1 + 1j * omega * tau)

def loss_tangent(eps_real, eps_imag):
    return eps_imag / eps_real

def breakdown_voltage(thickness, dielectric_strength):
    return dielectric_strength * thickness

def resistivity_temperature(rho0, temp, alpha_rho):
    return rho0 * (1 + alpha_rho * (temp - 293.15))

# Nonlinear Optical Properties
def kerr_effect(n0, intensity, n2):
    return n0 + n2 * intensity

def two_photon_absorption(intensity, beta_2PA):
    return beta_2PA * intensity

def self_focusing_critical_power(wavelength, n0, n2):
    return (3.77 * wavelength**2) / (8 * np.pi * n0 * n2)

def nonlinear_phase_shift(intensity, n2, length):
    return (2 * np.pi / WAVELENGTH_VACUUM) * n2 * intensity * length

def third_order_susceptibility(n0, n2):
    return (4 * n0**2 * n2) / (3 * EPSILON_0 * SPEED_OF_LIGHT)

# Surface Properties
def surface_roughness_scattering(roughness, wavelength, angle):
    return (4 * np.pi * roughness * np.cos(angle) / wavelength)**2

def contact_angle(surface_tension_lv, surface_tension_sv, surface_tension_sl):
    return np.arccos((surface_tension_sv - surface_tension_sl) / surface_tension_lv)

def surface_energy(contact_angle, liquid_surface_tension):
    return liquid_surface_tension * np.cos(contact_angle)

def adhesion_work(surface_tension_1, surface_tension_2, interfacial_tension):
    return surface_tension_1 + surface_tension_2 - interfacial_tension

def spreading_coefficient(surface_tension_lv, surface_tension_sv, surface_tension_sl):
    return surface_tension_sv - surface_tension_lv - surface_tension_sl

# Crystal Properties
def miller_indices_spacing(a, h, k, l):
    return a / np.sqrt(h**2 + k**2 + l**2)

def bragg_law(n, wavelength, d, theta):
    return n * wavelength == 2 * d * np.sin(theta)

def crystal_field_splitting(wavelength_transition):
    return PLANCK_CONSTANT * SPEED_OF_LIGHT / wavelength_transition

def lattice_parameter_temperature(a0, temp, alpha_lattice):
    return a0 * (1 + alpha_lattice * (temp - 293.15))

def piezoelectric_coefficient(strain, electric_field):
    return strain / electric_field

# Defects and Impurities
def color_center_absorption(oscillator_strength, concentration, line_width):
    return (oscillator_strength * concentration) / line_width

def dopant_concentration_absorption(absorption_coeff, cross_section):
    return absorption_coeff / cross_section

def defect_density_luminescence(luminescence_intensity, quantum_efficiency):
    return luminescence_intensity / quantum_efficiency

def vacancy_concentration_diffusion(diffusion_coeff, temp, activation_energy):
    return diffusion_coeff * np.exp(-activation_energy / (BOLTZMANN_CONSTANT * temp))

def impurity_level_energy(wavelength_emission, wavelength_absorption):
    return PLANCK_CONSTANT * SPEED_OF_LIGHT * (1/wavelength_emission - 1/wavelength_absorption)

# Phase Transitions
def glass_transition_viscosity(temp, tg, fragility):
    return np.exp(fragility * tg / (temp - tg))

def melting_point_pressure(tm0, pressure, dp_dt_slope):
    return tm0 + dp_dt_slope * pressure

def phase_transition_enthalpy(temp, transition_temp, delta_cp):
    return delta_cp * (temp - transition_temp)

def crystallization_rate(temp, activation_energy, pre_exponential):
    return pre_exponential * np.exp(-activation_energy / (BOLTZMANN_CONSTANT * temp))

def nucleation_rate(temp, surface_energy, volume_free_energy):
    barrier = (16 * np.pi * surface_energy**3) / (3 * volume_free_energy**2)
    return np.exp(-barrier / (BOLTZMANN_CONSTANT * temp))

# Composite Properties
def effective_refractive_index(n1, n2, volume_fraction):
    return n1 * volume_fraction + n2 * (1 - volume_fraction)

def maxwell_garnett_mixing(n_host, n_inclusion, volume_fraction):
    eps_host = n_host**2
    eps_inclusion = n_inclusion**2
    eps_eff = eps_host * (eps_inclusion + 2*eps_host + 2*volume_fraction*(eps_inclusion - eps_host)) / \
              (eps_inclusion + 2*eps_host - volume_fraction*(eps_inclusion - eps_host))
    return np.sqrt(eps_eff)

def bruggeman_mixing(n1, n2, f1):
    eps1, eps2 = n1**2, n2**2
    # Solve for effective medium
    a = f1 * (eps1 - eps2) / (eps1 + 2*eps2)
    b = (1 - f1) * (eps2 - eps1) / (eps2 + 2*eps1)
    eps_eff = eps1 if abs(a + b) < 1e-10 else eps2
    return np.sqrt(eps_eff)

def composite_thermal_conductivity(k1, k2, volume_fraction):
    return k1 * volume_fraction + k2 * (1 - volume_fraction)

def rule_of_mixtures_modulus(E1, E2, volume_fraction):
    return E1 * volume_fraction + E2 * (1 - volume_fraction)

# Material Database Helpers
def interpolate_property(wavelength, wavelength_data, property_data):
    return np.interp(wavelength, wavelength_data, property_data)

def temperature_scaling(property_value, temp, reference_temp, temp_coefficient):
    return property_value * (1 + temp_coefficient * (temp - reference_temp))

def wavelength_scaling(property_value, wavelength, reference_wavelength, wavelength_exponent):
    return property_value * (wavelength / reference_wavelength)**wavelength_exponent

def material_figure_of_merit(property1, property2, weight1=1, weight2=1):
    return weight1 * property1 + weight2 * property2

def property_uncertainty(measured_value, systematic_error, random_error):
    return np.sqrt(systematic_error**2 + random_error**2)

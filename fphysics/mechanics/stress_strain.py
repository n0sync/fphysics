import math
from constants import *

def normal_stress(force, area):
    return force / area

def shear_stress(force, area):
    return force / area

def normal_strain(delta_length, original_length):
    return delta_length / original_length

def shear_strain(displacement, height):
    return displacement / height

def hookes_law_stress(elastic_modulus, strain):
    return elastic_modulus * strain

def hookes_law_strain(stress, elastic_modulus):
    return stress / elastic_modulus

def elastic_modulus(stress, strain):
    return stress / strain

def poissons_ratio(lateral_strain, axial_strain):
    return -lateral_strain / axial_strain

def shear_modulus(shear_stress, shear_strain):
    return shear_stress / shear_strain

def bulk_modulus(pressure, volumetric_strain):
    return pressure / volumetric_strain

def elastic_moduli_relationship(elastic_modulus, shear_modulus, poissons_ratio):
    bulk_modulus = elastic_modulus / (3 * (1 - 2 * poissons_ratio))
    return bulk_modulus

def stress_concentration_factor(max_stress, nominal_stress):
    return max_stress / nominal_stress

def bending_stress(moment, distance_from_neutral, second_moment_of_area):
    return moment * distance_from_neutral / second_moment_of_area

def torsional_stress(torque, radius, polar_moment_of_inertia):
    return torque * radius / polar_moment_of_inertia

def von_mises_stress(sigma_x, sigma_y, sigma_z, tau_xy, tau_yz, tau_zx):
    return math.sqrt(0.5 * ((sigma_x - sigma_y)**2 + (sigma_y - sigma_z)**2 + 
                           (sigma_z - sigma_x)**2 + 6 * (tau_xy**2 + tau_yz**2 + tau_zx**2)))

def principal_stress_2d(sigma_x, sigma_y, tau_xy):
    avg_stress = (sigma_x + sigma_y) / 2
    diff_stress = (sigma_x - sigma_y) / 2
    shear_component = math.sqrt(diff_stress**2 + tau_xy**2)
    
    sigma_1 = avg_stress + shear_component
    sigma_2 = avg_stress - shear_component
    return sigma_1, sigma_2

def max_shear_stress_2d(sigma_x, sigma_y, tau_xy):
    diff_stress = (sigma_x - sigma_y) / 2
    return math.sqrt(diff_stress**2 + tau_xy**2)

def mohr_circle_center(sigma_x, sigma_y):
    return (sigma_x + sigma_y) / 2

def mohr_circle_radius(sigma_x, sigma_y, tau_xy):
    diff_stress = (sigma_x - sigma_y) / 2
    return math.sqrt(diff_stress**2 + tau_xy**2)

def strain_energy_density(stress, strain):
    return 0.5 * stress * strain

def strain_energy_elastic(elastic_modulus, stress, volume):
    return (stress**2 * volume) / (2 * elastic_modulus)

def thermal_stress(elastic_modulus, thermal_expansion_coeff, temperature_change):
    return elastic_modulus * thermal_expansion_coeff * temperature_change

def thermal_strain(thermal_expansion_coeff, temperature_change):
    return thermal_expansion_coeff * temperature_change

def beam_deflection_cantilever_point_load(force, length, elastic_modulus, second_moment):
    return (force * length**3) / (3 * elastic_modulus * second_moment)

def beam_deflection_simply_supported_center_load(force, length, elastic_modulus, second_moment):
    return (force * length**3) / (48 * elastic_modulus * second_moment)

def beam_deflection_cantilever_distributed_load(load_per_unit, length, elastic_modulus, second_moment):
    return (load_per_unit * length**4) / (8 * elastic_modulus * second_moment)

def critical_buckling_load_euler(elastic_modulus, second_moment, length, end_condition_factor=1):
    return (PI**2 * elastic_modulus * second_moment * end_condition_factor) / length**2

def slenderness_ratio(length, radius_of_gyration):
    return length / radius_of_gyration

def radius_of_gyration(second_moment_of_area, area):
    return math.sqrt(second_moment_of_area / area)

def fatigue_life_basquin(stress_amplitude, fatigue_strength_coeff, fatigue_strength_exponent):
    return (stress_amplitude / fatigue_strength_coeff)**(1 / fatigue_strength_exponent)

def stress_intensity_factor(stress, crack_length, geometry_factor=1.12):
    return geometry_factor * stress * math.sqrt(PI * crack_length)

def fracture_toughness(stress_intensity_factor_critical):
    return stress_intensity_factor_critical

def creep_strain_rate(applied_stress, temperature, material_constants):
    A, n, Q, R = material_constants
    return A * (applied_stress**n) * math.exp(-Q / (R * temperature))

def effective_stress_von_mises(stress_tensor):
    s11, s22, s33, s12, s13, s23 = stress_tensor
    return math.sqrt(0.5 * ((s11 - s22)**2 + (s22 - s33)**2 + (s33 - s11)**2 + 
                           6 * (s12**2 + s13**2 + s23**2)))

def plane_stress_transformation(sigma_x, sigma_y, tau_xy, theta):
    cos_theta = math.cos(theta)
    sin_theta = math.sin(theta)
    cos_2theta = math.cos(2 * theta)
    sin_2theta = math.sin(2 * theta)
    
    sigma_x_prime = (sigma_x + sigma_y) / 2 + (sigma_x - sigma_y) / 2 * cos_2theta + tau_xy * sin_2theta
    sigma_y_prime = (sigma_x + sigma_y) / 2 - (sigma_x - sigma_y) / 2 * cos_2theta - tau_xy * sin_2theta
    tau_xy_prime = -(sigma_x - sigma_y) / 2 * sin_2theta + tau_xy * cos_2theta
    
    return sigma_x_prime, sigma_y_prime, tau_xy_prime

def yield_criterion_tresca(sigma_1, sigma_2, sigma_3, yield_strength):
    max_shear = max(abs(sigma_1 - sigma_2), abs(sigma_2 - sigma_3), abs(sigma_3 - sigma_1)) / 2
    return max_shear <= yield_strength / 2

def yield_criterion_von_mises(sigma_1, sigma_2, sigma_3, yield_strength):
    von_mises = math.sqrt(0.5 * ((sigma_1 - sigma_2)**2 + (sigma_2 - sigma_3)**2 + (sigma_3 - sigma_1)**2))
    return von_mises <= yield_strength

def combined_stress_bending_axial(axial_stress, bending_stress):
    return axial_stress + bending_stress

def combined_stress_torsion_bending(bending_stress, torsional_stress):
    return math.sqrt(bending_stress**2 + 3 * torsional_stress**2)

def impact_stress(static_stress, height, static_deflection):
    return static_stress * (1 + math.sqrt(1 + 2 * height / static_deflection))

def stress_concentration_circular_hole(nominal_stress, hole_diameter, width):
    return nominal_stress * (1 + 2 * hole_diameter / width)

def endurance_limit_steel(ultimate_tensile_strength):
    return 0.5 * ultimate_tensile_strength

def goodman_relation(mean_stress, alternating_stress, ultimate_strength, endurance_limit):
    return alternating_stress / endurance_limit + mean_stress / ultimate_strength

def soderberg_relation(mean_stress, alternating_stress, yield_strength, endurance_limit):
    return alternating_stress / endurance_limit + mean_stress / yield_strength

def residual_stress_thermal_gradient(elastic_modulus, thermal_expansion, temp_gradient):
    return elastic_modulus * thermal_expansion * temp_gradient

def contact_stress_hertz(force, radius1, radius2, elastic_modulus, poissons_ratio):
    effective_radius = (radius1 * radius2) / (radius1 + radius2)
    effective_modulus = elastic_modulus / (2 * (1 - poissons_ratio**2))
    return math.sqrt(force * effective_modulus / (PI * effective_radius))

def bearing_stress(load, bearing_area):
    return load / bearing_area

def punching_shear_stress(load, perimeter, thickness):
    return load / (perimeter * thickness)

def plate_bending_stress(moment, thickness, poissons_ratio):
    return 6 * moment / (thickness**2 * (1 - poissons_ratio**2))

def membrane_stress_pressure_vessel(pressure, radius, thickness):
    return pressure * radius / thickness

def hoop_stress_thick_cylinder(internal_pressure, internal_radius, external_radius, radius):
    return internal_pressure * internal_radius**2 / (external_radius**2 - internal_radius**2) * (1 + external_radius**2 / radius**2)

def radial_stress_thick_cylinder(internal_pressure, internal_radius, external_radius, radius):
    return internal_pressure * internal_radius**2 / (external_radius**2 - internal_radius**2) * (1 - external_radius**2 / radius**2)

def stress_relaxation_time(initial_stress, relaxation_time, time):
    return initial_stress * math.exp(-time / relaxation_time)

def viscoelastic_maxwell_model(stress, relaxation_time, elastic_modulus, time):
    return stress * math.exp(-time / relaxation_time) / elastic_modulus

def creep_compliance(initial_strain, steady_state_rate, time):
    return initial_strain + steady_state_rate * time

def paris_law_crack_growth(stress_intensity_range, material_constant, exponent):
    return material_constant * (stress_intensity_range**exponent)

import math
from ..constants import *

def stress(force, area):
    return force / area

def strain(delta_length, original_length):
    return delta_length / original_length

def elastic_modulus(stress_val, strain_val):
    return stress_val / strain_val

def beam_deflection(force, length, elastic_mod, moment_of_inertia):
    return (force * length**3) / (3 * elastic_mod * moment_of_inertia)

def bone_stress_fracture(force, cross_sectional_area):
    return force / cross_sectional_area

def muscle_force(cross_sectional_area, specific_tension=300000):
    return cross_sectional_area * specific_tension

def tendon_spring_constant(elastic_mod, cross_sectional_area, length):
    return (elastic_mod * cross_sectional_area) / length

def joint_torque(force, moment_arm):
    return force * moment_arm

def walking_gait_frequency(leg_length, gravity=EARTH_GRAVITY):
    return 1 / (2 * math.pi * math.sqrt(leg_length / gravity))

def bone_density_from_ct(hounsfield_units):
    return 0.001 * hounsfield_units + 1.0

def muscle_power(force, velocity):
    return force * velocity

def metabolic_cost_walking(body_mass, speed, efficiency=0.25):
    return (body_mass * speed**2) / (2 * efficiency)

def impact_force_landing(mass, velocity, deformation_distance):
    return (mass * velocity**2) / (2 * deformation_distance)

def bone_remodeling_stimulus(strain_energy_density):
    return strain_energy_density / (2 * YOUNG_MODULUS_BONE)

def viscoelastic_relaxation(initial_stress, time, relaxation_time):
    return initial_stress * math.exp(-time / relaxation_time)

def fluid_flow_in_bone(pressure_gradient, permeability, viscosity, porosity):
    return -(permeability / viscosity) * pressure_gradient * porosity

def muscle_activation_dynamics(neural_input, time_constant):
    return 1 - math.exp(-neural_input / time_constant)

def ligament_strain_energy(force, displacement, spring_constant):
    return 0.5 * spring_constant * displacement**2

def fracture_toughness(critical_stress, crack_length):
    return critical_stress * math.sqrt(math.pi * crack_length)


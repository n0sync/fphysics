import math
from constants import *

def ficks_first_law(diffusion_coefficient, concentration_gradient):
    return -diffusion_coefficient * concentration_gradient

def ficks_second_law_solution_1d(initial_concentration, distance, time, diffusion_coefficient):
    return initial_concentration * math.exp(-distance**2 / (4 * diffusion_coefficient * time))

def einstein_diffusion_relation(mobility):
    return mobility * BOLTZMANN_CONSTANT * BODY_TEMPERATURE

def stokes_einstein_diffusion(temperature, viscosity, particle_radius):
    return (BOLTZMANN_CONSTANT * temperature) / (6 * math.pi * viscosity * particle_radius)

def random_walk_distance(diffusion_coefficient, time):
    return math.sqrt(6 * diffusion_coefficient * time)

def facilitated_diffusion_rate(max_rate, concentration, km):
    return (max_rate * concentration) / (km + concentration)

def membrane_flux(permeability, concentration_difference):
    return permeability * concentration_difference

def concentration_after_diffusion(initial_concentration, time, diffusion_coefficient, length):
    return initial_concentration * math.exp(-time / (length**2 / (math.pi**2 * diffusion_coefficient)))

def effective_diffusion_coefficient(tortuosity, porosity, bulk_diffusion_coefficient):
    return (porosity / tortuosity) * bulk_diffusion_coefficient

def drug_release_rate(surface_area, diffusion_coefficient, concentration_gradient, thickness):
    return surface_area * diffusion_coefficient * concentration_gradient / thickness

def brownian_motion_velocity(diffusion_coefficient, time_step):
    return math.sqrt(2 * diffusion_coefficient / time_step)

def anomalous_diffusion_msd(time, diffusion_coefficient, anomalous_exponent):
    return 2 * diffusion_coefficient * time**anomalous_exponent

def hindered_diffusion_coefficient(bulk_diffusion_coefficient, fiber_volume_fraction):
    return bulk_diffusion_coefficient * math.exp(-fiber_volume_fraction / 0.33)

def convection_diffusion_peclet_number(velocity, length_scale, diffusion_coefficient):
    return (velocity * length_scale) / diffusion_coefficient

def molecular_crowding_factor(volume_fraction):
    return 1 / (1 - volume_fraction)**2

def diffusion_limited_reaction_rate(diffusion_coefficient, encounter_radius):
    return 4 * math.pi * encounter_radius * diffusion_coefficient

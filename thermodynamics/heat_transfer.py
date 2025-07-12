import math
from constants import *

def fourier_law_conduction(thermal_conductivity, area, temperature_gradient):
    return -thermal_conductivity * area * temperature_gradient

def heat_conduction_1d_steady(thermal_conductivity, area, temperature_difference, thickness):
    return thermal_conductivity * area * temperature_difference / thickness

def thermal_resistance_conduction(thickness, thermal_conductivity, area):
    return thickness / (thermal_conductivity * area)

def thermal_resistance_convection(heat_transfer_coefficient, area):
    return 1 / (heat_transfer_coefficient * area)

def thermal_resistance_radiation(emissivity, area, temperature):
    return 1 / (4 * emissivity * STEFAN_BOLTZMANN_CONSTANT * area * temperature**3)

def composite_wall_resistance(resistances):
    return sum(resistances)

def parallel_thermal_resistance(resistances):
    return 1 / sum(1/r for r in resistances)

def heat_transfer_coefficient_natural_convection(nusselt_number, thermal_conductivity, characteristic_length):
    return nusselt_number * thermal_conductivity / characteristic_length

def heat_transfer_coefficient_forced_convection(nusselt_number, thermal_conductivity, characteristic_length):
    return nusselt_number * thermal_conductivity / characteristic_length

def newtons_law_cooling(heat_transfer_coefficient, area, temperature_difference):
    return heat_transfer_coefficient * area * temperature_difference

def reynolds_number(density, velocity, characteristic_length, dynamic_viscosity):
    return density * velocity * characteristic_length / dynamic_viscosity

def prandtl_number(specific_heat, dynamic_viscosity, thermal_conductivity):
    return specific_heat * dynamic_viscosity / thermal_conductivity

def grashof_number(gravity, thermal_expansion_coefficient, temperature_difference, characteristic_length, kinematic_viscosity):
    return gravity * thermal_expansion_coefficient * temperature_difference * characteristic_length**3 / kinematic_viscosity**2

def rayleigh_number(grashof_number, prandtl_number):
    return grashof_number * prandtl_number

def nusselt_number_forced_convection_plate(reynolds_number, prandtl_number):
    if reynolds_number < 5e5:
        return 0.332 * reynolds_number**0.5 * prandtl_number**(1/3)
    else:
        return 0.037 * reynolds_number**0.8 * prandtl_number**(1/3)

def nusselt_number_natural_convection_vertical_plate(rayleigh_number):
    if rayleigh_number < 1e9:
        return 0.59 * rayleigh_number**0.25
    else:
        return 0.1 * rayleigh_number**(1/3)

def nusselt_number_cylinder_crossflow(reynolds_number, prandtl_number):
    return 0.3 + (0.62 * reynolds_number**0.5 * prandtl_number**(1/3)) / (1 + (0.4/prandtl_number)**(2/3))**0.25

def stefan_boltzmann_radiation(emissivity, area, temperature):
    return emissivity * STEFAN_BOLTZMANN_CONSTANT * area * temperature**4

def radiation_heat_transfer_between_surfaces(emissivity1, emissivity2, area, temperature1, temperature2):
    view_factor = 1  # assuming simple geometry
    return view_factor * STEFAN_BOLTZMANN_CONSTANT * area * (temperature1**4 - temperature2**4) / (1/emissivity1 + 1/emissivity2 - 1)

def radiation_heat_transfer_coefficient(emissivity, temperature):
    return 4 * emissivity * STEFAN_BOLTZMANN_CONSTANT * temperature**3

def fin_efficiency(fin_parameter, fin_length):
    return math.tanh(fin_parameter * fin_length) / (fin_parameter * fin_length)

def fin_parameter(heat_transfer_coefficient, perimeter, thermal_conductivity, cross_sectional_area):
    return math.sqrt(heat_transfer_coefficient * perimeter / (thermal_conductivity * cross_sectional_area))

def fin_heat_transfer(fin_efficiency, heat_transfer_coefficient, fin_area, temperature_difference):
    return fin_efficiency * heat_transfer_coefficient * fin_area * temperature_difference

def heat_transfer_enhancement_factor(enhanced_surface_area, base_surface_area):
    return enhanced_surface_area / base_surface_area

def thermal_diffusivity(thermal_conductivity, density, specific_heat):
    return thermal_conductivity / (density * specific_heat)

def biot_number(heat_transfer_coefficient, characteristic_length, thermal_conductivity):
    return heat_transfer_coefficient * characteristic_length / thermal_conductivity

def fourier_number(thermal_diffusivity, time, characteristic_length):
    return thermal_diffusivity * time / characteristic_length**2

def lumped_capacitance_temperature(initial_temperature, ambient_temperature, time_constant, time):
    return ambient_temperature + (initial_temperature - ambient_temperature) * math.exp(-time / time_constant)

def lumped_capacitance_time_constant(mass, specific_heat, heat_transfer_coefficient, surface_area):
    return mass * specific_heat / (heat_transfer_coefficient * surface_area)

def transient_conduction_infinite_plate(initial_temperature, surface_temperature, thermal_diffusivity, time, position, plate_thickness):
    alpha = thermal_diffusivity
    L = plate_thickness / 2
    return surface_temperature + (initial_temperature - surface_temperature) * math.cos(PI * position / (2 * L)) * math.exp(-PI**2 * alpha * time / (4 * L**2))

def heat_generation_rate(power_density, volume):
    return power_density * volume

def critical_thickness_insulation(thermal_conductivity_insulation, heat_transfer_coefficient):
    return thermal_conductivity_insulation / heat_transfer_coefficient

def heat_exchanger_lmtd(inlet_hot, outlet_hot, inlet_cold, outlet_cold):
    delta_t1 = inlet_hot - outlet_cold
    delta_t2 = outlet_hot - inlet_cold
    if delta_t1 == delta_t2:
        return delta_t1
    else:
        return (delta_t1 - delta_t2) / math.log(delta_t1 / delta_t2)

def heat_exchanger_effectiveness_counterflow(ntu, capacity_ratio):
    if capacity_ratio == 1:
        return ntu / (1 + ntu)
    else:
        return (1 - math.exp(-ntu * (1 - capacity_ratio))) / (1 - capacity_ratio * math.exp(-ntu * (1 - capacity_ratio)))

def heat_exchanger_effectiveness_parallel_flow(ntu, capacity_ratio):
    return (1 - math.exp(-ntu * (1 + capacity_ratio))) / (1 + capacity_ratio)

def ntu_heat_exchanger(overall_heat_transfer_coefficient, area, minimum_capacity_rate):
    return overall_heat_transfer_coefficient * area / minimum_capacity_rate

def overall_heat_transfer_coefficient(individual_coefficients, thermal_resistances):
    total_resistance = sum(thermal_resistances) + sum(1/coeff for coeff in individual_coefficients)
    return 1 / total_resistance

def convective_mass_transfer_coefficient(sherwood_number, diffusion_coefficient, characteristic_length):
    return sherwood_number * diffusion_coefficient / characteristic_length

def sherwood_number(mass_transfer_coefficient, characteristic_length, diffusion_coefficient):
    return mass_transfer_coefficient * characteristic_length / diffusion_coefficient

def schmidt_number(kinematic_viscosity, diffusion_coefficient):
    return kinematic_viscosity / diffusion_coefficient

def peclet_number_heat(reynolds_number, prandtl_number):
    return reynolds_number * prandtl_number

def peclet_number_mass(reynolds_number, schmidt_number):
    return reynolds_number * schmidt_number

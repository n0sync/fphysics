import math
from ..constants import *

def ideal_gas_law(pressure, volume, temperature, moles):
    return pressure * volume == moles * GAS_CONSTANT * temperature

def first_law_thermodynamics(internal_energy_change, heat, work):
    return internal_energy_change == heat - work

def second_law_efficiency(hot_reservoir_temp, cold_reservoir_temp):
    return 1 - cold_reservoir_temp / hot_reservoir_temp

def carnot_efficiency(hot_temp, cold_temp):
    return (hot_temp - cold_temp) / hot_temp

def entropy_change_isothermal(heat, temperature):
    return heat / temperature

def entropy_change_ideal_gas(initial_temp, final_temp, initial_volume, final_volume, moles):
    temp_term = moles * GAS_CONSTANT * math.log(final_temp / initial_temp)
    volume_term = moles * GAS_CONSTANT * math.log(final_volume / initial_volume)
    return temp_term + volume_term

def heat_capacity_constant_volume(internal_energy_change, temperature_change):
    return internal_energy_change / temperature_change

def heat_capacity_constant_pressure(enthalpy_change, temperature_change):
    return enthalpy_change / temperature_change

def adiabatic_relation_temperature_volume(initial_temp, initial_volume, final_volume, gamma):
    return initial_temp * (initial_volume / final_volume)**(gamma - 1)

def adiabatic_relation_pressure_volume(initial_pressure, initial_volume, final_volume, gamma):
    return initial_pressure * (initial_volume / final_volume)**gamma

def isothermal_work(pressure, initial_volume, final_volume):
    return pressure * math.log(final_volume / initial_volume)

def adiabatic_work(initial_pressure, initial_volume, final_volume, gamma):
    return (initial_pressure * initial_volume / (gamma - 1)) * (1 - (final_volume / initial_volume)**(gamma - 1))

def otto_cycle_efficiency(compression_ratio, gamma):
    return 1 - compression_ratio**(1 - gamma)

def diesel_cycle_efficiency(compression_ratio, cutoff_ratio, gamma):
    term1 = 1 - compression_ratio**(1 - gamma)
    term2 = (cutoff_ratio**gamma - 1) / (gamma * (cutoff_ratio - 1))
    return 1 - term1 * term2

def refrigerator_cop(heat_extracted, work_input):
    return heat_extracted / work_input

def heat_pump_cop(heat_delivered, work_input):
    return heat_delivered / work_input

def maxwell_boltzmann_distribution(velocity, mass, temperature):
    factor = math.sqrt(mass / (2 * PI * BOLTZMANN_CONSTANT * temperature))
    exponent = -mass * velocity**2 / (2 * BOLTZMANN_CONSTANT * temperature)
    return 4 * PI * velocity**2 * factor**3 * math.exp(exponent)

def average_kinetic_energy_gas(temperature):
    return 1.5 * BOLTZMANN_CONSTANT * temperature

def root_mean_square_velocity(temperature, molar_mass):
    return math.sqrt(3 * GAS_CONSTANT * temperature / molar_mass)

def mean_velocity_gas(temperature, molar_mass):
    return math.sqrt(8 * GAS_CONSTANT * temperature / (PI * molar_mass))

def most_probable_velocity(temperature, molar_mass):
    return math.sqrt(2 * GAS_CONSTANT * temperature / molar_mass)

def equipartition_theorem_energy(degrees_of_freedom, temperature):
    return 0.5 * degrees_of_freedom * BOLTZMANN_CONSTANT * temperature

def stefan_boltzmann_law(temperature, area, emissivity):
    return emissivity * STEFAN_BOLTZMANN_CONSTANT * area * temperature**4

def wien_displacement_law(temperature):
    return WIEN_DISPLACEMENT_CONSTANT / temperature

def planck_distribution(frequency, temperature):
    hf_kt = PLANCK_CONSTANT * frequency / (BOLTZMANN_CONSTANT * temperature)
    return (2 * PLANCK_CONSTANT * frequency**3 / SPEED_OF_LIGHT**2) / (math.exp(hf_kt) - 1)

def rayleigh_jeans_law(frequency, temperature):
    return 2 * frequency**2 * BOLTZMANN_CONSTANT * temperature / SPEED_OF_LIGHT**2

def free_energy_helmholtz(internal_energy, temperature, entropy):
    return internal_energy - temperature * entropy

def free_energy_gibbs(enthalpy, temperature, entropy):
    return enthalpy - temperature * entropy

def chemical_potential_ideal_gas(temperature, pressure, reference_pressure):
    return BOLTZMANN_CONSTANT * temperature * math.log(pressure / reference_pressure)

def partition_function_harmonic_oscillator(frequency, temperature):
    beta = 1 / (BOLTZMANN_CONSTANT * temperature)
    return 1 / (2 * math.sinh(beta * PLANCK_CONSTANT * frequency / 2))

def fermi_dirac_distribution(energy, chemical_potential, temperature):
    exponent = (energy - chemical_potential) / (BOLTZMANN_CONSTANT * temperature)
    return 1 / (math.exp(exponent) + 1)

def bose_einstein_distribution(energy, chemical_potential, temperature):
    exponent = (energy - chemical_potential) / (BOLTZMANN_CONSTANT * temperature)
    return 1 / (math.exp(exponent) - 1)

def thermal_conductivity_fourier(heat_flux, temperature_gradient):
    return -heat_flux / temperature_gradient

def thermal_diffusivity(thermal_conductivity, density, specific_heat):
    return thermal_conductivity / (density * specific_heat)

def heat_equation_1d(thermal_diffusivity, second_derivative_temp):
    return thermal_diffusivity * second_derivative_temp


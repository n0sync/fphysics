import math
from constants import *

def atmospheric_pressure_altitude(altitude):
    """Atmospheric pressure at altitude"""
    return ATMOSPHERIC_PRESSURE * math.exp(-altitude / 8400)

def air_density_altitude(altitude, temperature=288.15):
    """Air density at altitude"""
    pressure = atmospheric_pressure_altitude(altitude)
    return pressure / (287 * temperature)

def sound_speed_air(temperature):
    """Speed of sound in air at given temperature"""
    return 331.3 * math.sqrt(temperature / 273.15)

def greenhouse_effect_temperature(solar_constant, albedo, emissivity=1):
    """Greenhouse effect temperature calculation"""
    absorbed_power = solar_constant * (1 - albedo) / 4
    return (absorbed_power / (emissivity * STEFAN_BOLTZMANN_CONSTANT))**(1/4)

def solar_irradiance(solar_constant, zenith_angle):
    """Solar irradiance at surface"""
    return solar_constant * math.cos(zenith_angle)

def photosynthetic_photon_flux(irradiance, wavelength=550e-9):
    """Photosynthetic photon flux density"""
    photon_energy = PLANCK_CONSTANT * SPEED_OF_LIGHT / wavelength
    return irradiance / photon_energy

def clausius_clapeyron(temperature, latent_heat):
    """Clausius-Clapeyron equation for vapor pressure"""
    reference_temp = 273.15
    reference_pressure = 611.2
    return reference_pressure * math.exp((latent_heat / GAS_CONSTANT) * (1/reference_temp - 1/temperature))

def mixing_ratio(vapor_pressure, total_pressure):
    """Water vapor mixing ratio"""
    return 0.622 * vapor_pressure / (total_pressure - vapor_pressure)

def potential_temperature(temperature, pressure, reference_pressure=100000):
    """Potential temperature"""
    return temperature * (reference_pressure / pressure)**(0.286)

def richardson_number(gravity, temperature_gradient, wind_shear, reference_temp):
    """Richardson number for atmospheric stability"""
    return (gravity / reference_temp) * temperature_gradient / wind_shear**2

def coriolis_parameter(latitude):
    """Coriolis parameter"""
    omega = 2 * PI / 86400
    return 2 * omega * math.sin(math.radians(latitude))

def geostrophic_wind(pressure_gradient, density, latitude):
    """Geostrophic wind speed"""
    f = coriolis_parameter(latitude)
    return pressure_gradient / (density * f)

def ozone_depletion_potential(concentration, reaction_rate, lifetime):
    """Ozone depletion potential"""
    return concentration * reaction_rate * lifetime

def radiative_forcing(delta_concentration, forcing_efficiency):
    """Radiative forcing calculation"""
    return forcing_efficiency * math.log(delta_concentration)

def heat_island_intensity(urban_temp, rural_temp):
    """Urban heat island intensity"""
    return urban_temp - rural_temp

def albedo_feedback(initial_albedo, temperature_change, feedback_coefficient):
    """Albedo feedback mechanism"""
    return initial_albedo - feedback_coefficient * temperature_change

def photolysis_rate(solar_zenith, absorption_cross_section, quantum_yield):
    """Photolysis rate calculation"""
    actinic_flux = 1e15 * math.cos(solar_zenith)
    return absorption_cross_section * quantum_yield * actinic_flux

def aerosol_optical_depth(extinction_coeff, path_length):
    """Aerosol optical depth"""
    return extinction_coeff * path_length

def scattering_coefficient(particle_concentration, scattering_cross_section):
    """Aerosol scattering coefficient"""
    return particle_concentration * scattering_cross_section

def visibility_range(extinction_coeff, contrast_threshold=0.02):
    """Visibility range from extinction"""
    return -math.log(contrast_threshold) / extinction_coeff

def settling_velocity(particle_diameter, particle_density, air_density=1.2, viscosity=1.8e-5):
    """Particle settling velocity"""
    return (particle_diameter**2 * (particle_density - air_density) * EARTH_GRAVITY) / (18 * viscosity)

def diffusion_coefficient_atmospheric(temperature, pressure, molecular_weight):
    """Atmospheric diffusion coefficient"""
    return 1e-5 * (temperature / 273.15)**(1.75) * (101325 / pressure) * (29 / molecular_weight)**0.5

def residence_time(total_mass, removal_rate):
    """Atmospheric residence time"""
    return total_mass / removal_rate

def carbon_cycle_flux(concentration_gradient, transfer_velocity):
    """Carbon cycle flux calculation"""
    return concentration_gradient * transfer_velocity

def photochemical_equilibrium(production_rate, loss_rate):
    """Photochemical equilibrium concentration"""
    return production_rate / loss_rate

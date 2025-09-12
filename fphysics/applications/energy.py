import math
from ..constants import *

def solar_cell_efficiency(power_out, solar_irradiance, cell_area):
    """Solar cell efficiency"""
    power_in = solar_irradiance * cell_area
    return power_out / power_in

def photovoltaic_current(photon_flux, quantum_efficiency, charge=ELEMENTARY_CHARGE):
    """Photovoltaic current calculation"""
    return photon_flux * quantum_efficiency * charge

def carnot_efficiency(hot_temp, cold_temp):
    """Carnot cycle efficiency"""
    return 1 - cold_temp / hot_temp

def wind_power(air_density, swept_area, wind_speed, power_coefficient=0.4):
    """Wind turbine power output"""
    return 0.5 * air_density * swept_area * wind_speed**3 * power_coefficient

def hydroelectric_power(flow_rate, head, efficiency=0.9):
    """Hydroelectric power calculation"""
    return flow_rate * WATER_DENSITY * EARTH_GRAVITY * head * efficiency

def fuel_cell_voltage(gibbs_free_energy, electrons_transferred=2):
    """Fuel cell theoretical voltage"""
    return -gibbs_free_energy / (electrons_transferred * ELEMENTARY_CHARGE)

def battery_energy_density(voltage, capacity, mass):
    """Battery energy density"""
    energy = voltage * capacity * 3600
    return energy / mass

def thermal_conductivity_insulation(heat_flux, thickness, temperature_diff):
    """Thermal conductivity from insulation performance"""
    return heat_flux * thickness / temperature_diff

def heat_pump_cop(heat_delivered, work_input):
    """Heat pump coefficient of performance"""
    return heat_delivered / work_input

def stirling_engine_power(pressure_amplitude, volume_amplitude, frequency):
    """Stirling engine power approximation"""
    return pressure_amplitude * volume_amplitude * frequency

def nuclear_binding_energy(mass_number, binding_energy_per_nucleon=8.5):
    """Nuclear binding energy"""
    return mass_number * binding_energy_per_nucleon * ELECTRON_VOLT * 1e6

def fission_energy_release(fissile_mass):
    """Energy released in nuclear fission"""
    energy_per_fission = 200e6 * ELECTRON_VOLT
    nuclei_per_gram = AVOGADRO_NUMBER / 235
    return fissile_mass * nuclei_per_gram * energy_per_fission

def fusion_energy_release(fuel_mass, q_value=17.6e6):
    """Energy released in nuclear fusion"""
    return fuel_mass * q_value * ELECTRON_VOLT / (4 * ATOMIC_MASS_UNIT)

def blackbody_power_density(temperature):
    """Blackbody power density"""
    return STEFAN_BOLTZMANN_CONSTANT * temperature**4

def wien_peak_wavelength(temperature):
    """Wien's displacement law"""
    return WIEN_DISPLACEMENT_CONSTANT / temperature

def photon_energy(wavelength):
    """Photon energy from wavelength"""
    return PLANCK_CONSTANT * SPEED_OF_LIGHT / wavelength

def solar_constant_distance(distance_au=1.0):
    """Solar constant at given distance"""
    return SOLAR_LUMINOSITY / (4 * PI * (distance_au * ASTRONOMICAL_UNIT)**2)

def geothermal_gradient_power(gradient, area, thermal_conductivity):
    """Geothermal power from temperature gradient"""
    return gradient * area * thermal_conductivity

def piezoelectric_power(force, displacement, coupling_coefficient):
    """Piezoelectric power generation"""
    return force * displacement * coupling_coefficient

def thermoelectric_power(seebeck_coeff, temperature_diff, resistance):
    """Thermoelectric power generation"""
    voltage = seebeck_coeff * temperature_diff
    return voltage**2 / resistance

def biomass_energy_content(mass, heating_value=15e6):
    """Biomass energy content"""
    return mass * heating_value

def tidal_power(tidal_range, basin_area, water_density=1025):
    """Tidal energy potential"""
    return 0.5 * water_density * EARTH_GRAVITY * basin_area * tidal_range**2

def wave_power(wave_height, wave_period, water_depth):
    """Ocean wave power per unit width"""
    wavelength = EARTH_GRAVITY * wave_period**2 / (2 * PI)
    group_velocity = math.sqrt(EARTH_GRAVITY * wavelength / (2 * PI)) / 2
    return (WATER_DENSITY * EARTH_GRAVITY * wave_height**2 * group_velocity) / 8

def energy_storage_time(capacity, power_rating):
    """Energy storage duration"""
    return capacity / power_rating

def round_trip_efficiency(energy_out, energy_in):
    """Energy storage round-trip efficiency"""
    return energy_out / energy_in

def grid_frequency_regulation(power_imbalance, system_inertia):
    """Grid frequency change from power imbalance"""
    return power_imbalance / system_inertia

def transmission_line_losses(resistance, current):
    """Transmission line power losses"""
    return resistance * current**2

def transformer_efficiency(primary_voltage, primary_current, secondary_voltage, secondary_current):
    """Transformer efficiency"""
    power_in = primary_voltage * primary_current
    power_out = secondary_voltage * secondary_current
    return power_out / power_in


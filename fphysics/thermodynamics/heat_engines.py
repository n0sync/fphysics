import math
from constants import *

def carnot_efficiency(hot_temp, cold_temp):
    return (hot_temp - cold_temp) / hot_temp

def otto_cycle_efficiency(compression_ratio, gamma):
    return 1 - compression_ratio**(1 - gamma)

def diesel_cycle_efficiency(compression_ratio, cutoff_ratio, gamma):
    term1 = 1 - compression_ratio**(1 - gamma)
    term2 = (cutoff_ratio**gamma - 1) / (gamma * (cutoff_ratio - 1))
    return 1 - term1 * term2

def brayton_cycle_efficiency(pressure_ratio, gamma):
    return 1 - pressure_ratio**((1 - gamma) / gamma)

def stirling_cycle_efficiency(hot_temp, cold_temp):
    return carnot_efficiency(hot_temp, cold_temp)

def ericsson_cycle_efficiency(hot_temp, cold_temp):
    return carnot_efficiency(hot_temp, cold_temp)

def rankine_cycle_efficiency(turbine_work, pump_work, heat_input):
    net_work = turbine_work - pump_work
    return net_work / heat_input

def refrigerator_cop(heat_extracted, work_input):
    return heat_extracted / work_input

def heat_pump_cop(heat_delivered, work_input):
    return heat_delivered / work_input

def carnot_refrigerator_cop(hot_temp, cold_temp):
    return cold_temp / (hot_temp - cold_temp)

def carnot_heat_pump_cop(hot_temp, cold_temp):
    return hot_temp / (hot_temp - cold_temp)

def vapor_compression_cop(evaporator_temp, condenser_temp, compressor_efficiency):
    ideal_cop = evaporator_temp / (condenser_temp - evaporator_temp)
    return ideal_cop * compressor_efficiency

def absorption_refrigeration_cop(generator_temp, condenser_temp, evaporator_temp):
    return (evaporator_temp / (condenser_temp - evaporator_temp)) * (generator_temp - condenser_temp) / generator_temp

def thermoelectric_figure_of_merit(seebeck_coefficient, electrical_conductivity, thermal_conductivity, temperature):
    return seebeck_coefficient**2 * electrical_conductivity * temperature / thermal_conductivity

def thermoelectric_efficiency(figure_of_merit, hot_temp, cold_temp):
    z_avg = figure_of_merit
    m = math.sqrt(1 + z_avg * (hot_temp + cold_temp) / 2)
    return ((hot_temp - cold_temp) / hot_temp) * ((m - 1) / (m + cold_temp / hot_temp))

def fuel_cell_efficiency(gibbs_free_energy_change, enthalpy_change):
    return abs(gibbs_free_energy_change) / abs(enthalpy_change)

def fuel_cell_voltage(gibbs_free_energy_change, electrons_transferred):
    return abs(gibbs_free_energy_change) / (electrons_transferred * FARADAY_CONSTANT)

def steam_turbine_efficiency(actual_enthalpy_drop, isentropic_enthalpy_drop):
    return actual_enthalpy_drop / isentropic_enthalpy_drop

def gas_turbine_efficiency(actual_work, isentropic_work):
    return actual_work / isentropic_work

def compressor_efficiency(isentropic_work, actual_work):
    return isentropic_work / actual_work

def nozzle_efficiency(actual_kinetic_energy, isentropic_kinetic_energy):
    return actual_kinetic_energy / isentropic_kinetic_energy

def diffuser_efficiency(isentropic_enthalpy_rise, actual_enthalpy_rise):
    return isentropic_enthalpy_rise / actual_enthalpy_rise

def heat_exchanger_effectiveness(actual_heat_transfer, maximum_possible_heat_transfer):
    return actual_heat_transfer / maximum_possible_heat_transfer

def regenerator_effectiveness(temperature_rise_cold_fluid, maximum_temperature_difference):
    return temperature_rise_cold_fluid / maximum_temperature_difference

def combined_cycle_efficiency(gas_turbine_efficiency, steam_cycle_efficiency, heat_recovery_effectiveness):
    return gas_turbine_efficiency + steam_cycle_efficiency * heat_recovery_effectiveness * (1 - gas_turbine_efficiency)

def cogeneration_fuel_utilization_efficiency(power_output, useful_heat_output, fuel_energy_input):
    return (power_output + useful_heat_output) / fuel_energy_input

def power_plant_heat_rate(fuel_energy_input, electrical_power_output):
    return fuel_energy_input / electrical_power_output

def exergy_efficiency(useful_exergy_output, exergy_input):
    return useful_exergy_output / exergy_input

def exergy_destruction(exergy_input, exergy_output):
    return exergy_input - exergy_output

def isentropic_efficiency_turbine(actual_work, isentropic_work):
    return actual_work / isentropic_work

def isentropic_efficiency_compressor(isentropic_work, actual_work):
    return isentropic_work / actual_work

def polytropic_efficiency(polytropic_index, gamma):
    return (gamma - 1) / (gamma * (polytropic_index - 1))

def mechanical_efficiency(brake_power, indicated_power):
    return brake_power / indicated_power

def volumetric_efficiency(actual_air_flow, theoretical_air_flow):
    return actual_air_flow / theoretical_air_flow

def thermal_efficiency_ic_engine(net_work, fuel_energy):
    return net_work / fuel_energy

def specific_fuel_consumption(fuel_flow_rate, power_output):
    return fuel_flow_rate / power_output

def brake_specific_fuel_consumption(fuel_consumption_rate, brake_power):
    return fuel_consumption_rate / brake_power

def indicated_thermal_efficiency(indicated_work, fuel_energy):
    return indicated_work / fuel_energy

def combustion_efficiency(actual_heating_value, theoretical_heating_value):
    return actual_heating_value / theoretical_heating_value

def air_fuel_ratio(mass_air, mass_fuel):
    return mass_air / mass_fuel

def equivalence_ratio(actual_air_fuel_ratio, stoichiometric_air_fuel_ratio):
    return stoichiometric_air_fuel_ratio / actual_air_fuel_ratio

def mean_effective_pressure(work_per_cycle, displacement_volume):
    return work_per_cycle / displacement_volume

def engine_torque(power, angular_velocity):
    return power / angular_velocity

def engine_power_from_torque(torque, angular_velocity):
    return torque * angular_velocity

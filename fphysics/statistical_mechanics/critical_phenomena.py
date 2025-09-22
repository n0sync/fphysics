import math
from ..constants import *

def ising_model_magnetization(temperature, critical_temperature, magnetic_field):
    if temperature < critical_temperature:
        return (1 - (temperature / critical_temperature)**2)**0.5
    else:
        return 0

def critical_opalescence(intensity_at_critical_point, temperature, critical_temperature):
    return intensity_at_critical_point / abs(temperature - critical_temperature)

def correlation_length(temperature, critical_temperature, decay_exponent):
    return abs(temperature - critical_temperature)**(-decay_exponent)

def heat_capacity(temperature, critical_temperature, alpha):
    return abs(temperature - critical_temperature)**(-alpha)

def magnetic_susceptibility(temperature, critical_temperature, gamma):
    return abs(temperature - critical_temperature)**(-gamma)

def scaling_of_magnetization(temperature, critical_temperature, beta):
    return abs(temperature - critical_temperature)**beta

def order_parameter_behavior(temperature, critical_temperature, beta):
    if temperature < critical_temperature:
        return (critical_temperature - temperature)**beta
    else:
        return 0

def coexistence_curve(pressure, critical_pressure, nu):
    return (1 - pressure / critical_pressure)**nu

def density_fluctuations(temperature, critical_temperature, gamma):
    return abs(temperature - critical_temperature)**(-gamma)

def relaxation_time(temperature, critical_temperature, nu, z):
    return abs(temperature - critical_temperature)**(-nu * z)

def ginzburg_criterion_temperature(temperature, critical_temperature, nu):
    return 1 / abs(temperature - critical_temperature)**nu

def lifshitz_point(pressure, critical_pressure, alpha, temperature_star):
    return temperature_star + (pressure - critical_pressure)**alpha

def interfacial_tension(temperature, critical_temperature, delta):
    return abs(temperature - critical_temperature)**delta


import math
from constants import *

def stress(force, area):
    """Calculate stress"""
    return force / area

def strain(delta_length, original_length):
    """Calculate strain"""
    return delta_length / original_length

def young_modulus(stress, strain):
    """Calculate Young's modulus"""
    return stress / strain

def thermal_expansion(length, alpha, delta_temp):
    """Linear thermal expansion"""
    return length * alpha * delta_temp

def heat_transfer_conduction(k, area, delta_temp, thickness):
    """Heat transfer by conduction"""
    return k * area * delta_temp / thickness

def reynolds_number(density, velocity, length, viscosity):
    """Calculate Reynolds number"""
    return density * velocity * length / viscosity

def drag_force(drag_coeff, density, velocity, area):
    """Calculate drag force"""
    return 0.5 * drag_coeff * density * velocity**2 * area

def lift_force(lift_coeff, density, velocity, area):
    """Calculate lift force"""
    return 0.5 * lift_coeff * density * velocity**2 * area

def moment_of_inertia_rectangle(width, height):
    """Moment of inertia for rectangular cross-section"""
    return width * height**3 / 12

def critical_buckling_load(e_modulus, moment_inertia, length):
    """Euler critical buckling load"""
    return PI**2 * e_modulus * moment_inertia / length**2

def fatigue_life(stress_amplitude, fatigue_strength_coeff, fatigue_strength_exp):
    """S-N fatigue life estimation"""
    return (stress_amplitude / fatigue_strength_coeff)**(1/fatigue_strength_exp)

def shear_stress_circular(torque, radius, polar_moment):
    """Shear stress in circular shaft"""
    return torque * radius / polar_moment

def deflection_cantilever(force, length, e_modulus, moment_inertia):
    """Deflection of cantilever beam"""
    return force * length**3 / (3 * e_modulus * moment_inertia)

def natural_frequency_beam(e_modulus, moment_inertia, mass_per_length, length):
    """Natural frequency of beam"""
    return (1.875**2 / (2 * PI)) * math.sqrt(e_modulus * moment_inertia / (mass_per_length * length**4))

def thermal_stress(e_modulus, alpha, delta_temp):
    """Thermal stress in constrained material"""
    return e_modulus * alpha * delta_temp

def pressure_vessel_hoop_stress(pressure, radius, thickness):
    """Hoop stress in thin-walled pressure vessel"""
    return pressure * radius / thickness

def creep_rate(stress, temperature, activation_energy, stress_exponent=5):
    """Creep rate equation"""
    return stress**stress_exponent * math.exp(-activation_energy / (BOLTZMANN_CONSTANT * temperature))

def fracture_toughness_critical_length(k_ic, stress, shape_factor=1):
    """Critical crack length from fracture toughness"""
    return (k_ic / (shape_factor * stress))**2 / PI

def electrical_resistance(resistivity, length, area):
    """Electrical resistance"""
    return resistivity * length / area

def power_dissipation(current, resistance):
    """Power dissipation in resistor"""
    return current**2 * resistance

def capacitance_parallel_plate(permittivity, area, distance):
    """Capacitance of parallel plate capacitor"""
    return permittivity * area / distance

def inductance_solenoid(permeability, turns, area, length):
    """Inductance of solenoid"""
    return permeability * turns**2 * area / length

def skin_depth(frequency, conductivity, permeability):
    """Electromagnetic skin depth"""
    return math.sqrt(2 / (2 * PI * frequency * conductivity * permeability))

def doppler_shift(source_freq, source_velocity, observer_velocity, wave_speed):
    """Doppler frequency shift"""
    return source_freq * (wave_speed + observer_velocity) / (wave_speed - source_velocity)

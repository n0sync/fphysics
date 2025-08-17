import math
from constants import *

def coulombs_law(q1, q2, distance):
    return COULOMB_CONSTANT * q1 * q2 / distance**2

def electric_field_point_charge(charge, distance):
    return COULOMB_CONSTANT * charge / distance**2

def electric_potential_point_charge(charge, distance):
    return COULOMB_CONSTANT * charge / distance

def gauss_law_electric(enclosed_charge):
    return enclosed_charge / VACUUM_PERMITTIVITY

def capacitance_parallel_plate(area, distance):
    return VACUUM_PERMITTIVITY * area / distance

def capacitor_energy(capacitance, voltage):
    return 0.5 * capacitance * voltage**2

def ohms_law(voltage, resistance):
    return voltage / resistance

def power_electrical(voltage, current):
    return voltage * current

def power_resistive(current, resistance):
    return current**2 * resistance

def magnetic_force_moving_charge(charge, velocity, magnetic_field):
    return charge * velocity * magnetic_field

def magnetic_force_current_wire(current, length, magnetic_field):
    return current * length * magnetic_field

def biot_savart_law(current, length, distance):
    return VACUUM_PERMEABILITY * current * length / (4 * PI * distance**2)

def amperes_law(current_enclosed):
    return VACUUM_PERMEABILITY * current_enclosed

def faradays_law(magnetic_flux_change, time):
    return -magnetic_flux_change / time

def lenz_law_direction(flux_change):
    return -1 if flux_change > 0 else 1

def inductance_solenoid(turns, area, length):
    return VACUUM_PERMEABILITY * turns**2 * area / length

def inductor_energy(inductance, current):
    return 0.5 * inductance * current**2

def electromagnetic_wave_speed():
    return 1 / math.sqrt(VACUUM_PERMEABILITY * VACUUM_PERMITTIVITY)

def poynting_vector(electric_field, magnetic_field):
    return (electric_field * magnetic_field) / VACUUM_PERMEABILITY

def lorentz_force(charge, electric_field, velocity, magnetic_field):
    return charge * (electric_field + velocity * magnetic_field)

def cyclotron_frequency(charge, mass, magnetic_field):
    return charge * magnetic_field / mass

def hall_effect_voltage(current, magnetic_field, thickness, charge_density):
    return current * magnetic_field / (thickness * charge_density * ELEMENTARY_CHARGE)

def magnetic_dipole_moment(current, area):
    return current * area

def electric_dipole_moment(charge, separation):
    return charge * separation

def dielectric_constant(capacitance_with_dielectric, capacitance_vacuum):
    return capacitance_with_dielectric / capacitance_vacuum

def magnetic_permeability_relative(permeability_material):
    return permeability_material / VACUUM_PERMEABILITY

def electromagnetic_momentum(energy):
    return energy / SPEED_OF_LIGHT

def radiation_pressure(intensity):
    return intensity / SPEED_OF_LIGHT

def ac_impedance(resistance, reactance):
    return math.sqrt(resistance**2 + reactance**2)

def capacitive_reactance(capacitance, frequency):
    return 1 / (2 * PI * frequency * capacitance)

def inductive_reactance(inductance, frequency):
    return 2 * PI * frequency * inductance

def resonant_frequency_lc(inductance, capacitance):
    return 1 / (2 * PI * math.sqrt(inductance * capacitance))

def skin_depth(frequency, conductivity, permeability):
    return math.sqrt(2 / (2 * PI * frequency * conductivity * permeability))

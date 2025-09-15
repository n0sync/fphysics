import math
from ..constants import *

def conservation_of_energy(kinetic_initial, potential_initial, kinetic_final, potential_final):
    return kinetic_initial + potential_initial == kinetic_final + potential_final

def conservation_of_momentum_elastic(m1, v1i, m2, v2i):
    v1f = ((m1 - m2) * v1i + 2 * m2 * v2i) / (m1 + m2)
    v2f = ((m2 - m1) * v2i + 2 * m1 * v1i) / (m1 + m2)
    return v1f, v2f

def conservation_of_angular_momentum(I1, omega1, I2, omega2):
    return I1 * omega1 + I2 * omega2

def conservation_of_mass_flow(rho1, A1, v1, rho2, A2, v2):
    return rho1 * A1 * v1 == rho2 * A2 * v2

def conservation_of_charge(charge_initial, charge_final):
    return charge_initial == charge_final

def noether_theorem_energy(lagrangian, time):
    return lagrangian

def center_of_mass_velocity(masses, velocities):
    total_mass = sum(masses)
    momentum_sum = sum(m * v for m, v in zip(masses, velocities))
    return momentum_sum / total_mass

def reduced_mass_system(m1, m2):
    return (m1 * m2) / (m1 + m2)

def elastic_collision_energy_transfer(m1, m2, v1):
    return (4 * m1 * m2 * v1**2) / (m1 + m2)**2

def inelastic_collision_final_velocity(m1, v1, m2, v2):
    return (m1 * v1 + m2 * v2) / (m1 + m2)

def coefficient_of_restitution(v1f, v2f, v1i, v2i):
    return (v2f - v1f) / (v1i - v2i)

def impulse_momentum_change(force, time_interval):
    return force * time_interval

def angular_impulse(torque, time_interval):
    return torque * time_interval

def energy_dissipation_inelastic(m1, v1i, m2, v2i, vf):
    initial_ke = 0.5 * m1 * v1i**2 + 0.5 * m2 * v2i**2
    final_ke = 0.5 * (m1 + m2) * vf**2
    return initial_ke - final_ke

def conservation_of_baryon_number(initial_baryons, final_baryons):
    return initial_baryons == final_baryons

def conservation_of_lepton_number(initial_leptons, final_leptons):
    return initial_leptons == final_leptons


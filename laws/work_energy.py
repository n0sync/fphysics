import math
from constants import *

def work(force, displacement, angle=0):
    return force * displacement * math.cos(angle)

def kinetic_energy(mass, velocity):
    return 0.5 * mass * velocity**2

def potential_energy_gravitational(mass, height, gravity=EARTH_GRAVITY):
    return mass * gravity * height

def potential_energy_spring(spring_constant, displacement):
    return 0.5 * spring_constant * displacement**2

def potential_energy_gravitational_field(mass1, mass2, distance):
    return -GRAVITATIONAL_CONSTANT * mass1 * mass2 / distance

def work_kinetic_energy_theorem(initial_kinetic_energy, final_kinetic_energy):
    return final_kinetic_energy - initial_kinetic_energy

def power_from_work(work, time):
    return work / time

def power_from_force_velocity(force, velocity, angle=0):
    return force * velocity * math.cos(angle)

def elastic_collision_velocity_1d(mass1, mass2, initial_velocity1, initial_velocity2):
    v1_final = ((mass1 - mass2) * initial_velocity1 + 2 * mass2 * initial_velocity2) / (mass1 + mass2)
    v2_final = ((mass2 - mass1) * initial_velocity2 + 2 * mass1 * initial_velocity1) / (mass1 + mass2)
    return v1_final, v2_final

def inelastic_collision_velocity_1d(mass1, mass2, initial_velocity1, initial_velocity2):
    return (mass1 * initial_velocity1 + mass2 * initial_velocity2) / (mass1 + mass2)

def coefficient_of_restitution(relative_velocity_separation, relative_velocity_approach):
    return relative_velocity_separation / relative_velocity_approach

def mechanical_energy(kinetic_energy, potential_energy):
    return kinetic_energy + potential_energy

def efficiency(useful_output, total_input):
    return useful_output / total_input

def work_variable_force(force_function, displacement_initial, displacement_final, steps=1000):
    dx = (displacement_final - displacement_initial) / steps
    total_work = 0
    for i in range(steps):
        x = displacement_initial + i * dx
        total_work += force_function(x) * dx
    return total_work

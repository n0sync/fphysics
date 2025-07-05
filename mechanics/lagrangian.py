import math
from constants import *

def lagrangian(kinetic_energy, potential_energy):
    return kinetic_energy - potential_energy

def kinetic_energy_particle(mass, velocity):
    return 0.5 * mass * velocity**2

def kinetic_energy_rotating_body(moment_of_inertia, angular_velocity):
    return 0.5 * moment_of_inertia * angular_velocity**2

def kinetic_energy_generalized(masses, velocities):
    return 0.5 * sum(m * v**2 for m, v in zip(masses, velocities))

def potential_energy_gravitational(mass, height, gravity=EARTH_GRAVITY):
    return mass * gravity * height

def potential_energy_spring(spring_constant, displacement):
    return 0.5 * spring_constant * displacement**2

def euler_lagrange_equation(dL_dq, dL_dq_dot, q_ddot):
    return dL_dq - dL_dq_dot + q_ddot

def generalized_force(Q, q):
    return Q

def constraint_force(constraint_multiplier, constraint_gradient):
    return constraint_multiplier * constraint_gradient

def hamiltonian(generalized_momentum, generalized_coordinate, lagrangian_value):
    return generalized_momentum - lagrangian_value

def generalized_momentum(mass, velocity):
    return mass * velocity

def canonical_momentum(dL_dq_dot):
    return dL_dq_dot

def hamilton_equations_q_dot(dH_dp):
    return dH_dp

def hamilton_equations_p_dot(dH_dq):
    return -dH_dq

def action_integral(lagrangian_values, time_step):
    return sum(L * time_step for L in lagrangian_values)

def principle_of_least_action(action1, action2):
    return action1 < action2

def cyclic_coordinate_conserved_momentum(generalized_momentum):
    return generalized_momentum

def noether_theorem_energy_conservation(lagrangian_time_independent):
    return lagrangian_time_independent

def lagrange_multiplier_constraint(constraint_function, lambda_multiplier):
    return lambda_multiplier * constraint_function

def virtual_work_principle(virtual_displacement, force):
    return force * virtual_displacement

def dalembert_principle(mass, acceleration, applied_force):
    return applied_force - mass * acceleration

def pendulum_lagrangian(length, mass, angle, angle_dot, gravity=EARTH_GRAVITY):
    T = 0.5 * mass * (length * angle_dot)**2
    V = -mass * gravity * length * math.cos(angle)
    return T - V

def double_pendulum_lagrangian(m1, m2, L1, L2, theta1, theta2, theta1_dot, theta2_dot, gravity=EARTH_GRAVITY):
    x1 = L1 * math.sin(theta1)
    y1 = -L1 * math.cos(theta1)
    x2 = x1 + L2 * math.sin(theta2)
    y2 = y1 - L2 * math.cos(theta2)
    
    x1_dot = L1 * theta1_dot * math.cos(theta1)
    y1_dot = L1 * theta1_dot * math.sin(theta1)
    x2_dot = x1_dot + L2 * theta2_dot * math.cos(theta2)
    y2_dot = y1_dot + L2 * theta2_dot * math.sin(theta2)
    
    T1 = 0.5 * m1 * (x1_dot**2 + y1_dot**2)
    T2 = 0.5 * m2 * (x2_dot**2 + y2_dot**2)
    V1 = m1 * gravity * y1
    V2 = m2 * gravity * y2
    
    return (T1 + T2) - (V1 + V2)

def central_force_lagrangian(mass, r, r_dot, theta_dot, potential_function):
    T = 0.5 * mass * (r_dot**2 + r**2 * theta_dot**2)
    V = potential_function(r)
    return T - V

def oscillator_lagrangian(mass, displacement, velocity, spring_constant):
    T = 0.5 * mass * velocity**2
    V = 0.5 * spring_constant * displacement**2
    return T - V

def rigid_body_lagrangian(moment_of_inertia_tensor, angular_velocity_vector, kinetic_energy_translation, potential_energy):
    T_rot = 0.5 * sum(I * omega**2 for I, omega in zip(moment_of_inertia_tensor, angular_velocity_vector))
    return kinetic_energy_translation + T_rot - potential_energy

def field_lagrangian_density(field, field_gradient, field_time_derivative):
    return 0.5 * (field_time_derivative**2 - field_gradient**2)

def electromagnetic_lagrangian(charge, velocity, vector_potential, scalar_potential):
    interaction = charge * (velocity * vector_potential - scalar_potential)
    return interaction

def relativistic_particle_lagrangian(mass, velocity, c=SPEED_OF_LIGHT):
    gamma = 1 / math.sqrt(1 - (velocity / c)**2)
    return -mass * c**2 / gamma

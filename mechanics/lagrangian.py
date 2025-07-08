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

def generalized_coordinates(mass, velocities, gravities):
    return [0.5 * m * v**2 - m * g for m, v, g in zip(mass, velocities, gravities)]

def lagrangian_with_constraints(lagrangian, lagrange_multipliers, constraint_functions):
    return lagrangian - sum(l * f for l, f in zip(lagrange_multipliers, constraint_functions))

def canonical_angular_momentum(moment_of_inertia, angular_velocity):
    return moment_of_inertia * angular_velocity

def central_force_conservative(field_strength, displacement):
    return -field_strength * displacement

def relativistic_lagrangian(mass, velocity, c=SPEED_OF_LIGHT):
    gamma = 1 / math.sqrt(1 - (velocity / c)**2)
    return -mass * c**2 * (1 - gamma)

def spring_lagrangian(spring_constant, displacement):
    return 0.5 * spring_constant * displacement**2

def fluid_pendulum_lagrangian(density, volume, length, angle, angle_dot, gravity=EARTH_GRAVITY):
    T = 0.5 * density * volume * (length * angle_dot)**2
    V = -density * gravity * volume * length * math.cos(angle)
    return T - V

def electromagnetic_lagrangian_density(charge_density, current_density, vector_potential, scalar_potential):
    return charge_density * scalar_potential - sum(j * a for j, a in zip(current_density, vector_potential))

def central_potential_lagrangian(density, volume, radial_velocity, potential_energy_density):
    return 0.5 * density * volume * radial_velocity**2 - potential_energy_density

def lagrangian_isotropic_oscillator(mass, frequency, displacement, velocity):
    T = 0.5 * mass * velocity**2
    V = 0.5 * mass * frequency**2 * displacement**2
    return T - V

def lagrange_poincare(L, R, M, v, w):
    return L - 0.5 * v.transpose() @ M @ v - w @ R @ w

def relativistic_free_particle_lagrangian(mass, velocity):
    return -mass * SPEED_OF_LIGHT**2 * math.sqrt(1 - (velocity / SPEED_OF_LIGHT)**2)

def double_oscillator_lagrangian(m1, m2, k1, k2, x1, x2, x1_dot, x2_dot):
    T1 = 0.5 * m1 * x1_dot**2
    T2 = 0.5 * m2 * x2_dot**2
    V1 = 0.5 * k1 * x1**2
    V2 = 0.5 * k2 * (x2 - x1)**2
    return (T1 + T2) - (V1 + V2)

def gyroscope_lagrangian(I1, I2, I3, omega1, omega2, omega3):
    return 0.5 * (I1 * omega1**2 + I2 * omega2**2 + I3 * omega3**2)

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

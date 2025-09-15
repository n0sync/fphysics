import math
from ..constants import *

def newtons_first_law(net_force):
    return net_force == 0

def newtons_second_law(mass, acceleration):
    return mass * acceleration

def newtons_second_law_momentum(momentum_change, time_interval):
    return momentum_change / time_interval

def newtons_third_law_reaction(action_force):
    return -action_force

def gravitational_acceleration(mass, radius):
    return GRAVITATIONAL_CONSTANT * mass / radius**2

def normal_force_horizontal(mass, gravity=EARTH_GRAVITY):
    return mass * gravity

def normal_force_inclined(mass, angle, gravity=EARTH_GRAVITY):
    return mass * gravity * math.cos(angle)

def friction_force_static(normal_force, coefficient_static):
    return coefficient_static * normal_force

def friction_force_kinetic(normal_force, coefficient_kinetic):
    return coefficient_kinetic * normal_force

def tension_force_hanging(mass, acceleration, gravity=EARTH_GRAVITY):
    return mass * (gravity + acceleration)

def centripetal_acceleration(velocity, radius):
    return velocity**2 / radius

def centrifugal_force(mass, velocity, radius):
    return mass * velocity**2 / radius

def banked_curve_no_friction(radius, angle, gravity=EARTH_GRAVITY):
    return math.sqrt(radius * gravity * math.tan(angle))

def maximum_static_friction_incline(angle, coefficient_static):
    return math.tan(angle) <= coefficient_static

def net_force_components(forces_x, forces_y):
    net_fx = sum(forces_x)
    net_fy = sum(forces_y)
    return math.sqrt(net_fx**2 + net_fy**2)

def acceleration_on_incline(angle, coefficient_friction, gravity=EARTH_GRAVITY):
    return gravity * (math.sin(angle) - coefficient_friction * math.cos(angle))

def force_required_circular_motion(mass, velocity, radius):
    return mass * velocity**2 / radius

def apparent_weight_elevator(mass, acceleration, gravity=EARTH_GRAVITY):
    return mass * (gravity + acceleration)

def force_spring_system(spring_constant, compression):
    return spring_constant * compression

def terminal_velocity_drag(mass, drag_coefficient, density, area, gravity=EARTH_GRAVITY):
    return math.sqrt(2 * mass * gravity / (drag_coefficient * density * area))

def atwood_machine_acceleration(m1, m2, gravity=EARTH_GRAVITY):
    return abs(m1 - m2) * gravity / (m1 + m2)

def atwood_machine_tension(m1, m2, gravity=EARTH_GRAVITY):
    return 2 * m1 * m2 * gravity / (m1 + m2)

def rocket_equation(exhaust_velocity, mass_initial, mass_final):
    return exhaust_velocity * math.log(mass_initial / mass_final)

def impulse_from_force_time(force, time):
    return force * time

def average_force_collision(mass, velocity_change, time_collision):
    return mass * velocity_change / time_collision


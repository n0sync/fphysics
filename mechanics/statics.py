import math
from constants import *

def static_equilibrium_forces(*forces):
    sum_fx = sum(force[0] for force in forces)
    sum_fy = sum(force[1] for force in forces)
    return abs(sum_fx) < 1e-10 and abs(sum_fy) < 1e-10

def static_equilibrium_torques(*torques):
    return abs(sum(torques)) < 1e-10

def center_of_gravity_2d(masses, positions):
    total_mass = sum(masses)
    x_cg = sum(m * pos[0] for m, pos in zip(masses, positions)) / total_mass
    y_cg = sum(m * pos[1] for m, pos in zip(masses, positions)) / total_mass
    return x_cg, y_cg

def center_of_gravity_3d(masses, positions):
    total_mass = sum(masses)
    x_cg = sum(m * pos[0] for m, pos in zip(masses, positions)) / total_mass
    y_cg = sum(m * pos[1] for m, pos in zip(masses, positions)) / total_mass
    z_cg = sum(m * pos[2] for m, pos in zip(masses, positions)) / total_mass
    return x_cg, y_cg, z_cg

def reaction_force_simple_beam(load, load_position, beam_length):
    R2 = load * load_position / beam_length
    R1 = load - R2
    return R1, R2

def reaction_force_cantilever(load, load_position):
    return load, load * load_position

def distributed_load_resultant(load_per_unit, length):
    return load_per_unit * length, length / 2

def truss_member_force_2d(joint_forces, member_angles):
    if len(member_angles) == 2:
        Fx, Fy = joint_forces[0]
        angle1, angle2 = member_angles
        
        cos1, sin1 = math.cos(angle1), math.sin(angle1)
        cos2, sin2 = math.cos(angle2), math.sin(angle2)
        
        determinant = cos1 * sin2 - cos2 * sin1
        if abs(determinant) < 1e-10:
            raise ValueError("Members are parallel")
        
        F1 = (Fx * sin2 - Fy * cos2) / determinant
        F2 = (Fy * cos1 - Fx * sin1) / determinant
        return [F1, F2]
    else:
        raise NotImplementedError("Only two-member joints supported")

def stability_factor_column(length, area, moment_of_inertia, elastic_modulus):
    return (PI**2 * elastic_modulus * moment_of_inertia) / length**2

def factor_of_safety(ultimate_strength, working_stress):
    return ultimate_strength / working_stress

def angle_of_repose(coefficient_of_friction):
    return math.atan(coefficient_of_friction)

def sliding_condition(normal_force, applied_force, friction_coefficient):
    return applied_force > friction_coefficient * normal_force

def tipping_condition(applied_force, force_height, weight, base_width):
    overturning_moment = applied_force * force_height
    restoring_moment = weight * base_width / 2
    return overturning_moment > restoring_moment

def pulley_system_advantage(num_supporting_ropes):
    return num_supporting_ropes

def lever_mechanical_advantage(effort_arm, load_arm):
    return effort_arm / load_arm

def inclined_plane_advantage(length, height):
    return length / height

def screw_mechanical_advantage(pitch, lever_arm):
    return (2 * PI * lever_arm) / pitch

def wedge_mechanical_advantage(length, thickness):
    return length / thickness

def wheel_and_axle_advantage(wheel_radius, axle_radius):
    return wheel_radius / axle_radius

def moment_of_inertia_rectangle(width, height):
    return width * height**3 / 12

def moment_of_inertia_circle(radius):
    return PI * radius**4 / 4

def moment_of_inertia_triangle(base, height):
    return base * height**3 / 36

def centroid_composite_area(areas, centroids):
    total_area = sum(areas)
    x_c = sum(A * x for A, (x, y) in zip(areas, centroids)) / total_area
    y_c = sum(A * y for A, (x, y) in zip(areas, centroids)) / total_area
    return x_c, y_c

def parallel_axis_theorem(I_centroid, area, distance):
    return I_centroid + area * distance**2

def section_modulus(moment_of_inertia, distance_from_neutral):
    return moment_of_inertia / distance_from_neutral

def shear_flow(shear_force, first_moment, moment_of_inertia):
    return shear_force * first_moment / moment_of_inertia

def cable_tension_distributed_load(load_per_unit, span, sag):
    return load_per_unit * span**2 / (8 * sag)

def cable_length_parabolic(span, sag):
    return span * (1 + (8 * sag**2) / (3 * span**2))

def arch_thrust(load, span, rise):
    return load * span / (8 * rise)

def friction_angle(friction_coefficient):
    return math.atan(friction_coefficient)

def wedge_friction_force(normal_force, wedge_angle, friction_coefficient):
    return normal_force * (math.sin(wedge_angle) + friction_coefficient * math.cos(wedge_angle))

def belt_friction_tension(T1, friction_coefficient, wrap_angle):
    return T1 * math.exp(friction_coefficient * wrap_angle)

def hydrostatic_pressure(density, height, gravity=EARTH_GRAVITY):
    return density * gravity * height

def hydrostatic_force_on_surface(pressure, area):
    return pressure * area

def buoyant_force(fluid_density, displaced_volume, gravity=EARTH_GRAVITY):
    return fluid_density * gravity * displaced_volume

def stability_metacentric_height(center_of_buoyancy, center_of_gravity):
    return center_of_buoyancy - center_of_gravity

def plastic_section_modulus_rectangle(width, height):
    return width * height**2 / 4

def plastic_moment_capacity(yield_strength, plastic_section_modulus):
    return yield_strength * plastic_section_modulus

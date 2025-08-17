def moment_of_inertia_point_mass(mass, radius):
    return mass * radius**2

def moment_of_inertia_rod_center(mass, length):
    return mass * length**2 / 12

def moment_of_inertia_rod_end(mass, length):
    return mass * length**2 / 3

def moment_of_inertia_disk(mass, radius):
    return 0.5 * mass * radius**2

def moment_of_inertia_ring(mass, radius):
    return mass * radius**2

def moment_of_inertia_sphere_solid(mass, radius):
    return 0.4 * mass * radius**2

def moment_of_inertia_sphere_hollow(mass, radius):
    return (2/3) * mass * radius**2

def moment_of_inertia_cylinder_solid(mass, radius):
    return 0.5 * mass * radius**2

def moment_of_inertia_cylinder_hollow(mass, inner_radius, outer_radius):
    return 0.5 * mass * (outer_radius**2 + inner_radius**2)

def parallel_axis_theorem(moment_of_inertia_cm, mass, distance):
    return moment_of_inertia_cm + mass * distance**2

def torque(force, lever_arm):
    return force * lever_arm

def torque_from_moment_of_inertia(moment_of_inertia, angular_acceleration):
    return moment_of_inertia * angular_acceleration

def angular_momentum(moment_of_inertia, angular_velocity):
    return moment_of_inertia * angular_velocity

def angular_momentum_point_mass(mass, velocity, radius):
    return mass * velocity * radius

def rotational_kinetic_energy(moment_of_inertia, angular_velocity):
    return 0.5 * moment_of_inertia * angular_velocity**2

def rolling_motion_velocity(angular_velocity, radius):
    return angular_velocity * radius

def rolling_motion_acceleration(angular_acceleration, radius):
    return angular_acceleration * radius

def rolling_kinetic_energy(mass, velocity, moment_of_inertia, angular_velocity):
    return 0.5 * mass * velocity**2 + 0.5 * moment_of_inertia * angular_velocity**2

def gyroscopic_precession_frequency(torque, angular_momentum):
    return torque / angular_momentum

def rotational_work(torque, angular_displacement):
    return torque * angular_displacement

def rotational_power(torque, angular_velocity):
    return torque * angular_velocity

def precession_rate(torque, angular_momentum):
    return torque / angular_momentum

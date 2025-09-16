import math
from ..constants import *


def displacement(initial_position, velocity, time, acceleration=0):
    return initial_position + velocity * time + 0.5 * acceleration * time**2

def velocity_from_acceleration(initial_velocity, acceleration, time):
    return initial_velocity + acceleration * time

def velocity_from_displacement(initial_velocity, acceleration, displacement):
    return math.sqrt(initial_velocity**2 + 2 * acceleration * displacement)

def average_velocity(initial_velocity, final_velocity):
    return (initial_velocity + final_velocity) / 2

def acceleration_from_velocity(initial_velocity, final_velocity, time):
    return (final_velocity - initial_velocity) / time

def projectile_range(initial_velocity, angle, height=0):
    g = EARTH_GRAVITY
    sin_2theta = math.sin(2 * angle)
    cos_theta = math.cos(angle)
    sin_theta = math.sin(angle)
    
    if height == 0:
        return initial_velocity**2 * sin_2theta / g
    else:
        return (initial_velocity * cos_theta / g) * (initial_velocity * sin_theta + math.sqrt((initial_velocity * sin_theta)**2 + 2 * g * height))

def projectile_max_height(initial_velocity, angle):
    return (initial_velocity * math.sin(angle))**2 / (2 * EARTH_GRAVITY)

def projectile_time_of_flight(initial_velocity, angle, height=0):
    g = EARTH_GRAVITY
    sin_theta = math.sin(angle)
    
    if height == 0:
        return 2 * initial_velocity * sin_theta / g
    else:
        return (initial_velocity * sin_theta + math.sqrt((initial_velocity * sin_theta)**2 + 2 * g * height)) / g

def circular_velocity(radius, period):
    return 2 * PI * radius / period

def centripetal_acceleration(velocity, radius):
    return velocity**2 / radius

def angular_velocity(angle, time):
    return angle / time

def angular_acceleration(initial_angular_velocity, final_angular_velocity, time):
    return (final_angular_velocity - initial_angular_velocity) / time

def angular_displacement(initial_angular_velocity, time, angular_acceleration=0):
    return initial_angular_velocity * time + 0.5 * angular_acceleration * time**2



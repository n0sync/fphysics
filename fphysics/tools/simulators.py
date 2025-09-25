from ..constants import *
import numpy as np
from typing import List, Tuple

def simulate_projectile_motion(initial_velocity, angle, height=0, time_step=0.01):
    vx = initial_velocity * np.cos(np.radians(angle))
    vy = initial_velocity * np.sin(np.radians(angle))
    
    x, y = 0, height
    positions = [(x, y)]
    
    while y >= 0:
        x += vx * time_step
        y += vy * time_step - 0.5 * GRAVITY * time_step**2
        vy -= GRAVITY * time_step
        positions.append((x, y))
    
    return positions

def simulate_pendulum(length, initial_angle, time_duration=10, time_step=0.01):
    theta = initial_angle
    omega = 0
    
    times = np.arange(0, time_duration, time_step)
    angles = []
    
    for t in times:
        theta += omega * time_step
        omega -= (GRAVITY / length) * np.sin(theta) * time_step
        angles.append(theta)
    
    return times, angles

def simulate_spring_mass_system(mass, spring_constant, initial_displacement, time_duration=10, time_step=0.01):
    x = initial_displacement
    v = 0
    
    times = np.arange(0, time_duration, time_step)
    positions = []
    
    for t in times:
        acceleration = -spring_constant * x / mass
        v += acceleration * time_step
        x += v * time_step
        positions.append(x)
    
    return times, positions

def simulate_orbital_motion(central_mass, orbital_mass, initial_position, initial_velocity, time_duration=100, time_step=0.01):
    positions = [initial_position]
    velocities = [initial_velocity]
    
    x, y = initial_position
    vx, vy = initial_velocity
    
    times = np.arange(0, time_duration, time_step)
    
    for t in times[1:]:
        r = np.sqrt(x**2 + y**2)
        force_magnitude = GRAVITATIONAL_CONSTANT * central_mass * orbital_mass / r**2
        
        fx = -force_magnitude * x / r
        fy = -force_magnitude * y / r
        
        ax = fx / orbital_mass
        ay = fy / orbital_mass
        
        vx += ax * time_step
        vy += ay * time_step
        
        x += vx * time_step
        y += vy * time_step
        
        positions.append((x, y))
        velocities.append((vx, vy))
    
    return times, positions, velocities

def simulate_wave_propagation(amplitude, frequency, wavelength, time_duration=5, space_points=100, time_step=0.01):
    x_points = np.linspace(0, wavelength * 3, space_points)
    times = np.arange(0, time_duration, time_step)
    
    wave_data = []
    
    for t in times:
        wave = amplitude * np.sin(2 * np.pi * (frequency * t - x_points / wavelength))
        wave_data.append(wave)
    
    return x_points, times, wave_data

def simulate_collision(mass1, velocity1, mass2, velocity2, restitution=1.0):
    total_momentum = mass1 * velocity1 + mass2 * velocity2
    relative_velocity = velocity1 - velocity2
    
    if mass1 + mass2 == 0:
        return velocity1, velocity2
    
    new_velocity1 = velocity1 - (2 * mass2 / (mass1 + mass2)) * relative_velocity * restitution
    new_velocity2 = velocity2 + (2 * mass1 / (mass1 + mass2)) * relative_velocity * restitution
    
    return new_velocity1, new_velocity2

def simulate_electric_field(charges_positions, test_charge_position, grid_size=50):
    x = np.linspace(-10, 10, grid_size)
    y = np.linspace(-10, 10, grid_size)
    X, Y = np.meshgrid(x, y)
    
    Ex = np.zeros_like(X)
    Ey = np.zeros_like(Y)
    
    for charge, (qx, qy) in charges_positions:
        dx = X - qx
        dy = Y - qy
        r = np.sqrt(dx**2 + dy**2)
        r = np.where(r < 0.1, 0.1, r)
        
        field_magnitude = COULOMB_CONSTANT * charge / r**2
        Ex += field_magnitude * dx / r
        Ey += field_magnitude * dy / r
    
    return X, Y, Ex, Ey

def simulate_radioactive_decay(initial_quantity, decay_constant, time_duration=100, time_step=0.1):
    times = np.arange(0, time_duration, time_step)
    quantities = []
    
    current_quantity = initial_quantity
    
    for t in times:
        quantities.append(current_quantity)
        current_quantity = initial_quantity * np.exp(-decay_constant * t)
    
    return times, quantities

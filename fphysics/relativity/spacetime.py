import math
import numpy as np
from constants import *


def minkowski_metric():
    """Return Minkowski metric tensor"""
    return np.diag([-1, 1, 1, 1])


def schwarzschild_metric(mass, r, theta=0):
    """Return Schwarzschild metric components"""
    rs = 2 * GRAVITATIONAL_CONSTANT * mass / SPEED_OF_LIGHT**2
    g_tt = -(1 - rs/r)
    g_rr = 1 / (1 - rs/r)
    g_theta = r**2
    g_phi = r**2 * math.sin(theta)**2
    return np.diag([g_tt, g_rr, g_theta, g_phi])


def proper_distance(metric, dx):
    """Calculate proper distance from metric and coordinate differences"""
    return math.sqrt(np.dot(dx, np.dot(metric, dx)))


def geodesic_equation(mass, r, dr_dt, d_theta_dt):
    """Simplified geodesic equation for radial motion"""
    rs = 2 * GRAVITATIONAL_CONSTANT * mass / SPEED_OF_LIGHT**2
    acceleration = -rs * SPEED_OF_LIGHT**2 / (2 * r**2 * (1 - rs/r))
    return acceleration


def four_velocity(velocity_3d, c=SPEED_OF_LIGHT):
    """Calculate four-velocity from 3D velocity"""
    gamma = 1 / math.sqrt(1 - np.dot(velocity_3d, velocity_3d) / c**2)
    u0 = gamma * c
    u_spatial = gamma * velocity_3d
    return np.array([u0, *u_spatial])


def spacetime_interval(dt, dx, dy, dz, c=SPEED_OF_LIGHT):
    """Calculate spacetime interval"""
    return -c**2 * dt**2 + dx**2 + dy**2 + dz**2


def light_cone_constraint(dt, dx, dy, dz, c=SPEED_OF_LIGHT):
    """Check if event is within light cone"""
    ds2 = spacetime_interval(dt, dx, dy, dz, c)
    return ds2 <= 0  # Timelike or null


def coordinate_transformation_lorentz(x, t, velocity):
    """Lorentz coordinate transformation"""
    gamma = 1 / math.sqrt(1 - (velocity / SPEED_OF_LIGHT)**2)
    x_prime = gamma * (x - velocity * t)
    t_prime = gamma * (t - velocity * x / SPEED_OF_LIGHT**2)
    return x_prime, t_prime


def riemann_curvature_scalar(mass, radius):
    """Calculate scalar curvature for Schwarzschild spacetime"""
    rs = 2 * GRAVITATIONAL_CONSTANT * mass / SPEED_OF_LIGHT**2
    return 12 * rs / radius**3 if radius > rs else float('inf')

import numpy as np
import matplotlib.pyplot as plt
from ..constants import *

# Projectile Motion Example
def projectile_motion_demo():
    v0 = 50  # Initial velocity (m/s)
    angle = 45  # Launch angle (degrees)
    
    vx0 = v0 * np.cos(np.radians(angle))
    vy0 = v0 * np.sin(np.radians(angle))
    
    # Time of flight
    t_flight = 2 * vy0 / EARTH_GRAVITY
    t = np.linspace(0, t_flight, 100)
    
    # Position equations
    x = vx0 * t
    y = vy0 * t - 0.5 * EARTH_GRAVITY * t**2
    
    max_range = vx0 * t_flight
    max_height = vy0**2 / (2 * EARTH_GRAVITY)
    
    print(f"Projectile Motion Results:")
    print(f"Maximum Range: {max_range:.2f} m")
    print(f"Maximum Height: {max_height:.2f} m")
    print(f"Time of Flight: {t_flight:.2f} s")
    
    return t, x, y

# Collision Example
def elastic_collision_demo():
    m1, m2 = 2.0, 3.0  # masses (kg)
    v1i, v2i = 10.0, -5.0  # initial velocities (m/s)
    
    # Conservation of momentum and energy for elastic collision
    v1f = ((m1 - m2) * v1i + 2 * m2 * v2i) / (m1 + m2)
    v2f = ((m2 - m1) * v2i + 2 * m1 * v1i) / (m1 + m2)
    
    # Energy check
    ke_initial = 0.5 * m1 * v1i**2 + 0.5 * m2 * v2i**2
    ke_final = 0.5 * m1 * v1f**2 + 0.5 * m2 * v2f**2
    
    print(f"\nElastic Collision Results:")
    print(f"Initial velocities: v1={v1i} m/s, v2={v2i} m/s")
    print(f"Final velocities: v1={v1f:.2f} m/s, v2={v2f:.2f} m/s")
    print(f"Energy conservation: {abs(ke_initial - ke_final) < 1e-10}")

# Orbital Mechanics Example
def orbital_mechanics_demo():
    r = 400e3 + EARTH_RADIUS  # Altitude 400km above Earth
    
    # Orbital velocity for circular orbit
    v_orbital = np.sqrt(GRAVITATIONAL_CONSTANT * EARTH_MASS / r)
    period = 2 * PI * r / v_orbital
    
    # Escape velocity
    v_escape = np.sqrt(2 * GRAVITATIONAL_CONSTANT * EARTH_MASS / r)
    
    print(f"\nOrbital Mechanics Results:")
    print(f"Orbital radius: {r/1000:.0f} km")
    print(f"Orbital velocity: {v_orbital/1000:.2f} km/s")
    print(f"Orbital period: {period/3600:.2f} hours")
    print(f"Escape velocity: {v_escape/1000:.2f} km/s")

# Pendulum Motion
def pendulum_demo():
    L = 1.0  # length (m)
    theta0 = 0.2  # initial angle (radians)
    
    # Small angle approximation
    omega = np.sqrt(EARTH_GRAVITY / L)
    period = 2 * PI / omega
    
    t = np.linspace(0, 2 * period, 200)
    theta = theta0 * np.cos(omega * t)
    
    print(f"\nPendulum Motion Results:")
    print(f"Length: {L} m")
    print(f"Period: {period:.3f} s")
    print(f"Frequency: {1/period:.3f} Hz")
    
    return t, theta

if __name__ == "__main__":
    print("=== Mechanics Examples ===")
    
    # Run demonstrations
    t_proj, x_proj, y_proj = projectile_motion_demo()
    elastic_collision_demo()
    orbital_mechanics_demo()
    t_pend, theta_pend = pendulum_demo()
    
    # Simple plotting
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(12, 10))
    
    # Projectile trajectory
    ax1.plot(x_proj, y_proj)
    ax1.set_xlabel('Distance (m)')
    ax1.set_ylabel('Height (m)')
    ax1.set_title('Projectile Motion')
    ax1.grid(True)
    
    # Pendulum motion
    ax2.plot(t_pend, np.degrees(theta_pend))
    ax2.set_xlabel('Time (s)')
    ax2.set_ylabel('Angle (degrees)')
    ax2.set_title('Pendulum Oscillation')
    ax2.grid(True)
    
    plt.tight_layout()
    plt.show()


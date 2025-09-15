import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D
from ..constants import *

# Electric Field Visualization
def plot_electric_field():
    print("=== Electric Field Visualization ===")
    
    # Two point charges
    q1, q2 = 1e-9, -1e-9  # Coulombs
    x1, y1 = -0.5, 0  # Position of q1
    x2, y2 = 0.5, 0   # Position of q2
    
    # Create grid
    x = np.linspace(-2, 2, 20)
    y = np.linspace(-2, 2, 20)
    X, Y = np.meshgrid(x, y)
    
    # Calculate electric field
    r1_sq = (X - x1)**2 + (Y - y1)**2
    r2_sq = (X - x2)**2 + (Y - y2)**2
    
    # Avoid division by zero
    r1_sq = np.where(r1_sq == 0, 1e-10, r1_sq)
    r2_sq = np.where(r2_sq == 0, 1e-10, r2_sq)
    
    Ex1 = COULOMB_CONSTANT * q1 * (X - x1) / r1_sq**(3/2)
    Ey1 = COULOMB_CONSTANT * q1 * (Y - y1) / r1_sq**(3/2)
    
    Ex2 = COULOMB_CONSTANT * q2 * (X - x2) / r2_sq**(3/2)
    Ey2 = COULOMB_CONSTANT * q2 * (Y - y2) / r2_sq**(3/2)
    
    Ex_total = Ex1 + Ex2
    Ey_total = Ey1 + Ey2
    
    # Plot
    plt.figure(figsize=(10, 8))
    plt.quiver(X, Y, Ex_total, Ey_total, alpha=0.7)
    
    # Mark charges
    plt.plot(x1, y1, 'ro', markersize=10, label='Positive charge')
    plt.plot(x2, y2, 'bo', markersize=10, label='Negative charge')
    
    plt.xlabel('x (m)')
    plt.ylabel('y (m)')
    plt.title('Electric Field of Two Point Charges')
    plt.legend()
    plt.axis('equal')
    plt.grid(True, alpha=0.3)
    plt.show()

# Wave Interference
def plot_wave_interference():
    print("\n=== Wave Interference ===")
    
    # Parameters
    lambda_wave = 1.0  # wavelength
    k = 2 * PI / lambda_wave  # wave number
    omega = 2 * PI  # angular frequency
    
    # Spatial grid
    x = np.linspace(-5, 5, 500)
    t_vals = [0, PI/4, PI/2, 3*PI/4]
    
    plt.figure(figsize=(12, 8))
    
    for i, t in enumerate(t_vals):
        plt.subplot(2, 2, i+1)
        
        # Two waves with slight phase difference
        y1 = np.sin(k * x - omega * t)
        y2 = np.sin(k * x - omega * t + PI/3)
        y_sum = y1 + y2
        
        plt.plot(x, y1, 'b--', alpha=0.7, label='Wave 1')
        plt.plot(x, y2, 'r--', alpha=0.7, label='Wave 2')
        plt.plot(x, y_sum, 'k-', linewidth=2, label='Sum')
        
        plt.xlabel('Position')
        plt.ylabel('Amplitude')
        plt.title(f't = {t:.2f}')
        plt.legend()
        plt.grid(True, alpha=0.3)
        plt.ylim(-3, 3)
    
    plt.tight_layout()
    plt.show()

# Orbital Trajectories
def plot_orbital_trajectories():
    print("\n=== Orbital Trajectories ===")
    
    # Different eccentricities
    eccentricities = [0, 0.3, 0.6, 0.9]
    
    plt.figure(figsize=(12, 10))
    
    for i, e in enumerate(eccentricities):
        plt.subplot(2, 2, i+1)
        
        # Parametric equations for ellipse
        theta = np.linspace(0, 2*PI, 1000)
        a = 1.0  # semi-major axis
        b = a * np.sqrt(1 - e**2)  # semi-minor axis
        
        r = a * (1 - e**2) / (1 + e * np.cos(theta))
        x = r * np.cos(theta)
        y = r * np.sin(theta)
        
        plt.plot(x, y, 'b-', linewidth=2)
        plt.plot(0, 0, 'yo', markersize=10, label='Focus')  # Focus at origin
        plt.plot(a*e, 0, 'ro', markersize=8, label='Center')
        
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title(f'Eccentricity e = {e}')
        plt.axis('equal')
        plt.grid(True, alpha=0.3)
        plt.legend()
    
    plt.tight_layout()
    plt.show()

# Energy Level Diagram
def plot_energy_levels():
    print("\n=== Hydrogen Energy Level Diagram ===")
    
    plt.figure(figsize=(10, 8))
    
    # Hydrogen energy levels
    n_max = 6
    energies = []
    
    for n in range(1, n_max + 1):
        E_n = -13.6057 / n**2  # eV
        energies.append(E_n)
        
        # Draw energy level
        plt.hlines(E_n, 0, 2, colors='blue', linewidth=3)
        plt.text(2.1, E_n, f'n={n}, E={E_n:.2f} eV', 
                verticalalignment='center', fontsize=10)
    
    # Draw transitions (Balmer series)
    balmer_transitions = [(3, 2), (4, 2), (5, 2), (6, 2)]
    colors = ['red', 'cyan', 'blue', 'violet']
    
    for i, (ni, nf) in enumerate(balmer_transitions):
        Ei = energies[ni-1]
        Ef = energies[nf-1]
        
        # Arrow for transition
        plt.annotate('', xy=(1.5, Ef), xytext=(1.5, Ei),
                    arrowprops=dict(arrowstyle='->', color=colors[i], lw=2))
        
        # Calculate wavelength
        E_photon = Ei - Ef
        lambda_nm = 1240 / E_photon  # nm (using hc = 1240 eV·nm)
        
        plt.text(1.0, (Ei + Ef)/2, f'{lambda_nm:.0f} nm', 
                rotation=90, verticalalignment='center', color=colors[i])
    
    plt.xlim(0, 3)
    plt.ylim(-15, 1)
    plt.ylabel('Energy (eV)')
    plt.title('Hydrogen Atom Energy Levels and Balmer Series')
    plt.axhline(0, color='black', linestyle='--', alpha=0.5, label='Ionization')
    plt.grid(True, alpha=0.3)
    plt.show()

# Phase Space Plot
def plot_phase_space():
    print("\n=== Harmonic Oscillator Phase Space ===")
    
    # Parameters
    omega = 2 * PI  # angular frequency
    
    # Different energy levels
    energies = [0.5, 1.0, 1.5, 2.0]
    
    plt.figure(figsize=(10, 8))
    
    for E in energies:
        # Phase space trajectory (ellipse)
        theta = np.linspace(0, 2*PI, 1000)
        
        # x_max = sqrt(2E), p_max = sqrt(2E) for normalized units
        x_max = np.sqrt(2 * E)
        p_max = np.sqrt(2 * E)
        
        x = x_max * np.cos(theta)
        p = p_max * np.sin(theta)
        
        plt.plot(x, p, linewidth=2, label=f'E = {E}')
    
    plt.xlabel('Position x')
    plt.ylabel('Momentum p')
    plt.title('Harmonic Oscillator Phase Space Trajectories')
    plt.legend()
    plt.axis('equal')
    plt.grid(True, alpha=0.3)
    plt.show()

# Magnetic Field Lines
def plot_magnetic_field():
    print("\n=== Magnetic Field of Current Loop ===")
    
    # Current loop parameters
    I = 1.0  # Current (A)
    R = 1.0  # Loop radius (m)
    
    # Create cylindrical coordinate system
    rho = np.linspace(0.1, 3, 15)
    z = np.linspace(-3, 3, 15)
    RHO, Z = np.meshgrid(rho, z)
    
    # Simplified field calculation (approximate)
    # Exact calculation requires elliptic integrals
    
    # On-axis field (exact)
    B_z_axis = (VACUUM_PERMEABILITY * I * R**2) / (2 * (R**2 + Z**2)**(3/2))
    
    # Approximate off-axis field
    factor = 1 / (RHO**2 + Z**2 + R**2)**(3/2)
    B_rho = VACUUM_PERMEABILITY * I * Z * factor
    B_z = VACUUM_PERMEABILITY * I * R**2 * factor
    
    fig = plt.figure(figsize=(12, 8))
    
    # 2D field plot
    ax1 = plt.subplot(121)
    plt.streamplot(RHO, Z, B_rho, B_z, density=1.5, color='blue')
    
    # Draw current loop
    theta_loop = np.linspace(0, 2*PI, 100)
    x_loop = R * np.cos(theta_loop)
    y_loop = R * np.sin(theta_loop)
    plt.plot(R*np.ones(10), np.zeros(10), 'ro', markersize=8)
    plt.text(R+0.1, 0, 'I', fontsize=12, color='red')
    
    plt.xlabel('ρ (m)')
    plt.ylabel('z (m)')
    plt.title('Magnetic Field Lines of Current Loop')
    plt.axis('equal')
    plt.grid(True, alpha=0.3)
    
    # 3D visualization
    ax2 = plt.subplot(122, projection='3d')
    
    # Create 3D current loop
    theta = np.linspace(0, 2*PI, 100)
    x_3d = R * np.cos(theta)
    y_3d = R * np.sin(theta)
    z_3d = np.zeros_like(theta)
    
    ax2.plot(x_3d, y_3d, z_3d, 'r-', linewidth=4, label='Current Loop')
    
    # Add some field lines (simplified)
    for z_line in [-2, -1, 1, 2]:
        r_line = np.linspace(0.2, 2.5, 50)
        theta_line = np.zeros_like(r_line)
        x_line = r_line * np.cos(theta_line)
        y_line = r_line * np.sin(theta_line)
        z_line_arr = z_line * np.ones_like(r_line)
        
        ax2.plot(x_line, y_line, z_line_arr, 'b-', alpha=0.6)
        ax2.plot(-x_line, y_line, z_line_arr, 'b-', alpha=0.6)
    
    ax2.set_xlabel('x (m)')
    ax2.set_ylabel('y (m)')
    ax2.set_zlabel('z (m)')
    ax2.set_title('3D Current Loop')
    
    plt.tight_layout()
    plt.show()

# Wave Packet Animation
def create_wave_packet_animation():
    print("\n=== Wave Packet Animation ===")
    print("Creating animated wave packet... Close window to continue.")
    
    # Parameters
    x = np.linspace(-10, 10, 500)
    k0 = 2.0  # Central wave number
    sigma = 1.0  # Packet width
    omega0 = k0**2 / 2  # Dispersion relation for free particle
    
    fig, ax = plt.subplots(figsize=(12, 6))
    line_real, = ax.plot([], [], 'b-', label='Real part')
    line_imag, = ax.plot([], [], 'r--', label='Imaginary part')
    line_abs, = ax.plot([], [], 'k-', linewidth=2, label='|ψ|²')
    
    ax.set_xlim(-10, 10)
    ax.set_ylim(-1.5, 1.5)
    ax.set_xlabel('Position')
    ax.set_ylabel('Amplitude')
    ax.set_title('Dispersing Wave Packet')
    ax.legend()
    ax.grid(True, alpha=0.3)
    
    def animate(frame):
        t = frame * 0.1
        
        # Wave packet with dispersion
        psi = np.exp(1j * (k0 * x - omega0 * t)) * np.exp(-(x - k0 * t)**2 / (2 * sigma**2 * (1 + 1j * t / sigma**2)))
        
        line_real.set_data(x, np.real(psi))
        line_imag.set_data(x, np.imag(psi))
        line_abs.set_data(x, np.abs(psi)**2)
        
        return line_real, line_imag, line_abs
    
    ani = FuncAnimation(fig, animate, frames=100, interval=50, blit=True)
    plt.show()

if __name__ == "__main__":
    print("=== Physics Visualization Examples ===")
    
    # Static plots
    plot_electric_field()
    plot_wave_interference()
    plot_orbital_trajectories()
    plot_energy_levels()
    plot_phase_space()
    plot_magnetic_field()
    
    # Animation (uncomment to run)
    # create_wave_packet_animation()


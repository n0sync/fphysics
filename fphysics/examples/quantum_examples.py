import numpy as np
import matplotlib.pyplot as plt
from ..constants import *

# Particle in a Box
def particle_in_box_demo():
    L = 1e-9  # Box length (1 nm)
    n_levels = 5
    
    print("=== Particle in a Box ===")
    print(f"Box length: {L*1e9:.1f} nm")
    
    for n in range(1, n_levels + 1):
        # Energy levels
        E_n = (n**2 * PLANCK_CONSTANT**2) / (8 * ELECTRON_MASS * L**2)
        E_eV = E_n / ELECTRON_VOLT
        
        # Wavelength
        lambda_n = 2 * L / n
        
        print(f"n={n}: E={E_eV:.3f} eV, λ={lambda_n*1e9:.3f} nm")
    
    # Wave function for n=1,2,3
    x = np.linspace(0, L, 1000)
    
    psi_data = []
    for n in [1, 2, 3]:
        psi = np.sqrt(2/L) * np.sin(n * PI * x / L)
        psi_data.append((n, x, psi))
    
    return psi_data, L

# Harmonic Oscillator
def harmonic_oscillator_demo():
    m = ELECTRON_MASS
    omega = 1e15  # Angular frequency (rad/s)
    n_levels = 4
    
    print("\n=== Quantum Harmonic Oscillator ===")
    print(f"Frequency: {omega/1e15:.1f} × 10¹⁵ rad/s")
    
    # Energy levels
    for n in range(n_levels):
        E_n = REDUCED_PLANCK * omega * (n + 0.5)
        E_eV = E_n / ELECTRON_VOLT
        print(f"n={n}: E={E_eV:.4f} eV")
    
    # Classical turning points for ground state
    E_0 = 0.5 * REDUCED_PLANCK * omega
    x_tp = np.sqrt(2 * E_0 / (m * omega**2))
    
    print(f"Ground state turning point: {x_tp*1e12:.2f} pm")
    
    return E_0, x_tp

# Hydrogen Atom Energy Levels
def hydrogen_atom_demo():
    print("\n=== Hydrogen Atom Energy Levels ===")
    
    for n in range(1, 6):
        # Bohr model energy levels
        E_n = -RYDBERG_CONSTANT * HC_IN_MEV_FM / n**2
        E_eV = E_n * 1e6 / ELECTRON_VOLT  # Convert from MeV·fm to eV
        
        # More direct calculation
        E_n_direct = -13.6057 / n**2  # eV
        
        print(f"n={n}: E={E_n_direct:.3f} eV")
    
    # Bohr radii
    for n in range(1, 4):
        r_n = n**2 * BOHR_RADIUS
        print(f"n={n}: r={r_n*1e12:.1f} pm")

# Tunneling Probability
def tunneling_demo():
    print("\n=== Quantum Tunneling ===")
    
    # Rectangular barrier
    E = 1.0 * ELECTRON_VOLT  # Particle energy
    V0 = 2.0 * ELECTRON_VOLT  # Barrier height
    a = 1e-9  # Barrier width (1 nm)
    
    # Transmission coefficient
    kappa = np.sqrt(2 * ELECTRON_MASS * (V0 - E)) / REDUCED_PLANCK
    T = 1 / (1 + (V0**2 * np.sinh(kappa * a)**2) / (4 * E * (V0 - E)))
    
    print(f"Particle energy: {E/ELECTRON_VOLT:.1f} eV")
    print(f"Barrier height: {V0/ELECTRON_VOLT:.1f} eV")
    print(f"Barrier width: {a*1e9:.1f} nm")
    print(f"Transmission probability: {T:.2e}")
    print(f"Tunneling probability: {T*100:.4f}%")

# de Broglie Wavelength
def de_broglie_demo():
    print("\n=== de Broglie Wavelength ===")
    
    particles = [
        ("Electron (1 eV)", ELECTRON_MASS, 1.0 * ELECTRON_VOLT),
        ("Proton (1 MeV)", PROTON_MASS, 1e6 * ELECTRON_VOLT),
        ("Tennis ball", 0.06, 0.5 * 0.06 * 30**2)  # 60g at 30 m/s
    ]
    
    for name, mass, KE in particles:
        # Non-relativistic momentum
        p = np.sqrt(2 * mass * KE)
        lambda_db = PLANCK_CONSTANT / p
        
        if lambda_db > 1e-12:
            print(f"{name}: λ = {lambda_db*1e12:.2f} pm")
        elif lambda_db > 1e-15:
            print(f"{name}: λ = {lambda_db*1e15:.2f} fm")
        else:
            print(f"{name}: λ = {lambda_db:.2e} m")

# Wave Function Visualization
def plot_wave_functions():
    psi_data, L = particle_in_box_demo()
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    
    # Plot wave functions
    for n, x, psi in psi_data:
        ax1.plot(x*1e9, psi*1e-4.5, label=f'n={n}')
    
    ax1.set_xlabel('Position (nm)')
    ax1.set_ylabel('ψ(x) (nm⁻¹/²)')
    ax1.set_title('Particle in Box Wave Functions')
    ax1.legend()
    ax1.grid(True)
    
    # Plot probability densities
    for n, x, psi in psi_data:
        ax2.plot(x*1e9, (psi**2)*1e-9, label=f'n={n}')
    
    ax2.set_xlabel('Position (nm)')
    ax2.set_ylabel('|ψ(x)|² (nm⁻¹)')
    ax2.set_title('Probability Densities')
    ax2.legend()
    ax2.grid(True)
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    print("=== Quantum Physics Examples ===")
    
    particle_in_box_demo()
    harmonic_oscillator_demo()
    hydrogen_atom_demo()
    tunneling_demo()
    de_broglie_demo()
    
    # Uncomment to show plots
    # plot_wave_functions()


import numpy as np
import matplotlib.pyplot as plt
from ..constants import *

# Ideal Gas Law Demonstrations
def ideal_gas_demo():
    print("=== Ideal Gas Law Examples ===")
    
    # Standard conditions
    n = 1.0  # moles
    T1 = STANDARD_TEMPERATURE  # K
    P1 = STANDARD_PRESSURE     # Pa
    
    # Volume at STP
    V1 = n * GAS_CONSTANT * T1 / P1
    
    print(f"At STP (T={T1:.1f} K, P={P1/1000:.1f} kPa):")
    print(f"Volume of 1 mole: {V1*1000:.1f} L")
    
    # Temperature change at constant pressure
    T2 = 373.15  # Boiling point of water
    V2 = V1 * T2 / T1
    
    print(f"\nAt T={T2:.1f} K (constant P):")
    print(f"New volume: {V2*1000:.1f} L")
    print(f"Volume ratio: {V2/V1:.3f}")
    
    # Pressure change at constant temperature
    V3 = V1 / 2  # Half volume
    P3 = P1 * V1 / V3
    
    print(f"\nAt half volume (constant T):")
    print(f"New pressure: {P3/1000:.1f} kPa")
    print(f"Pressure ratio: {P3/P1:.1f}")

# Carnot Engine Efficiency
def carnot_engine_demo():
    print("\n=== Carnot Heat Engine ===")
    
    T_hot = 600   # K (hot reservoir)
    T_cold = 300  # K (cold reservoir)
    Q_hot = 1000  # J (heat input)
    
    # Carnot efficiency
    eta_carnot = 1 - T_cold / T_hot
    W_output = eta_carnot * Q_hot
    Q_cold = Q_hot - W_output
    
    print(f"Hot reservoir: {T_hot} K")
    print(f"Cold reservoir: {T_cold} K")
    print(f"Heat input: {Q_hot} J")
    print(f"Carnot efficiency: {eta_carnot:.3f} ({eta_carnot*100:.1f}%)")
    print(f"Work output: {W_output:.1f} J")
    print(f"Heat rejected: {Q_cold:.1f} J")
    
    # Coefficient of performance for refrigerator
    COP_ref = T_cold / (T_hot - T_cold)
    print(f"COP (refrigerator): {COP_ref:.2f}")

# Maxwell-Boltzmann Distribution
def maxwell_boltzmann_demo():
    print("\n=== Maxwell-Boltzmann Distribution ===")
    
    T = ROOM_TEMPERATURE  # K
    m = 4.0 * ATOMIC_MASS_UNIT  # Helium atom mass
    
    # Most probable speed
    v_mp = np.sqrt(2 * BOLTZMANN_CONSTANT * T / m)
    
    # Average speed
    v_avg = np.sqrt(8 * BOLTZMANN_CONSTANT * T / (PI * m))
    
    # RMS speed
    v_rms = np.sqrt(3 * BOLTZMANN_CONSTANT * T / m)
    
    print(f"Temperature: {T:.1f} K")
    print(f"Gas: Helium (m = {m/ATOMIC_MASS_UNIT:.1f} u)")
    print(f"Most probable speed: {v_mp:.0f} m/s")
    print(f"Average speed: {v_avg:.0f} m/s")
    print(f"RMS speed: {v_rms:.0f} m/s")
    
    # Speed distribution
    v = np.linspace(0, 3000, 1000)
    f_v = 4 * PI * (m / (2 * PI * BOLTZMANN_CONSTANT * T))**(3/2) * v**2 * np.exp(-m * v**2 / (2 * BOLTZMANN_CONSTANT * T))
    
    return v, f_v, v_mp, v_avg, v_rms

# Heat Capacity and Energy
def heat_capacity_demo():
    print("\n=== Heat Capacity ===")
    
    # Monatomic ideal gas (Ar)
    print("Monatomic gas (Argon):")
    Cv_mono = 1.5 * GAS_CONSTANT
    Cp_mono = 2.5 * GAS_CONSTANT
    gamma_mono = Cp_mono / Cv_mono
    
    print(f"Cv = {Cv_mono:.2f} J/(mol·K)")
    print(f"Cp = {Cp_mono:.2f} J/(mol·K)")
    print(f"γ = {gamma_mono:.3f}")
    
    # Diatomic ideal gas (N2)
    print("\nDiatomic gas (Nitrogen):")
    Cv_di = 2.5 * GAS_CONSTANT
    Cp_di = 3.5 * GAS_CONSTANT
    gamma_di = Cp_di / Cv_di
    
    print(f"Cv = {Cv_di:.2f} J/(mol·K)")
    print(f"Cp = {Cp_di:.2f} J/(mol·K)")
    print(f"γ = {gamma_di:.3f}")

# Entropy Calculations
def entropy_demo():
    print("\n=== Entropy Examples ===")
    
    # Entropy of mixing
    n1, n2 = 1.0, 1.0  # moles of each gas
    n_total = n1 + n2
    x1, x2 = n1/n_total, n2/n_total  # mole fractions
    
    delta_S_mix = -GAS_CONSTANT * (n1 * np.log(x1) + n2 * np.log(x2))
    
    print(f"Mixing {n1:.1f} mol + {n2:.1f} mol ideal gases:")
    print(f"Entropy of mixing: {delta_S_mix:.2f} J/K")
    
    # Temperature-dependent entropy change
    T1, T2 = 300, 400  # K
    n = 1.0  # mol
    Cp = 2.5 * GAS_CONSTANT  # monatomic gas
    
    delta_S_temp = n * Cp * np.log(T2 / T1)
    
    print(f"\nHeating {n:.1f} mol from {T1} to {T2} K:")
    print(f"Entropy change: {delta_S_temp:.2f} J/K")

# Blackbody Radiation
def blackbody_demo():
    print("\n=== Blackbody Radiation ===")
    
    T_sun = SOLAR_SURFACE_TEMPERATURE  # K
    T_room = ROOM_TEMPERATURE          # K
    
    # Stefan-Boltzmann law
    j_sun = STEFAN_BOLTZMANN_CONSTANT * T_sun**4
    j_room = STEFAN_BOLTZMANN_CONSTANT * T_room**4
    
    print(f"Sun surface ({T_sun} K): {j_sun:.2e} W/m²")
    print(f"Room temp ({T_room} K): {j_room:.1f} W/m²")
    
    # Wien's displacement law
    lambda_max_sun = WIEN_DISPLACEMENT_CONSTANT / T_sun
    lambda_max_room = WIEN_DISPLACEMENT_CONSTANT / T_room
    
    print(f"Peak wavelength (Sun): {lambda_max_sun*1e9:.0f} nm")
    print(f"Peak wavelength (room): {lambda_max_room*1e6:.1f} μm")

# Phase Transition
def phase_transition_demo():
    print("\n=== Phase Transitions ===")
    
    # Water phase transition
    T_melt = STANDARD_TEMPERATURE  # K
    T_boil = 373.15  # K
    
    # Latent heats (approximate)
    L_fusion = 334e3    # J/kg
    L_vaporization = 2.26e6  # J/kg
    
    m = 1.0  # kg of water
    
    print(f"Melting 1 kg ice at {T_melt:.1f} K:")
    Q_melt = m * L_fusion
    print(f"Energy required: {Q_melt/1000:.0f} kJ")
    
    print(f"\nVaporizing 1 kg water at {T_boil:.1f} K:")
    Q_vap = m * L_vaporization
    print(f"Energy required: {Q_vap/1000:.0f} kJ")
    
    # Clausius-Clapeyron equation (approximate)
    R_specific = GAS_CONSTANT / (18e-3)  # J/(kg·K) for water
    dP_dT = L_vaporization / (T_boil * R_specific)
    print(f"dP/dT at boiling: {dP_dT/1000:.1f} kPa/K")

def plot_distributions():
    v, f_v, v_mp, v_avg, v_rms = maxwell_boltzmann_demo()
    
    plt.figure(figsize=(10, 6))
    plt.plot(v, f_v*1e-3, 'b-', linewidth=2)
    plt.axvline(v_mp, color='r', linestyle='--', label=f'v_mp = {v_mp:.0f} m/s')
    plt.axvline(v_avg, color='g', linestyle='--', label=f'v_avg = {v_avg:.0f} m/s')
    plt.axvline(v_rms, color='orange', linestyle='--', label=f'v_rms = {v_rms:.0f} m/s')
    
    plt.xlabel('Speed (m/s)')
    plt.ylabel('f(v) × 10³ (s/m)')
    plt.title('Maxwell-Boltzmann Distribution (He at 298 K)')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.show()

if __name__ == "__main__":
    print("=== Thermodynamics Examples ===")
    
    ideal_gas_demo()
    carnot_engine_demo()
    maxwell_boltzmann_demo()
    heat_capacity_demo()
    entropy_demo()
    blackbody_demo()
    phase_transition_demo()
    
    # Uncomment to show plots
    # plot_distributions()


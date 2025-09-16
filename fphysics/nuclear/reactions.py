import numpy as np
import matplotlib.pyplot as plt
from typing import Union, List, Tuple, Dict
from ..constants import *
import math


def nuclear_reaction(projectile_mass: float, target_mass: float, product1_mass: float, 
                    product2_mass: float) -> float:
    Q = (projectile_mass + target_mass) - (product1_mass + product2_mass)
    return Q * ATOMIC_MASS_UNIT_MEV


def reaction_q_value(initial_masses: List[float], final_masses: List[float]) -> float:
    initial_mass = sum(initial_masses)
    final_mass = sum(final_masses)
    mass_defect = initial_mass - final_mass
    return mass_defect * ATOMIC_MASS_UNIT_MEV


def threshold_energy(projectile_mass: float, target_mass: float, Q_value: float) -> float:
    if Q_value >= 0:
        return 0.0
    
    total_mass = projectile_mass + target_mass
    threshold = -Q_value * (total_mass + projectile_mass) / (2 * target_mass)
    return threshold


def center_of_mass_energy(E_lab: float, m_projectile: float, m_target: float) -> float:
    E_cm = math.sqrt(2 * m_target * E_lab + (m_projectile + m_target)**2)
    return E_cm - (m_projectile + m_target)


def lab_to_cm_angle(theta_lab: float, m_projectile: float, m_target: float, 
                   m_product: float, E_lab: float) -> float:
    gamma = math.sqrt(E_lab / (m_projectile * SPEED_OF_LIGHT**2))
    beta = math.sqrt(1 - 1/gamma**2)
    
    cos_theta_cm = (math.cos(theta_lab) - beta) / (1 - beta * math.cos(theta_lab))
    return math.acos(cos_theta_cm)


def cross_section(reaction_rate: float, beam_intensity: float, target_density: float, 
                 target_thickness: float) -> float:
    return reaction_rate / (beam_intensity * target_density * target_thickness)


def rutherford_cross_section(Z1: int, Z2: int, energy: float, angle: float) -> float:
    k = COULOMB_CONSTANT * Z1 * Z2 * ELEMENTARY_CHARGE**2
    factor = (k / (4 * energy))**2
    sin4_half_theta = (math.sin(angle/2))**4
    return factor / sin4_half_theta


def compound_nucleus_cross_section(energy: float, resonance_energy: float, 
                                  total_width: float, partial_width: float) -> float:
    denominator = (energy - resonance_energy)**2 + (total_width/2)**2
    return (math.pi * (REDUCED_PLANCK * SPEED_OF_LIGHT)**2 / (2 * energy)) * \
           (partial_width**2 / denominator)


def fission_cross_section(energy: float, fissile_nucleus: str = 'U-235') -> float:
    if fissile_nucleus == 'U-235':
        if energy < 1.0:
            return 580 * BARN_TO_SQUARE_METER * math.sqrt(0.025 / energy)
        else:
            return 1.2 * BARN_TO_SQUARE_METER
    elif fissile_nucleus == 'Pu-239':
        if energy < 1.0:
            return 750 * BARN_TO_SQUARE_METER * math.sqrt(0.025 / energy)
        else:
            return 1.8 * BARN_TO_SQUARE_METER
    else:
        raise ValueError(f"Fission cross-section data not available for {fissile_nucleus}")


def neutron_absorption_cross_section(element: str, energy: float) -> float:
    thermal_cross_sections = {
        'H': 0.33, 'B': 767, 'C': 0.0035, 'N': 1.9, 'O': 0.00019,
        'Al': 0.231, 'Fe': 2.56, 'Cd': 2520, 'Gd': 49000, 'U': 7.57
    }
    
    if element in thermal_cross_sections:
        sigma_thermal = thermal_cross_sections[element] * BARN_TO_SQUARE_METER
        return sigma_thermal * math.sqrt(0.025 / energy)
    else:
        raise ValueError(f"Cross-section data not available for {element}")


def reaction_rate(cross_section: float, flux: float, number_density: float) -> float:
    return cross_section * flux * number_density


def maxwell_boltzmann_average(cross_section_func, temperature: float, 
                             energy_range: Tuple[float, float] = (0.001, 10.0)) -> float:
    kT = BOLTZMANN_CONSTANT * temperature / ELECTRON_VOLT
    
    def integrand(E):
        return cross_section_func(E) * E * np.exp(-E / kT)
    
    energies = np.linspace(energy_range[0], energy_range[1], 1000)
    values = [integrand(E) for E in energies]
    
    numerator = np.trapz(values, energies)
    denominator = kT**2
    
    return numerator / denominator


def coulomb_barrier(Z1: int, Z2: int, R: float) -> float:
    return COULOMB_CONSTANT * Z1 * Z2 * ELEMENTARY_CHARGE**2 / (4 * math.pi * VACUUM_PERMITTIVITY * R)


def gamow_factor(Z1: int, Z2: int, energy: float) -> float:
    eta = Z1 * Z2 * FINE_STRUCTURE_CONSTANT * math.sqrt(ATOMIC_MASS_UNIT * SPEED_OF_LIGHT**2 / (2 * energy))
    return 2 * math.pi * eta


def fusion_cross_section(Z1: int, Z2: int, energy: float, S_factor: float = 1.0) -> float:
    gamow = gamow_factor(Z1, Z2, energy)
    return (S_factor / energy) * np.exp(-gamow)


def resonance_integral(cross_section_func, energy_range: Tuple[float, float]) -> float:
    energies = np.logspace(np.log10(energy_range[0]), np.log10(energy_range[1]), 1000)
    values = [cross_section_func(E) / E for E in energies]
    return np.trapz(values, energies)


def doppler_broadening(energy: float, temperature: float, mass: float) -> float:
    thermal_velocity = math.sqrt(2 * BOLTZMANN_CONSTANT * temperature / mass)
    return 2 * energy * thermal_velocity / SPEED_OF_LIGHT


def plot_cross_section(energy_range: Tuple[float, float], cross_section_func, 
                      title: str = "Nuclear Cross-Section", log_scale: bool = True):
    energies = np.logspace(np.log10(energy_range[0]), np.log10(energy_range[1]), 1000)
    cross_sections = [cross_section_func(E) for E in energies]
    
    plt.figure(figsize=(10, 6))
    if log_scale:
        plt.loglog(energies, cross_sections, 'b-', linewidth=2)
    else:
        plt.plot(energies, cross_sections, 'b-', linewidth=2)
    
    plt.xlabel('Energy (eV)')
    plt.ylabel('Cross-Section (m²)')
    plt.title(title)
    plt.grid(True, alpha=0.3)
    plt.show()


def two_body_kinematics(m1: float, m2: float, m3: float, m4: float, 
                       E1: float, theta3: float) -> Tuple[float, float, float]:
    Q = nuclear_reaction(m1, m2, m3, m4)
    
    p1 = math.sqrt(2 * m1 * E1)
    
    A = m3 + m4 - (p1**2 * math.cos(theta3)**2) / (2 * m4)
    B = -2 * E1 - Q
    C = E1**2 + 2 * m2 * E1 + Q * (Q + 2 * m2)
    
    discriminant = B**2 - 4 * A * C
    if discriminant < 0:
        raise ValueError("Kinematically forbidden reaction")
    
    E3 = (-B + math.sqrt(discriminant)) / (2 * A)
    
    p3 = math.sqrt(2 * m3 * E3)
    p4_x = p1 - p3 * math.cos(theta3)
    p4_y = -p3 * math.sin(theta3)
    p4 = math.sqrt(p4_x**2 + p4_y**2)
    
    E4 = p4**2 / (2 * m4)
    theta4 = math.atan2(p4_y, p4_x)
    
    return E3, E4, theta4


REACTION_DATA = {
    'D(d,n)He3': {'Q': 3.27, 'threshold': 0.0},
    'D(d,p)T': {'Q': 4.03, 'threshold': 0.0},
    'T(d,n)He4': {'Q': 17.59, 'threshold': 0.0},
    'He3(d,p)He4': {'Q': 18.35, 'threshold': 0.0},
    'Li6(n,t)He4': {'Q': 4.78, 'threshold': 0.0},
    'B10(n,a)Li7': {'Q': 2.79, 'threshold': 0.0},
    'C12(p,g)N13': {'Q': 1.94, 'threshold': 0.0},
    'N14(p,a)C11': {'Q': -2.92, 'threshold': 5.5},
    'O16(p,a)N13': {'Q': -1.19, 'threshold': 2.4}
}


def get_reaction_data(reaction: str) -> Dict:
    if reaction in REACTION_DATA:
        return REACTION_DATA[reaction].copy()
    else:
        available = ', '.join(REACTION_DATA.keys())
        raise ValueError(f"Reaction {reaction} not found. Available: {available}")


def neutron_flux_spectrum(energy: float, flux_type: str = 'thermal') -> float:
    if flux_type == 'thermal':
        kT = 0.025
        return (2 / math.sqrt(math.pi)) * math.sqrt(energy / kT**3) * np.exp(-energy / kT)
    elif flux_type == 'fast':
        return 0.484 * math.sinh(math.sqrt(2 * energy)) * np.exp(-energy)
    elif flux_type == 'epithermal':
        return 1.0 / energy
    else:
        raise ValueError(f"Unknown flux type: {flux_type}")


def activation_rate(cross_section: float, flux: float, decay_constant: float, 
                   irradiation_time: float) -> float:
    production_rate = cross_section * flux
    return production_rate * (1 - np.exp(-decay_constant * irradiation_time)) / decay_constant

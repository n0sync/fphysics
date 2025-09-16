import numpy as np
import matplotlib.pyplot as plt
from typing import Union, List, Tuple, Dict
from ..constants import *
import math


def fission_energy(fissile_mass: float, fragment1_mass: float, fragment2_mass: float, 
                  neutron_count: int = 2) -> float:
    neutron_mass_total = neutron_count * NEUTRON_MASS_MEV / ATOMIC_MASS_UNIT_MEV
    mass_defect = fissile_mass - (fragment1_mass + fragment2_mass + neutron_mass_total)
    return mass_defect * ATOMIC_MASS_UNIT_MEV


def fusion_energy(reactant1_mass: float, reactant2_mass: float, 
                 product1_mass: float, product2_mass: float = 0) -> float:
    initial_mass = reactant1_mass + reactant2_mass
    final_mass = product1_mass + product2_mass
    mass_defect = initial_mass - final_mass
    return mass_defect * ATOMIC_MASS_UNIT_MEV


def critical_mass(density: float, fissile_isotope: str = 'U-235') -> float:
    if fissile_isotope == 'U-235':
        D = 1.4
        k_inf = 1.65
        B_c_squared = (k_inf - 1) / (D**2)
        R_c = math.pi / math.sqrt(B_c_squared)
        volume = (4/3) * math.pi * (R_c * 1e-2)**3
        return density * volume
    elif fissile_isotope == 'Pu-239':
        D = 1.2
        k_inf = 2.1
        B_c_squared = (k_inf - 1) / (D**2)
        R_c = math.pi / math.sqrt(B_c_squared)
        volume = (4/3) * math.pi * (R_c * 1e-2)**3
        return density * volume
    else:
        raise ValueError(f"Critical mass data not available for {fissile_isotope}")


def multiplication_factor(k_eff: float, generation_time: float, delayed_neutron_fraction: float) -> float:
    reactivity = (k_eff - 1) / k_eff
    if k_eff > 1:
        return math.exp(reactivity / (generation_time * delayed_neutron_fraction))
    else:
        return k_eff


def chain_reaction_rate(initial_neutrons: int, k_eff: float, generations: int) -> int:
    return int(initial_neutrons * k_eff**generations)


def reactor_period(reactivity: float, delayed_neutron_fraction: float = 0.0065, 
                  generation_time: float = 1e-5) -> float:
    if reactivity > delayed_neutron_fraction:
        return generation_time / (reactivity - delayed_neutron_fraction)
    else:
        return generation_time / reactivity


def four_factor_formula(eta: float, f: float, p: float, epsilon: float) -> float:
    return eta * f * p * epsilon


def thermal_utilization(absorption_fuel: float, absorption_total: float) -> float:
    return absorption_fuel / absorption_total


def resonance_escape_probability(absorption_resonance: float, scattering_total: float) -> float:
    return math.exp(-absorption_resonance / scattering_total)


def fast_fission_factor(fast_fissions: float, thermal_fissions: float) -> float:
    return 1 + fast_fissions / thermal_fissions


def reproduction_factor(neutrons_produced: float, neutrons_absorbed: float) -> float:
    return neutrons_produced / neutrons_absorbed


def lawson_criterion(density: float, temperature: float, confinement_time: float, 
                    reaction: str = 'DT') -> bool:
    if reaction == 'DT':
        criterion_value = 3e21
        nT_tau = density * temperature * confinement_time
        return nT_tau > criterion_value
    elif reaction == 'DD':
        criterion_value = 1e22
        nT_tau = density * temperature * confinement_time
        return nT_tau > criterion_value
    else:
        raise ValueError(f"Lawson criterion not defined for reaction: {reaction}")


def fusion_cross_section_dt(energy: float) -> float:
    if energy < 1:
        return 0
    
    sigma_max = 5.0 * BARN_TO_SQUARE_METER
    E_peak = 65
    
    if energy < E_peak:
        return sigma_max * (energy / E_peak) * math.exp(-43.2 / math.sqrt(energy))
    else:
        return sigma_max * (E_peak / energy)


def fusion_cross_section_dd(energy: float) -> float:
    if energy < 1:
        return 0
    
    return 0.1 * BARN_TO_SQUARE_METER * math.exp(-44.4 / math.sqrt(energy))


def fusion_reaction_rate(density1: float, density2: float, temperature: float, 
                        reaction: str = 'DT') -> float:
    kT = BOLTZMANN_CONSTANT * temperature
    
    if reaction == 'DT':
        if temperature < 1e7:
            sigma_v = 0
        else:
            T_keV = kT / ELECTRON_VOLT / 1000
            sigma_v = 1.1e-24 * T_keV**2 / (1 + 5.1e-4 * T_keV + 2.1e-7 * T_keV**2)
        
        return density1 * density2 * sigma_v
    else:
        raise ValueError(f"Reaction rate not implemented for: {reaction}")


def ignition_temperature(reaction: str = 'DT') -> float:
    if reaction == 'DT':
        return 4.4e7
    elif reaction == 'DD':
        return 2.3e8
    elif reaction == 'DHe3':
        return 5.8e8
    else:
        raise ValueError(f"Ignition temperature not defined for: {reaction}")


def magnetic_confinement_time(plasma_radius: float, magnetic_field: float, 
                             temperature: float) -> float:
    diffusion_coeff = BOLTZMANN_CONSTANT * temperature / (16 * ELEMENTARY_CHARGE * magnetic_field)
    return plasma_radius**2 / diffusion_coeff


def inertial_confinement_time(pellet_radius: float, ion_temperature: float) -> float:
    sound_speed = math.sqrt(BOLTZMANN_CONSTANT * ion_temperature / PROTON_MASS)
    return pellet_radius / sound_speed


def fission_fragment_energy(A_fragment: int, Z_fragment: int) -> float:
    A_fissile = 235
    Z_fissile = 92
    
    r0 = NUCLEAR_RADIUS_CONSTANT * 1e-15
    R_contact = r0 * (A_fragment**(1/3) + (A_fissile - A_fragment)**(1/3))
    
    E_coulomb = COULOMB_CONSTANT * Z_fragment * (Z_fissile - Z_fragment) * ELEMENTARY_CHARGE**2 / R_contact
    
    mass_ratio = (A_fissile - A_fragment) / A_fragment
    fragment_fraction = mass_ratio / (1 + mass_ratio)
    
    return E_coulomb * fragment_fraction / ELECTRON_VOLT / 1e6


def delayed_neutron_parameters() -> Dict:
    return {
        'groups': 6,
        'fractions': [0.000247, 0.0013845, 0.001222, 0.0026455, 0.0008320, 0.000169],
        'decay_constants': [0.0124, 0.0305, 0.111, 0.301, 1.14, 3.01],
        'total_fraction': 0.0065
    }


def prompt_neutron_lifetime(moderator: str = 'water') -> float:
    lifetimes = {
        'water': 2e-5,
        'graphite': 1e-3,
        'heavy_water': 1e-4,
        'fast': 1e-7
    }
    
    if moderator in lifetimes:
        return lifetimes[moderator]
    else:
        raise ValueError(f"Neutron lifetime not available for: {moderator}")


def conversion_ratio(fertile_absorptions: float, fissile_absorptions: float) -> float:
    return fertile_absorptions / fissile_absorptions


def breeding_ratio(fissile_produced: float, fissile_consumed: float) -> float:
    return fissile_produced / fissile_consumed


def power_density(fission_rate: float, energy_per_fission: float = 200e6) -> float:
    power_per_unit_volume = fission_rate * energy_per_fission * ELECTRON_VOLT
    return power_per_unit_volume


def burnup_calculation(initial_fuel: float, final_fuel: float, energy_released: float) -> float:
    fuel_consumed = initial_fuel - final_fuel
    burnup = energy_released / fuel_consumed / (24 * 3600 * 1e6)
    return burnup


def xenon_poisoning(flux: float, sigma_a_xe135: float = 2.65e6 * BARN_TO_SQUARE_METER) -> float:
    yield_xe135 = 0.063
    yield_i135 = 0.061
    lambda_i135 = 2.92e-5
    lambda_xe135 = 2.09e-5
    
    sigma_f = 580 * BARN_TO_SQUARE_METER
    
    production_rate = flux * sigma_f * (yield_xe135 + yield_i135)
    removal_rate = lambda_xe135 + flux * sigma_a_xe135
    
    xe135_concentration = production_rate / removal_rate
    return flux * sigma_a_xe135 * xe135_concentration


def plot_fission_cross_section(energy_range: Tuple[float, float] = (0.01, 10)):
    energies = np.logspace(np.log10(energy_range[0]), np.log10(energy_range[1]), 1000)
    
    sigma_u235 = []
    for E in energies:
        if E < 1:
            sigma = 580 * BARN_TO_SQUARE_METER * math.sqrt(0.025 / E)
        else:
            sigma = 1.2 * BARN_TO_SQUARE_METER
        sigma_u235.append(sigma / BARN_TO_SQUARE_METER)
    
    plt.figure(figsize=(10, 6))
    plt.loglog(energies, sigma_u235, 'b-', linewidth=2, label='U-235')
    plt.xlabel('Neutron Energy (eV)')
    plt.ylabel('Fission Cross-Section (barns)')
    plt.title('Nuclear Fission Cross-Section')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.show()


def plot_fusion_cross_section(energy_range: Tuple[float, float] = (1, 1000)):
    energies = np.linspace(energy_range[0], energy_range[1], 1000)
    
    dt_cross_sections = [fusion_cross_section_dt(E) / BARN_TO_SQUARE_METER for E in energies]
    dd_cross_sections = [fusion_cross_section_dd(E) / BARN_TO_SQUARE_METER for E in energies]
    
    plt.figure(figsize=(10, 6))
    plt.semilogy(energies, dt_cross_sections, 'r-', linewidth=2, label='D-T')
    plt.semilogy(energies, dd_cross_sections, 'b-', linewidth=2, label='D-D')
    plt.xlabel('Center-of-Mass Energy (keV)')
    plt.ylabel('Cross-Section (barns)')
    plt.title('Nuclear Fusion Cross-Sections')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.show()


FISSION_DATA = {
    'U-235': {
        'thermal_fission_cs': 580,
        'fast_fission_cs': 1.2,
        'nu': 2.4,
        'energy_per_fission': 200
    },
    'U-238': {
        'thermal_fission_cs': 0,
        'fast_fission_cs': 0.3,
        'nu': 2.4,
        'energy_per_fission': 200
    },
    'Pu-239': {
        'thermal_fission_cs': 750,
        'fast_fission_cs': 1.8,
        'nu': 2.9,
        'energy_per_fission': 210
    }
}


FUSION_DATA = {
    'D-T': {
        'Q_value': 17.6,
        'products': ['He-4', 'n'],
        'ignition_T': 4.4e7
    },
    'D-D': {
        'Q_value': 3.27,
        'products': ['He-3', 'n'],
        'ignition_T': 2.3e8
    },
    'D-He3': {
        'Q_value': 18.35,
        'products': ['He-4', 'p'],
        'ignition_T': 5.8e8
    }
}

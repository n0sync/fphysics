import numpy as np
import matplotlib.pyplot as plt
from typing import Union, List, Tuple, Dict
from ..constants import *
import math


def binding_energy(mass_number: int, atomic_mass: float) -> float:
    Z = atomic_number_from_mass(mass_number)
    mass_defect = Z * PROTON_MASS + (mass_number - Z) * NEUTRON_MASS - atomic_mass * ATOMIC_MASS_UNIT
    return mass_defect * SPEED_OF_LIGHT**2 / ELECTRON_VOLT / 1e6


def binding_energy_per_nucleon(mass_number: int, atomic_mass: float) -> float:
    BE = binding_energy(mass_number, atomic_mass)
    return BE / mass_number


def mass_defect(mass_number: int, atomic_mass: float) -> float:
    Z = atomic_number_from_mass(mass_number)
    theoretical_mass = Z * PROTON_MASS_MEV + (mass_number - Z) * NEUTRON_MASS_MEV
    actual_mass = atomic_mass * ATOMIC_MASS_UNIT_MEV
    return (theoretical_mass - actual_mass) / ATOMIC_MASS_UNIT_MEV


def atomic_number_from_mass(mass_number: int) -> int:
    if mass_number <= 20:
        return mass_number // 2
    elif mass_number <= 40:
        return int(mass_number / 2.1)
    elif mass_number <= 100:
        return int(mass_number / 2.2)
    else:
        return int(mass_number / 2.4)


def semi_empirical_mass_formula(A: int, Z: int) -> float:
    a_v = 15.75
    a_s = 17.8
    a_c = 0.711
    a_A = 23.7
    
    if Z % 2 == 0 and (A - Z) % 2 == 0:
        delta = 11.18 / math.sqrt(A)
    elif Z % 2 == 1 and (A - Z) % 2 == 1:
        delta = -11.18 / math.sqrt(A)
    else:
        delta = 0
    
    BE = (a_v * A - 
          a_s * A**(2/3) - 
          a_c * Z**2 / A**(1/3) - 
          a_A * (A - 2*Z)**2 / A + 
          delta)
    
    mass_energy = Z * PROTON_MASS_MEV + (A - Z) * NEUTRON_MASS_MEV - BE
    return mass_energy / ATOMIC_MASS_UNIT_MEV


def separation_energy(A: int, Z: int, particle: str = 'neutron') -> float:
    if particle == 'neutron':
        BE_initial = binding_energy_semf(A, Z)
        BE_final = binding_energy_semf(A-1, Z)
        return BE_initial - BE_final
    elif particle == 'proton':
        BE_initial = binding_energy_semf(A, Z)
        BE_final = binding_energy_semf(A-1, Z-1)
        return BE_initial - BE_final
    elif particle == 'alpha':
        BE_initial = binding_energy_semf(A, Z)
        BE_final = binding_energy_semf(A-4, Z-2)
        return BE_initial - BE_final - 28.3
    else:
        raise ValueError(f"Unknown particle type: {particle}")


def binding_energy_semf(A: int, Z: int) -> float:
    a_v = 15.75
    a_s = 17.8
    a_c = 0.711
    a_A = 23.7
    
    if Z % 2 == 0 and (A - Z) % 2 == 0:
        delta = 11.18 / math.sqrt(A)
    elif Z % 2 == 1 and (A - Z) % 2 == 1:
        delta = -11.18 / math.sqrt(A)
    else:
        delta = 0
    
    return (a_v * A - 
            a_s * A**(2/3) - 
            a_c * Z**2 / A**(1/3) - 
            a_A * (A - 2*Z)**2 / A + 
            delta)


def q_value_alpha_decay(A_parent: int, Z_parent: int) -> float:
    M_parent = semi_empirical_mass_formula(A_parent, Z_parent)
    M_daughter = semi_empirical_mass_formula(A_parent - 4, Z_parent - 2)
    M_alpha = 4.002603
    
    return (M_parent - M_daughter - M_alpha) * ATOMIC_MASS_UNIT_MEV


def q_value_beta_decay(A: int, Z: int, decay_type: str = 'beta-') -> float:
    if decay_type == 'beta-':
        M_parent = semi_empirical_mass_formula(A, Z)
        M_daughter = semi_empirical_mass_formula(A, Z + 1)
        return (M_parent - M_daughter) * ATOMIC_MASS_UNIT_MEV
    elif decay_type == 'beta+':
        M_parent = semi_empirical_mass_formula(A, Z)
        M_daughter = semi_empirical_mass_formula(A, Z - 1)
        return (M_parent - M_daughter - 2 * ELECTRON_MASS_MEV) * ATOMIC_MASS_UNIT_MEV
    else:
        raise ValueError(f"Unknown decay type: {decay_type}")


def magic_numbers() -> List[int]:
    return [2, 8, 20, 28, 50, 82, 126]


def is_magic_nucleus(A: int, Z: int) -> bool:
    N = A - Z
    magic = magic_numbers()
    return Z in magic or N in magic


def nuclear_radius(A: int) -> float:
    r0 = NUCLEAR_RADIUS_CONSTANT
    return r0 * A**(1/3)


def nuclear_density() -> float:
    r0 = NUCLEAR_RADIUS_CONSTANT * 1e-15
    volume_per_nucleon = (4/3) * math.pi * r0**3
    return ATOMIC_MASS_UNIT / volume_per_nucleon


def liquid_drop_energy(A: int, Z: int) -> float:
    return -binding_energy_semf(A, Z) + Z * PROTON_MASS_MEV + (A - Z) * NEUTRON_MASS_MEV


def coulomb_energy(A: int, Z: int) -> float:
    R = nuclear_radius(A) * 1e-15
    return (3/5) * COULOMB_CONSTANT * Z**2 * ELEMENTARY_CHARGE**2 / R / ELECTRON_VOLT / 1e6


def surface_energy(A: int) -> float:
    a_s = 17.8
    return a_s * A**(2/3)


def asymmetry_energy(A: int, Z: int) -> float:
    a_A = 23.7
    return a_A * (A - 2*Z)**2 / A


def pairing_energy(A: int, Z: int) -> float:
    N = A - Z
    if Z % 2 == 0 and N % 2 == 0:
        return 11.18 / math.sqrt(A)
    elif Z % 2 == 1 and N % 2 == 1:
        return -11.18 / math.sqrt(A)
    else:
        return 0


def valley_of_stability(A_range: Tuple[int, int]) -> List[int]:
    stable_Z = []
    for A in range(A_range[0], A_range[1] + 1):
        min_mass = float('inf')
        best_Z = 1
        
        for Z in range(1, A):
            mass = semi_empirical_mass_formula(A, Z)
            if mass < min_mass:
                min_mass = mass
                best_Z = Z
        
        stable_Z.append(best_Z)
    
    return stable_Z


def plot_binding_energy_curve(A_range: Tuple[int, int] = (1, 250)):
    A_values = range(A_range[0], A_range[1] + 1)
    BE_per_A = []
    
    for A in A_values:
        Z = atomic_number_from_mass(A)
        BE = binding_energy_semf(A, Z)
        BE_per_A.append(BE / A)
    
    plt.figure(figsize=(12, 8))
    plt.plot(A_values, BE_per_A, 'b-', linewidth=2)
    plt.xlabel('Mass Number (A)')
    plt.ylabel('Binding Energy per Nucleon (MeV)')
    plt.title('Nuclear Binding Energy Curve')
    plt.grid(True, alpha=0.3)
    
    important_nuclei = [(4, 'He-4'), (12, 'C-12'), (16, 'O-16'), (56, 'Fe-56'), (238, 'U-238')]
    for A, label in important_nuclei:
        if A_range[0] <= A <= A_range[1]:
            Z = atomic_number_from_mass(A)
            BE = binding_energy_semf(A, Z) / A
            plt.annotate(label, (A, BE), xytext=(A, BE + 0.5), 
                        arrowprops=dict(arrowstyle='->', color='red'))
    
    plt.show()


def mass_excess(A: int, Z: int) -> float:
    atomic_mass_u = semi_empirical_mass_formula(A, Z)
    return (atomic_mass_u - A) * ATOMIC_MASS_UNIT_MEV


def two_neutron_separation_energy(A: int, Z: int) -> float:
    BE_initial = binding_energy_semf(A, Z)
    BE_final = binding_energy_semf(A - 2, Z)
    return BE_initial - BE_final


def neutron_drip_line(Z: int) -> int:
    for A in range(Z, 300):
        S_n = separation_energy(A, Z, 'neutron')
        if S_n <= 0:
            return A - 1
    return 300


def proton_drip_line(Z: int) -> int:
    for A in range(Z, 300):
        S_p = separation_energy(A, Z, 'proton')
        if S_p <= 0:
            return A - 1
    return 300


NUCLEAR_DATA = {
    'H-1': {'A': 1, 'Z': 1, 'mass': 1.007825},
    'H-2': {'A': 2, 'Z': 1, 'mass': 2.014102},
    'H-3': {'A': 3, 'Z': 1, 'mass': 3.016049},
    'He-3': {'A': 3, 'Z': 2, 'mass': 3.016029},
    'He-4': {'A': 4, 'Z': 2, 'mass': 4.002603},
    'Li-6': {'A': 6, 'Z': 3, 'mass': 6.015122},
    'Li-7': {'A': 7, 'Z': 3, 'mass': 7.016004},
    'C-12': {'A': 12, 'Z': 6, 'mass': 12.000000},
    'N-14': {'A': 14, 'Z': 7, 'mass': 14.003074},
    'O-16': {'A': 16, 'Z': 8, 'mass': 15.994915},
    'Fe-56': {'A': 56, 'Z': 26, 'mass': 55.934942},
    'U-235': {'A': 235, 'Z': 92, 'mass': 235.043930},
    'U-238': {'A': 238, 'Z': 92, 'mass': 238.050788}
}


def get_nuclear_data(nucleus: str) -> Dict:
    if nucleus in NUCLEAR_DATA:
        return NUCLEAR_DATA[nucleus].copy()
    else:
        available = ', '.join(NUCLEAR_DATA.keys())
        raise ValueError(f"Nucleus {nucleus} not found. Available: {available}")

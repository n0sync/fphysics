"""
Radioactive Decay Module
Functions for radioactive decay calculations including decay constants, half-lives, activities, and decay chains.
"""

import numpy as np
import matplotlib.pyplot as plt
from typing import Union, List, Tuple, Dict
from ..constants import *
import math


def decay_constant(half_life: float) -> float:
    """Calculate the decay constant from half-life."""
    return math.log(2) / half_life


def half_life(decay_constant: float) -> float:
    """Calculate the half-life from decay constant."""
    return math.log(2) / decay_constant


def radioactive_decay(N0: float, decay_constant: float, time: Union[float, np.ndarray]) -> Union[float, np.ndarray]:
    """Calculate number of radioactive nuclei remaining after time t."""
    return N0 * np.exp(-decay_constant * time)


def activity(N0: float, decay_constant: float, time: Union[float, np.ndarray] = 0) -> Union[float, np.ndarray]:
    """Calculate the activity (decay rate) at time t."""
    N_t = radioactive_decay(N0, decay_constant, time)
    return decay_constant * N_t


def mean_lifetime(decay_constant: float) -> float:
    """Calculate the mean lifetime of a radioactive nucleus."""
    return 1.0 / decay_constant


def decay_chain(N0_list: List[float], decay_constants: List[float], time: Union[float, np.ndarray]) -> List[Union[float, np.ndarray]]:
    """Calculate radioactive decay chain (Bateman equations for simple chain A→B→C)."""
    if len(N0_list) != len(decay_constants):
        raise ValueError("Number of initial conditions must match number of decay constants")
    
    n_species = len(N0_list)
    results = []
    
    if n_species == 2:
        λ1, λ2 = decay_constants
        N0_A, N0_B = N0_list
        
        N_A = N0_A * np.exp(-λ1 * time)
        
        if abs(λ1 - λ2) > 1e-15:
            production_term = (λ1 * N0_A / (λ2 - λ1)) * (np.exp(-λ1 * time) - np.exp(-λ2 * time))
            decay_term = N0_B * np.exp(-λ2 * time)
            N_B = production_term + decay_term
        else:
            N_B = (N0_B + λ1 * N0_A * time) * np.exp(-λ1 * time)
        
        results = [N_A, N_B]
    else:
        results = []
        for i, (N0, λ) in enumerate(zip(N0_list, decay_constants)):
            if i == 0:
                N_i = N0 * np.exp(-λ * time)
            else:
                production_rate = decay_constants[i-1] * N0_list[i-1]
                if λ > 0:
                    production_contribution = (production_rate / λ) * (1 - np.exp(-λ * time))
                    initial_decay = N0 * np.exp(-λ * time)
                    N_i = production_contribution + initial_decay
                else:
                    N_i = N0
            results.append(N_i)
    
    return results


def specific_activity(mass_grams: float, atomic_mass: float, half_life: float) -> float:
    """Calculate the specific activity of a radioactive sample."""
    N_atoms_per_gram = AVOGADRO_NUMBER / atomic_mass
    N_total = N_atoms_per_gram * mass_grams
    λ = decay_constant(half_life)
    A_total = λ * N_total
    return A_total / mass_grams


def decay_energy(mass_parent: float, mass_daughter: float, mass_particle: float) -> float:
    """Calculate the Q-value (energy released) in a decay process."""
    mass_defect = mass_parent - (mass_daughter + mass_particle)
    return mass_defect * ATOMIC_MASS_UNIT_MEV


def plot_decay_curve(N0: float, decay_constant: float, max_time: float = None, num_points: int = 1000):
    """Plot the radioactive decay curve."""
    if max_time is None:
        max_time = 5 * half_life(decay_constant)
    
    time_array = np.linspace(0, max_time, num_points)
    N_array = radioactive_decay(N0, decay_constant, time_array)
    
    plt.figure(figsize=(10, 6))
    plt.plot(time_array, N_array, 'b-', linewidth=2, label='N(t)')
    plt.axhline(y=N0/2, color='r', linestyle='--', alpha=0.7, label='N₀/2')
    plt.axvline(x=half_life(decay_constant), color='r', linestyle='--', alpha=0.7, label='t₁/₂')
    
    plt.xlabel('Time (s)')
    plt.ylabel('Number of Nuclei')
    plt.title('Radioactive Decay Curve')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.show()


def effective_half_life(biological_half_life: float, physical_half_life: float) -> float:
    """Calculate effective half-life considering both biological and physical decay."""
    λ_bio = decay_constant(biological_half_life)
    λ_phys = decay_constant(physical_half_life)
    λ_eff = λ_bio + λ_phys
    return half_life(λ_eff)


ISOTOPE_DATA = {
    'C-14': {'half_life': 1.81e11, 'decay_type': 'beta-', 'atomic_mass': 14.003242},
    'U-238': {'half_life': 1.41e17, 'decay_type': 'alpha', 'atomic_mass': 238.050788},
    'U-235': {'half_life': 2.22e16, 'decay_type': 'alpha', 'atomic_mass': 235.043930},
    'Ra-226': {'half_life': 5.05e10, 'decay_type': 'alpha', 'atomic_mass': 226.025410},
    'Co-60': {'half_life': 1.67e8, 'decay_type': 'beta-', 'atomic_mass': 59.934072},
    'I-131': {'half_life': 6.95e5, 'decay_type': 'beta-', 'atomic_mass': 130.906127},
    'Tc-99m': {'half_life': 2.16e4, 'decay_type': 'gamma', 'atomic_mass': 98.906255},
    'Pu-239': {'half_life': 7.60e11, 'decay_type': 'alpha', 'atomic_mass': 239.052164},
    'Sr-90': {'half_life': 9.03e8, 'decay_type': 'beta-', 'atomic_mass': 89.907474},
    'Cs-137': {'half_life': 9.49e8, 'decay_type': 'beta-', 'atomic_mass': 136.907089}
}


def get_isotope_properties(isotope: str) -> Dict:
    """Get properties of common radioactive isotopes."""
    if isotope in ISOTOPE_DATA:
        return ISOTOPE_DATA[isotope].copy()
    else:
        available = ', '.join(ISOTOPE_DATA.keys())
        raise ValueError(f"Isotope {isotope} not found. Available: {available}")


def branching_ratio_decay(N0: float, decay_constants: List[float], branching_ratios: List[float], 
                         time: Union[float, np.ndarray]) -> Tuple[Union[float, np.ndarray], List[Union[float, np.ndarray]]]:
    """Calculate decay with branching ratios for multiple decay pathways."""
    if len(decay_constants) != len(branching_ratios):
        raise ValueError("Number of decay constants must match number of branching ratios")
    
    if abs(sum(branching_ratios) - 1.0) > 1e-10:
        raise ValueError("Branching ratios must sum to 1.0")
    
    λ_total = sum(λ * br for λ, br in zip(decay_constants, branching_ratios))
    N_parent = N0 * np.exp(-λ_total * time)
    N_decayed = N0 - N_parent
    
    daughters = [N_decayed * br for br in branching_ratios]
    
    return N_parent, daughters

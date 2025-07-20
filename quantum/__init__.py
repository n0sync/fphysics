"""Quantum Mechanics Module.

This module contains implementations of quantum mechanical concepts including:
- Wave functions and Schrödinger equation
- Quantum operators and observables
- Quantum harmonic oscillator
- Hydrogen atom solutions
- Quantum tunneling
- Spin and angular momentum
- Quantum statistics
- Perturbation theory
"""

from .wave_functions import *
from .operators import *
from .harmonic_oscillator import *
from .hydrogen_atom import *
from .tunneling import *
from .spin import *
from .statistics import *
from .perturbation import *

__all__ = [
    # Wave functions
    'schrodinger_time_dependent',
    'schrodinger_time_independent',
    'wave_function_normalization',
    'probability_density',
    'expectation_value',
    
    # Operators
    'momentum_operator',
    'kinetic_energy_operator',
    'hamiltonian_operator',
    'commutator',
    'uncertainty_principle',
    
    # Harmonic oscillator
    'harmonic_oscillator_energy',
    'harmonic_oscillator_wavefunction',
    'creation_operator',
    'annihilation_operator',
    
    # Hydrogen atom
    'hydrogen_energy_levels',
    'hydrogen_wavefunction',
    'radial_wavefunction',
    'spherical_harmonics',
    
    # Tunneling
    'tunnel_probability',
    'transmission_coefficient',
    'reflection_coefficient',
    
    # Spin
    'spin_matrices',
    'spin_eigenvalues',
    'spin_eigenvectors',
    
    # Statistics
    'fermi_dirac_distribution',
    'bose_einstein_distribution',
    'quantum_partition_function',
    
    # Perturbation theory
    'first_order_correction',
    'second_order_correction',
    'stark_effect',
    'zeeman_effect'
]

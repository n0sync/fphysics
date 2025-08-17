"""Electromagnetic Theory Module.

This module contains implementations of fundamental electromagnetic concepts including:
- Electrostatics (Coulomb's law, electric fields)
- Magnetostatics (magnetic fields & forces)
- Circuit analysis (DC/AC circuits)
- Electromagnetic waves
- Maxwell's equations
- Optics (geometric & wave optics)
"""

from .electrostatics import *
from .magnetostatics import *
from .circuits import *
from .waves import *
from .maxwell import *
from .optics import *

__all__ = [
    # Electrostatics
    'coulomb_force',
    'electric_field',
    'electric_potential',
    
    # Magnetostatics
    'magnetic_field',
    'magnetic_force',
    'biot_savart',
    
    # Circuits
    'ohms_law',
    'power_dissipation',
    'impedance',
    
    # Waves
    'wave_equation',
    'electromagnetic_wave',
    
    # Maxwell's equations
    'gauss_law',
    'faraday_law',
    'ampere_law',
    
    # Optics
    'snells_law',
    'thin_lens_equation',
    'interference'
]

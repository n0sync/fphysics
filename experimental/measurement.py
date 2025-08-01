import numpy as np
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from constants import SPEED_OF_LIGHT, PLANCK_CONSTANT, AVOGADRO_NUMBER

def calculate_wavelength(frequency):
    """Calculate wavelength from frequency using speed of light."""
    return SPEED_OF_LIGHT / frequency

def calculate_energy(wavelength):
    """Calculate energy from wavelength using Planck's constant."""
    return PLANCK_CONSTANT * SPEED_OF_LIGHT / wavelength

def molarity_to_molality(molarity, density, molecular_weight):
    """Convert molarity (mol/L) to molality (mol/kg solvent)."""
    solvent_kg_per_l = (1.0 / density) - (molarity * molecular_weight / 1000.0)
    return molarity / solvent_kg_per_l

def calculate_beer_lambert(absorbance, path_length, molar_absorptivity):
    """Calculate concentration using Beer-Lambert law."""
    return absorbance / (molar_absorptivity * path_length)

def calculate_half_life(rate_constant):
    """Calculate half-life from rate constant."""
    return np.log(2) / rate_constant

def calculate_stopping_voltage(wavelength, work_function):
    """Calculate stopping voltage using photoelectric effect."""
    energy = calculate_energy(wavelength)
    stopping_voltage = energy - work_function
    return stopping_voltage

def calculate_number_of_particles(substance_mass, molecular_weight):
    """Calculate the number of particles using Avogadro's number."""
    moles = substance_mass / molecular_weight
    return moles * AVOGADRO_NUMBER

import math
from ..constants import *

def nernst_potential(ion_concentration_out, ion_concentration_in, valence):
    return (GAS_CONSTANT * BODY_TEMPERATURE) / (valence * FARADAY_CONSTANT) * math.log(ion_concentration_out / ion_concentration_in)

def goldman_hodgkin_katz_voltage(p_k, k_out, k_in, p_na, na_out, na_in, p_cl, cl_out, cl_in):
    return (GAS_CONSTANT * BODY_TEMPERATURE / FARADAY_CONSTANT) * math.log(
        (p_k * k_out + p_na * na_out + p_cl * cl_in) /
        (p_k * k_in + p_na * na_in + p_cl * cl_out)
    )

def membrane_capacitance(charge, voltage):
    return charge / voltage

def membrane_time_constant(membrane_resistance, membrane_capacitance_val):
    return membrane_resistance * membrane_capacitance_val

def membrane_potential_decay(initial_potential, time, time_constant):
    return initial_potential * math.exp(-time / time_constant)

def lipid_bilayer_surface_tension(lateral_pressure, thickness):
    return lateral_pressure * thickness

def passive_membrane_permeability(diffusion_coefficient, partition_coefficient, thickness):
    return (diffusion_coefficient * partition_coefficient) / thickness

def osmotic_pressure(solute_concentration):
    return solute_concentration * GAS_CONSTANT * BODY_TEMPERATURE

def membrane_bending_rigidity(youngs_modulus, thickness):
    return (youngs_modulus * thickness**3) / (12 * (1 - 0.5**2))

def donnan_equilibrium_ratio(ion_concentration_out, ion_concentration_in):
    return ion_concentration_out / ion_concentration_in

def membrane_surface_charge_density(total_charge, surface_area):
    return total_charge / surface_area

def debye_length(ionic_strength):
    return math.sqrt((VACUUM_PERMITTIVITY * GAS_CONSTANT * BODY_TEMPERATURE) / (2 * FARADAY_CONSTANT**2 * ionic_strength))

def membrane_fusion_energy_barrier(membrane_tension, fusion_pore_radius):
    return 8 * math.pi * membrane_tension * fusion_pore_radius**2

def electroporation_threshold_voltage(cell_radius, pulse_duration):
    return (1 / (1.5 * cell_radius)) * (1 + (pulse_duration / (2 * math.pi * 1e-6)))

def membrane_elastic_energy(area_strain, area_compressibility_modulus):
    return 0.5 * area_compressibility_modulus * area_strain**2


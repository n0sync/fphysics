import math
from ..constants import *

def radiation_dose_rate(activity, distance, gamma_constant=0.5):
    """Calculate radiation dose rate"""
    return gamma_constant * activity / (distance ** 2)

def half_value_layer(attenuation_coeff):
    """Calculate half-value layer thickness"""
    return math.log(2) / attenuation_coeff

def ct_number(mu_tissue, mu_water):
    """Calculate CT Hounsfield number"""
    return 1000 * (mu_tissue - mu_water) / mu_water

def mri_relaxation(t, t1):
    """MRI T1 relaxation recovery"""
    return 1 - math.exp(-t / t1)

def ultrasound_intensity(power, beam_area):
    """Calculate ultrasound intensity"""
    return power / beam_area

def radioactive_decay(n0, decay_constant, time):
    """Radioactive decay law"""
    return n0 * math.exp(-decay_constant * time)

def linear_energy_transfer(energy_loss, path_length):
    """Calculate linear energy transfer (LET)"""
    return energy_loss / path_length

def relative_biological_effectiveness(dose_test, dose_reference):
    """Calculate relative biological effectiveness (RBE)"""
    return dose_reference / dose_test

def bragg_peak_range(energy, density=1.0, z_eff=7.4):
    """Approximate Bragg peak range for protons"""
    return 0.31 * (energy ** 1.8) / (density * z_eff)

def compton_scatter_energy(incident_energy, scatter_angle):
    """Compton scattered photon energy"""
    electron_rest_energy = ELECTRON_MASS * SPEED_OF_LIGHT**2 / ELECTRON_VOLT
    denominator = 1 + (incident_energy / electron_rest_energy) * (1 - math.cos(scatter_angle))
    return incident_energy / denominator

def tissue_air_ratio(depth, field_size, energy):
    """Simplified tissue-air ratio calculation"""
    mu = 0.05 * energy**(-0.5)
    return math.exp(-mu * depth) * (1 + 0.1 * field_size)

def percent_depth_dose(depth, ssd=100, field_size=10, energy=6):
    """Percent depth dose calculation"""
    dmax = 0.9 + 0.15 * energy
    if depth <= dmax:
        return 100
    return 100 * math.exp(-0.05 * (depth - dmax))

def monitor_unit_calculation(prescribed_dose, dose_rate, field_factors=1.0):
    """Calculate monitor units for treatment"""
    return prescribed_dose / (dose_rate * field_factors)

def biological_effective_dose(physical_dose, alpha_beta_ratio, dose_per_fraction):
    """Calculate biological effective dose"""
    return physical_dose * (1 + dose_per_fraction / alpha_beta_ratio)

def effective_dose(absorbed_dose, radiation_weighting, tissue_weighting):
    """Calculate effective dose"""
    equivalent_dose = absorbed_dose * radiation_weighting
    return equivalent_dose * tissue_weighting


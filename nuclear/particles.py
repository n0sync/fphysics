"""
Particles Module
Functions for particle interactions and properties.
"""

import numpy as np
import matplotlib.pyplot as plt
from typing import Union, List, Tuple, Dict
from ..constants import *
import math


def particle_properties(particle_name: str) -> Dict:
    """Get properties of fundamental particles."""
    particles = {
        'electron': {'mass': ELECTRON_MASS, 'charge': -ELEMENTARY_CHARGE, 'spin': 0.5},
        'proton': {'mass': PROTON_MASS, 'charge': ELEMENTARY_CHARGE, 'spin': 0.5},
        'neutron': {'mass': NEUTRON_MASS, 'charge': 0, 'spin': 0.5},
        'muon': {'mass': MUON_MASS, 'charge': -ELEMENTARY_CHARGE, 'spin': 0.5},
        'tau': {'mass': TAU_MASS, 'charge': -ELEMENTARY_CHARGE, 'spin': 0.5},
        'alpha': {'mass': ALPHA_PARTICLE_MASS, 'charge': 2*ELEMENTARY_CHARGE, 'spin': 0},
        'deuteron': {'mass': DEUTERON_MASS, 'charge': ELEMENTARY_CHARGE, 'spin': 1},
        'triton': {'mass': TRITON_MASS, 'charge': ELEMENTARY_CHARGE, 'spin': 0.5},
        'pion+': {'mass': PION_CHARGED_MASS, 'charge': ELEMENTARY_CHARGE, 'spin': 0},
        'pion-': {'mass': PION_CHARGED_MASS, 'charge': -ELEMENTARY_CHARGE, 'spin': 0},
        'pion0': {'mass': PION_NEUTRAL_MASS, 'charge': 0, 'spin': 0},
        'kaon+': {'mass': KAON_CHARGED_MASS, 'charge': ELEMENTARY_CHARGE, 'spin': 0},
        'kaon-': {'mass': KAON_CHARGED_MASS, 'charge': -ELEMENTARY_CHARGE, 'spin': 0},
        'kaon0': {'mass': KAON_NEUTRAL_MASS, 'charge': 0, 'spin': 0}
    }
    
    if particle_name.lower() in particles:
        return particles[particle_name.lower()].copy()
    else:
        available = ', '.join(particles.keys())
        raise ValueError(f"Particle {particle_name} not found. Available: {available}")


def relativistic_energy(momentum: float, mass: float) -> float:
    """Calculate relativistic total energy."""
    return math.sqrt((momentum * SPEED_OF_LIGHT)**2 + (mass * SPEED_OF_LIGHT**2)**2)


def relativistic_momentum(energy: float, mass: float) -> float:
    """Calculate relativistic momentum."""
    return math.sqrt(energy**2 - (mass * SPEED_OF_LIGHT**2)**2) / SPEED_OF_LIGHT


def lorentz_factor(velocity: float) -> float:
    """Calculate Lorentz factor (gamma)."""
    beta = velocity / SPEED_OF_LIGHT
    return 1 / math.sqrt(1 - beta**2)


def kinetic_energy_relativistic(momentum: float, mass: float) -> float:
    """Calculate relativistic kinetic energy."""
    total_energy = relativistic_energy(momentum, mass)
    rest_energy = mass * SPEED_OF_LIGHT**2
    return total_energy - rest_energy


def de_broglie_wavelength(momentum: float) -> float:
    """Calculate de Broglie wavelength."""
    return PLANCK_CONSTANT / momentum


def compton_scattering(photon_energy: float, scattering_angle: float) -> float:
    """Calculate photon energy after Compton scattering."""
    energy_ratio = 1 + (photon_energy / (ELECTRON_MASS * SPEED_OF_LIGHT**2)) * (1 - math.cos(scattering_angle))
    return photon_energy / energy_ratio


def thomson_scattering_cross_section() -> float:
    """Return Thomson scattering cross-section."""
    return THOMSON_CROSS_SECTION


def klein_nishina_cross_section(photon_energy: float, scattering_angle: float) -> float:
    """Calculate Klein-Nishina cross-section for Compton scattering."""
    alpha = photon_energy / (ELECTRON_MASS * SPEED_OF_LIGHT**2)
    cos_theta = math.cos(scattering_angle)
    
    ratio = 1 / (1 + alpha * (1 - cos_theta))
    cross_section = (CLASSICAL_ELECTRON_RADIUS**2 / 2) * ratio**2 * \
                   (ratio + 1/ratio - (1 - cos_theta**2))
    
    return cross_section


def photoelectric_cross_section(photon_energy: float, Z: int) -> float:
    """Approximate photoelectric absorption cross-section."""
    # Simplified formula (valid for E >> binding energy)
    if photon_energy < 0.1:  # MeV
        return 0
    
    sigma_0 = 1.5e-28  # m² (approximate)
    return sigma_0 * Z**5 / (photon_energy / ELECTRON_VOLT)**3.5


def pair_production_cross_section(photon_energy: float, Z: int) -> float:
    """Approximate pair production cross-section."""
    threshold = 2 * ELECTRON_MASS * SPEED_OF_LIGHT**2
    
    if photon_energy < threshold:
        return 0
    
    sigma_0 = 1.4e-29  # m² (approximate)
    return sigma_0 * Z**2 * math.log(photon_energy / threshold)


def bremsstrahlung_spectrum(electron_energy: float, photon_energy: float, Z: int) -> float:
    """Calculate bremsstrahlung photon spectrum."""
    if photon_energy >= electron_energy:
        return 0
    
    # Simplified spectrum (not exact)
    alpha_factor = FINE_STRUCTURE_CONSTANT * Z**2
    return alpha_factor / photon_energy


def bethe_bloch_formula(particle_energy: float, particle_mass: float, particle_charge: float,
                       medium_Z: int, medium_A: float, medium_density: float) -> float:
    """Calculate energy loss rate using Bethe-Bloch formula."""
    beta = math.sqrt(1 - (particle_mass * SPEED_OF_LIGHT**2 / particle_energy)**2)
    gamma = 1 / math.sqrt(1 - beta**2)
    
    # Mean excitation energy (approximation)
    I = 16 * medium_Z**0.9 * ELECTRON_VOLT
    
    # Classical electron radius times electron density
    K = 4 * math.pi * CLASSICAL_ELECTRON_RADIUS**2 * ELECTRON_MASS * SPEED_OF_LIGHT**2
    n_e = medium_density * AVOGADRO_NUMBER * medium_Z / (medium_A * ATOMIC_MASS_UNIT)
    
    # Bethe-Bloch formula
    dE_dx = K * n_e * (particle_charge / ELEMENTARY_CHARGE)**2 / beta**2 * \
            (0.5 * math.log(2 * ELECTRON_MASS * SPEED_OF_LIGHT**2 * beta**2 * gamma**2 / I) - beta**2)
    
    return dE_dx  # J/m


def range_approximation(initial_energy: float, particle_mass: float, 
                       medium_density: float, medium_Z: int) -> float:
    """Approximate range of charged particle in medium."""
    # Geiger-Nuttal rule approximation
    if particle_mass == ALPHA_PARTICLE_MASS:
        # Alpha particle range in air at STP (empirical)
        range_air = 0.31 * (initial_energy / ELECTRON_VOLT / 1e6)**1.5  # cm
        return range_air * 1.225 / medium_density * 1e-2  # m
    else:
        # General approximation
        range_approx = initial_energy / (bethe_bloch_formula(initial_energy, particle_mass, 
                                       ELEMENTARY_CHARGE, medium_Z, medium_Z*2, medium_density))
        return range_approx


def bragg_peak_depth(particle_energy: float, particle_mass: float, 
                    medium_density: float) -> float:
    """Calculate depth of Bragg peak."""
    # Simplified calculation for protons in water
    if particle_mass == PROTON_MASS:
        # Empirical formula for protons in water
        energy_MeV = particle_energy / ELECTRON_VOLT / 1e6
        depth_cm = 0.022 * energy_MeV**1.77
        return depth_cm * medium_density / 1000 * 1e-2  # m
    else:
        return range_approximation(particle_energy, particle_mass, medium_density, 8) * 0.8


def multiple_scattering_angle(thickness: float, particle_momentum: float, 
                             particle_charge: float, medium_Z: int, medium_A: float) -> float:
    """Calculate RMS multiple scattering angle (Highland formula)."""
    # Radiation length (approximation)
    X0 = 716.4 * medium_A / (medium_Z * (medium_Z + 1) * math.log(287 / math.sqrt(medium_Z)))  # g/cm²
    X0_m = X0 * 1e-1 / 1000  # kg/m²
    
    # Highland formula
    theta_rms = 13.6e-3 * abs(particle_charge / ELEMENTARY_CHARGE) / particle_momentum * \
                math.sqrt(thickness / X0_m) * (1 + 0.038 * math.log(thickness / X0_m))
    
    return theta_rms


def cyclotron_frequency(particle_mass: float, particle_charge: float, magnetic_field: float) -> float:
    """Calculate cyclotron frequency."""
    return abs(particle_charge) * magnetic_field / particle_mass


def cyclotron_radius(particle_momentum: float, particle_charge: float, magnetic_field: float) -> float:
    """Calculate cyclotron radius."""
    return particle_momentum / (abs(particle_charge) * magnetic_field)


def synchrotron_power(particle_energy: float, particle_mass: float, 
                     particle_charge: float, magnetic_field: float) -> float:
    """Calculate synchrotron radiation power."""
    gamma = particle_energy / (particle_mass * SPEED_OF_LIGHT**2)
    beta = math.sqrt(1 - 1/gamma**2)
    
    power = (2 * CLASSICAL_ELECTRON_RADIUS * SPEED_OF_LIGHT / 3) * \
            (particle_charge / ELEMENTARY_CHARGE)**2 * \
            (ELECTRON_MASS / particle_mass)**2 * \
            beta**4 * gamma**4 * magnetic_field**2 / VACUUM_PERMEABILITY**2
    
    return power


def cherenkov_threshold(particle_mass: float, refractive_index: float) -> float:
    """Calculate Cherenkov radiation threshold energy."""
    beta_threshold = 1 / refractive_index
    gamma_threshold = 1 / math.sqrt(1 - beta_threshold**2)
    return (gamma_threshold - 1) * particle_mass * SPEED_OF_LIGHT**2


def cherenkov_angle(particle_velocity: float, refractive_index: float) -> float:
    """Calculate Cherenkov radiation angle."""
    beta = particle_velocity / SPEED_OF_LIGHT
    if beta < 1 / refractive_index:
        return 0
    return math.acos(1 / (refractive_index * beta))


def scattering_cross_section(impact_parameter: float, scattering_angle: float) -> float:
    """Calculate differential scattering cross-section."""
    # For Coulomb scattering
    if scattering_angle == 0:
        return float('inf')
    
    b = impact_parameter
    theta = scattering_angle
    
    # Rutherford formula
    sigma = (b / math.sin(theta/2))**2 * math.pi
    return sigma


def particle_interaction(particle1: str, particle2: str, energy: float) -> Dict:
    """Calculate interaction properties between particles."""
    p1 = particle_properties(particle1)
    p2 = particle_properties(particle2)
    
    # Calculate reduced mass
    reduced_mass = (p1['mass'] * p2['mass']) / (p1['mass'] + p2['mass'])
    
    # Calculate relative velocity (non-relativistic approximation)
    relative_velocity = math.sqrt(2 * energy / reduced_mass)
    
    # de Broglie wavelength
    momentum = reduced_mass * relative_velocity
    wavelength = de_broglie_wavelength(momentum)
    
    return {
        'reduced_mass': reduced_mass,
        'relative_velocity': relative_velocity,
        'momentum': momentum,
        'wavelength': wavelength
    }


def beta_decay_energy_spectrum(Q_value: float, electron_energy: float) -> float:
    """Calculate beta decay electron energy spectrum."""
    if electron_energy <= 0 or electron_energy >= Q_value:
        return 0
    
    # Simplified beta spectrum (not exact)
    neutrino_energy = Q_value - electron_energy
    return electron_energy * neutrino_energy**2


def alpha_decay_energy(Q_value: float, daughter_mass: float, alpha_mass: float = None) -> Tuple[float, float]:
    """Calculate kinetic energies in alpha decay."""
    if alpha_mass is None:
        alpha_mass = ALPHA_PARTICLE_MASS
    
    # Conservation of momentum and energy
    alpha_energy = Q_value * daughter_mass / (daughter_mass + alpha_mass)
    daughter_energy = Q_value * alpha_mass / (daughter_mass + alpha_mass)
    
    return alpha_energy, daughter_energy


def neutrino_oscillation_probability(distance: float, energy: float, 
                                   mass_diff_squared: float, mixing_angle: float) -> float:
    """Calculate neutrino oscillation probability."""
    # Simplified two-flavor oscillation
    L = distance  # m
    E = energy    # eV
    delta_m2 = mass_diff_squared  # eV²
    theta = mixing_angle  # radians
    
    oscillation_length = 4 * math.pi * E / delta_m2
    probability = (math.sin(2 * theta))**2 * (math.sin(math.pi * L / oscillation_length))**2
    
    return probability


def stopping_power_table(particle: str, energy_range: Tuple[float, float] = (0.1, 100)) -> Tuple[List[float], List[float]]:
    """Generate stopping power table for particle."""
    p = particle_properties(particle)
    energies = np.logspace(np.log10(energy_range[0]), np.log10(energy_range[1]), 100)
    
    stopping_powers = []
    for E in energies:
        E_joules = E * 1e6 * ELECTRON_VOLT  # Convert MeV to J
        # Approximate stopping power in water
        dE_dx = bethe_bloch_formula(E_joules, p['mass'], p['charge'], 8, 16, 1000)
        stopping_powers.append(dE_dx / ELECTRON_VOLT * 1e-6)  # MeV/m
    
    return energies.tolist(), stopping_powers


def plot_stopping_power(particle: str, energy_range: Tuple[float, float] = (0.1, 100)):
    """Plot stopping power vs energy."""
    energies, stopping_powers = stopping_power_table(particle, energy_range)
    
    plt.figure(figsize=(10, 6))
    plt.loglog(energies, stopping_powers, 'b-', linewidth=2)
    plt.xlabel('Kinetic Energy (MeV)')
    plt.ylabel('Stopping Power (MeV/m)')
    plt.title(f'Stopping Power for {particle.capitalize()}')
    plt.grid(True, alpha=0.3)
    plt.show()


PARTICLE_DETECTOR_RESPONSE = {
    'scintillator': {
        'light_yield': 10000,  # photons/MeV
        'decay_time': 2.4e-9,  # s
        'efficiency': 0.9
    },
    'semiconductor': {
        'energy_resolution': 0.001,  # FWHM/E
        'electron_hole_energy': 3.6,  # eV
        'efficiency': 0.8
    },
    'gas_detector': {
        'ionization_energy': 35,  # eV per ion pair
        'drift_velocity': 5e4,  # m/s
        'efficiency': 0.7
    }
}

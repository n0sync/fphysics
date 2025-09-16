import numpy as np
import matplotlib.pyplot as plt
from typing import Union, List, Tuple, Dict
from ..constants import *
import math


def particle_properties(particle_name: str) -> Dict:
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
    return math.sqrt((momentum * SPEED_OF_LIGHT)**2 + (mass * SPEED_OF_LIGHT**2)**2)


def relativistic_momentum(energy: float, mass: float) -> float:
    return math.sqrt(energy**2 - (mass * SPEED_OF_LIGHT**2)**2) / SPEED_OF_LIGHT


def lorentz_factor(velocity: float) -> float:
    beta = velocity / SPEED_OF_LIGHT
    return 1 / math.sqrt(1 - beta**2)


def kinetic_energy_relativistic(momentum: float, mass: float) -> float:
    total_energy = relativistic_energy(momentum, mass)
    rest_energy = mass * SPEED_OF_LIGHT**2
    return total_energy - rest_energy


def de_broglie_wavelength(momentum: float) -> float:
    return PLANCK_CONSTANT / momentum


def compton_scattering(photon_energy: float, scattering_angle: float) -> float:
    energy_ratio = 1 + (photon_energy / (ELECTRON_MASS * SPEED_OF_LIGHT**2)) * (1 - math.cos(scattering_angle))
    return photon_energy / energy_ratio


def thomson_scattering_cross_section() -> float:
    return THOMSON_CROSS_SECTION


def klein_nishina_cross_section(photon_energy: float, scattering_angle: float) -> float:
    alpha = photon_energy / (ELECTRON_MASS * SPEED_OF_LIGHT**2)
    cos_theta = math.cos(scattering_angle)
    ratio = 1 / (1 + alpha * (1 - cos_theta))
    cross_section = (CLASSICAL_ELECTRON_RADIUS**2 / 2) * ratio**2 * \
                   (ratio + 1/ratio - (1 - cos_theta**2))
    return cross_section


def photoelectric_cross_section(photon_energy: float, Z: int) -> float:
    if photon_energy < 0.1:
        return 0
    sigma_0 = 1.5e-28
    return sigma_0 * Z**5 / (photon_energy / ELECTRON_VOLT)**3.5


def pair_production_cross_section(photon_energy: float, Z: int) -> float:
    threshold = 2 * ELECTRON_MASS * SPEED_OF_LIGHT**2
    if photon_energy < threshold:
        return 0
    sigma_0 = 1.4e-29
    return sigma_0 * Z**2 * math.log(photon_energy / threshold)


def bremsstrahlung_spectrum(electron_energy: float, photon_energy: float, Z: int) -> float:
    if photon_energy >= electron_energy:
        return 0
    alpha_factor = FINE_STRUCTURE_CONSTANT * Z**2
    return alpha_factor / photon_energy


def bethe_bloch_formula(particle_energy: float, particle_mass: float, particle_charge: float,
                       medium_Z: int, medium_A: float, medium_density: float) -> float:
    beta = math.sqrt(1 - (particle_mass * SPEED_OF_LIGHT**2 / particle_energy)**2)
    gamma = 1 / math.sqrt(1 - beta**2)
    I = 16 * medium_Z**0.9 * ELECTRON_VOLT
    K = 4 * math.pi * CLASSICAL_ELECTRON_RADIUS**2 * ELECTRON_MASS * SPEED_OF_LIGHT**2
    n_e = medium_density * AVOGADRO_NUMBER * medium_Z / (medium_A * ATOMIC_MASS_UNIT)
    dE_dx = K * n_e * (particle_charge / ELEMENTARY_CHARGE)**2 / beta**2 * \
            (0.5 * math.log(2 * ELECTRON_MASS * SPEED_OF_LIGHT**2 * beta**2 * gamma**2 / I) - beta**2)
    return dE_dx


def range_approximation(initial_energy: float, particle_mass: float, 
                       medium_density: float, medium_Z: int) -> float:
    if particle_mass == ALPHA_PARTICLE_MASS:
        range_air = 0.31 * (initial_energy / ELECTRON_VOLT / 1e6)**1.5
        return range_air * 1.225 / medium_density * 1e-2
    else:
        range_approx = initial_energy / (bethe_bloch_formula(initial_energy, particle_mass, 
                                       ELEMENTARY_CHARGE, medium_Z, medium_Z*2, medium_density))
        return range_approx


def bragg_peak_depth(particle_energy: float, particle_mass: float, 
                    medium_density: float) -> float:
    if particle_mass == PROTON_MASS:
        energy_MeV = particle_energy / ELECTRON_VOLT / 1e6
        depth_cm = 0.022 * energy_MeV**1.77
        return depth_cm * medium_density / 1000 * 1e-2
    else:
        return range_approximation(particle_energy, particle_mass, medium_density, 8) * 0.8


def multiple_scattering_angle(thickness: float, particle_momentum: float, 
                             particle_charge: float, medium_Z: int, medium_A: float) -> float:
    X0 = 716.4 * medium_A / (medium_Z * (medium_Z + 1) * math.log(287 / math.sqrt(medium_Z)))
    X0_m = X0 * 1e-1 / 1000
    theta_rms = 13.6e-3 * abs(particle_charge / ELEMENTARY_CHARGE) / particle_momentum * \
                math.sqrt(thickness / X0_m) * (1 + 0.038 * math.log(thickness / X0_m))
    return theta_rms


def cyclotron_frequency(particle_mass: float, particle_charge: float, magnetic_field: float) -> float:
    return abs(particle_charge) * magnetic_field / particle_mass


def cyclotron_radius(particle_momentum: float, particle_charge: float, magnetic_field: float) -> float:
    return particle_momentum / (abs(particle_charge) * magnetic_field)


def synchrotron_power(particle_energy: float, particle_mass: float, 
                     particle_charge: float, magnetic_field: float) -> float:
    gamma = particle_energy / (particle_mass * SPEED_OF_LIGHT**2)
    beta = math.sqrt(1 - 1/gamma**2)
    power = (2 * CLASSICAL_ELECTRON_RADIUS * SPEED_OF_LIGHT / 3) * \
            (particle_charge / ELEMENTARY_CHARGE)**2 * \
            (ELECTRON_MASS / particle_mass)**2 * \
            beta**4 * gamma**4 * magnetic_field**2 / VACUUM_PERMEABILITY**2
    return power


def cherenkov_threshold(particle_mass: float, refractive_index: float) -> float:
    beta_threshold = 1 / refractive_index
    gamma_threshold = 1 / math.sqrt(1 - beta_threshold**2)
    return (gamma_threshold - 1) * particle_mass * SPEED_OF_LIGHT**2


def cherenkov_angle(particle_velocity: float, refractive_index: float) -> float:
    beta = particle_velocity / SPEED_OF_LIGHT
    if beta < 1 / refractive_index:
        return 0
    return math.acos(1 / (refractive_index * beta))


def scattering_cross_section(impact_parameter: float, scattering_angle: float) -> float:
    if scattering_angle == 0:
        return float('inf')
    b = impact_parameter
    theta = scattering_angle
    sigma = (b / math.sin(theta/2))**2 * math.pi
    return sigma


def particle_interaction(particle1: str, particle2: str, energy: float) -> Dict:
    p1 = particle_properties(particle1)
    p2 = particle_properties(particle2)
    reduced_mass = (p1['mass'] * p2['mass']) / (p1['mass'] + p2['mass'])
    relative_velocity = math.sqrt(2 * energy / reduced_mass)
    momentum = reduced_mass * relative_velocity
    wavelength = de_broglie_wavelength(momentum)
    return {
        'reduced_mass': reduced_mass,
        'relative_velocity': relative_velocity,
        'momentum': momentum,
        'wavelength': wavelength
    }


def beta_decay_energy_spectrum(Q_value: float, electron_energy: float) -> float:
    if electron_energy <= 0 or electron_energy >= Q_value:
        return 0
    neutrino_energy = Q_value - electron_energy
    return electron_energy * neutrino_energy**2


def alpha_decay_energy(Q_value: float, daughter_mass: float, alpha_mass: float = None) -> Tuple[float, float]:
    if alpha_mass is None:
        alpha_mass = ALPHA_PARTICLE_MASS
    alpha_energy = Q_value * daughter_mass / (daughter_mass + alpha_mass)
    daughter_energy = Q_value * alpha_mass / (daughter_mass + alpha_mass)
    return alpha_energy, daughter_energy


def neutrino_oscillation_probability(distance: float, energy: float, 
                                   mass_diff_squared: float, mixing_angle: float) -> float:
    L = distance
    E = energy
    delta_m2 = mass_diff_squared
    theta = mixing_angle
    oscillation_length = 4 * math.pi * E / delta_m2
    probability = (math.sin(2 * theta))**2 * (math.sin(math.pi * L / oscillation_length))**2
    return probability


def stopping_power_table(particle: str, energy_range: Tuple[float, float] = (0.1, 100)) -> Tuple[List[float], List[float]]:
    p = particle_properties(particle)
    energies = np.logspace(np.log10(energy_range[0]), np.log10(energy_range[1]), 100)
    stopping_powers = []
    for E in energies:
        E_joules = E * 1e6 * ELECTRON_VOLT
        dE_dx = bethe_bloch_formula(E_joules, p['mass'], p['charge'], 8, 16, 1000)
        stopping_powers.append(dE_dx / ELECTRON_VOLT * 1e-6)
    return energies.tolist(), stopping_powers


def plot_stopping_power(particle: str, energy_range: Tuple[float, float] = (0.1, 100)):
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
        'light_yield': 10000,
        'decay_time': 2.4e-9,
        'efficiency': 0.9
    },
    'semiconductor': {
        'energy_resolution': 0.001,
        'electron_hole_energy': 3.6,
        'efficiency': 0.8
    },
    'gas_detector': {
        'ionization_energy': 35,
        'drift_velocity': 5e4,
        'efficiency': 0.7
    }
}

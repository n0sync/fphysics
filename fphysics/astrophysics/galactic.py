import math
from ..constants import *

def circular_velocity(enclosed_mass, radius):
    """
    Calculate circular velocity in a galactic potential.
    
    Args:
        enclosed_mass (float): Mass enclosed within radius (kg)
        radius (float): Distance from galactic center (m)
    
    Returns:
        float: Circular velocity (m/s)
    """
    return math.sqrt(GRAVITATIONAL_CONSTANT * enclosed_mass / radius)


def rotation_curve(mass_profile, radius_array):
    """
    Calculate rotation curve for given mass profile.
    
    Args:
        mass_profile (list): Enclosed mass at each radius (kg)
        radius_array (list): Radial distances (m)
    
    Returns:
        list: Circular velocities (m/s)
    """
    velocities = []
    for i, radius in enumerate(radius_array):
        if radius > 0:
            v_circ = math.sqrt(GRAVITATIONAL_CONSTANT * mass_profile[i] / radius)
            velocities.append(v_circ)
        else:
            velocities.append(0)
    return velocities


def oort_constants(velocity, radius, velocity_gradient):
    """
    Calculate Oort A and B constants from rotation curve.
    
    Args:
        velocity (float): Circular velocity at solar radius (m/s)
        radius (float): Solar galactocentric radius (m)
        velocity_gradient (float): dV/dR at solar position (s⁻¹)
    
    Returns:
        tuple: (Oort A, Oort B) constants (s⁻¹)
    """
    omega = velocity / radius  # Angular velocity
    A = -0.5 * velocity_gradient
    B = -0.5 * (velocity_gradient + 2 * omega)
    return A, B


def galactic_escape_velocity(total_mass, galactic_radius):
    """
    Calculate escape velocity from galaxy.
    
    Args:
        total_mass (float): Total galactic mass (kg)
        galactic_radius (float): Galactic radius (m)
    
    Returns:
        float: Escape velocity (m/s)
    """
    return math.sqrt(2 * GRAVITATIONAL_CONSTANT * total_mass / galactic_radius)


def virial_mass(velocity_dispersion, radius):
    """
    Calculate virial mass of galactic system.
    
    Args:
        velocity_dispersion (float): 3D velocity dispersion (m/s)
        radius (float): System radius (m)
    
    Returns:
        float: Virial mass (kg)
    """
    return (5 * velocity_dispersion**2 * radius) / GRAVITATIONAL_CONSTANT


def disk_scale_height(velocity_dispersion, surface_density):
    """
    Calculate disk scale height using hydrostatic equilibrium.
    
    Args:
        velocity_dispersion (float): Vertical velocity dispersion (m/s)
        surface_density (float): Disk surface density (kg/m²)
    
    Returns:
        float: Scale height (m)
    """
    return velocity_dispersion**2 / (PI * GRAVITATIONAL_CONSTANT * surface_density)


def spiral_density_wave(radius, pattern_speed, arm_number=2):
    """
    Calculate spiral arm pattern for density wave theory.
    
    Args:
        radius (float): Galactocentric radius (m)
        pattern_speed (float): Pattern angular velocity (rad/s)
        arm_number (int): Number of spiral arms
    
    Returns:
        float: Spiral phase angle (radians)
    """
    # Simplified logarithmic spiral
    pitch_angle = math.pi / 6  # ~30 degrees typical
    return arm_number * (math.log(radius) / math.tan(pitch_angle))


def toomre_q_parameter(velocity_dispersion, surface_density, epicyclic_frequency):
    """
    Calculate Toomre Q parameter for disk stability.
    
    Args:
        velocity_dispersion (float): Radial velocity dispersion (m/s)
        surface_density (float): Surface density (kg/m²)
        epicyclic_frequency (float): Epicyclic frequency (rad/s)
    
    Returns:
        float: Toomre Q parameter (dimensionless)
    """
    return (velocity_dispersion * epicyclic_frequency) / (PI * GRAVITATIONAL_CONSTANT * surface_density)


def epicyclic_frequency(velocity, radius, velocity_derivative):
    """
    Calculate epicyclic frequency for galactic orbits.
    
    Args:
        velocity (float): Circular velocity (m/s)
        radius (float): Galactocentric radius (m)
        velocity_derivative (float): dV/dR (s⁻¹)
    
    Returns:
        float: Epicyclic frequency (rad/s)
    """
    omega = velocity / radius
    return math.sqrt(2 * omega * (omega + velocity_derivative))


def vertical_frequency(surface_density):
    """
    Calculate vertical oscillation frequency in galactic disk.
    
    Args:
        surface_density (float): Disk surface density (kg/m²)
    
    Returns:
        float: Vertical frequency (rad/s)
    """
    return math.sqrt(2 * PI * GRAVITATIONAL_CONSTANT * surface_density)


def lindblad_resonances(pattern_speed, orbital_frequency, epicyclic_freq):
    """
    Find Lindblad resonance conditions.
    
    Args:
        pattern_speed (float): Pattern angular velocity (rad/s)
        orbital_frequency (float): Orbital frequency (rad/s)
        epicyclic_freq (float): Epicyclic frequency (rad/s)
    
    Returns:
        dict: Inner and outer Lindblad resonance frequencies
    """
    ilr_condition = orbital_frequency - epicyclic_freq/2 - pattern_speed
    olr_condition = orbital_frequency + epicyclic_freq/2 - pattern_speed
    
    return {
        'inner_lindblad': abs(ilr_condition),
        'outer_lindblad': abs(olr_condition),
        'corotation': abs(orbital_frequency - pattern_speed)
    }


def dark_matter_profile(radius, scale_radius=8.5e3*PARSEC, rho_0=0.3e-21):
    """
    Calculate dark matter density using NFW profile.
    
    Args:
        radius (float): Distance from galactic center (m)
        scale_radius (float): Scale radius (m)
        rho_0 (float): Characteristic density (kg/m³)
    
    Returns:
        float: Dark matter density (kg/m³)
    """
    x = radius / scale_radius
    return rho_0 / (x * (1 + x)**2)


def stellar_relaxation_time(stellar_density, stellar_mass, velocity_dispersion):
    """
    Calculate two-body relaxation time for stellar system.
    
    Args:
        stellar_density (float): Number density of stars (m⁻³)
        stellar_mass (float): Typical stellar mass (kg)
        velocity_dispersion (float): Velocity dispersion (m/s)
    
    Returns:
        float: Relaxation time (s)
    """
    coulomb_log = 10  # Typical value
    return (velocity_dispersion**3) / (4 * PI * GRAVITATIONAL_CONSTANT**2 * stellar_mass**2 * stellar_density * coulomb_log)


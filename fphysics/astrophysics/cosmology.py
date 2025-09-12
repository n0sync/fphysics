import math
from ..constants import *

def hubble_distance():
    """
    Calculate Hubble distance (c/H₀).
    
    Returns:
        float: Hubble distance (m)
    """
    return SPEED_OF_LIGHT / HUBBLE_CONSTANT


def lookback_time(redshift, omega_m=0.31, omega_lambda=0.69):
    """
    Calculate lookback time to given redshift.
    
    Args:
        redshift (float): Cosmological redshift z
        omega_m (float): Matter density parameter
        omega_lambda (float): Dark energy density parameter
    
    Returns:
        float: Lookback time (s)
    """
    # Simplified approximation for flat universe
    hubble_time = 1 / HUBBLE_CONSTANT
    integral_approx = (2/3) * (1/math.sqrt(omega_lambda)) * math.asinh(math.sqrt(omega_lambda/omega_m))
    return hubble_time * integral_approx * (1 - 1/math.sqrt(1 + redshift))


def comoving_distance(redshift, omega_m=0.31, omega_lambda=0.69):
    """
    Calculate comoving distance to given redshift.
    
    Args:
        redshift (float): Cosmological redshift z
        omega_m (float): Matter density parameter
        omega_lambda (float): Dark energy density parameter
    
    Returns:
        float: Comoving distance (m)
    """
    # Simplified for flat universe
    dh = hubble_distance()
    # Numerical integration approximation
    z_steps = max(100, int(redshift * 100))
    dz = redshift / z_steps
    integral = 0
    
    for i in range(z_steps):
        z = i * dz
        ez = math.sqrt(omega_m * (1 + z)**3 + omega_lambda)
        integral += dz / ez
    
    return dh * integral


def angular_diameter_distance(redshift, omega_m=0.31, omega_lambda=0.69):
    """
    Calculate angular diameter distance.
    
    Args:
        redshift (float): Cosmological redshift z
        omega_m (float): Matter density parameter
        omega_lambda (float): Dark energy density parameter
    
    Returns:
        float: Angular diameter distance (m)
    """
    dc = comoving_distance(redshift, omega_m, omega_lambda)
    return dc / (1 + redshift)


def luminosity_distance(redshift, omega_m=0.31, omega_lambda=0.69):
    """
    Calculate luminosity distance.
    
    Args:
        redshift (float): Cosmological redshift z
        omega_m (float): Matter density parameter
        omega_lambda (float): Dark energy density parameter
    
    Returns:
        float: Luminosity distance (m)
    """
    dc = comoving_distance(redshift, omega_m, omega_lambda)
    return dc * (1 + redshift)


def critical_density():
    """
    Calculate critical density of the universe.
    
    Returns:
        float: Critical density (kg/m³)
    """
    return (3 * HUBBLE_CONSTANT**2) / (8 * PI * GRAVITATIONAL_CONSTANT)


def density_parameter(density, critical_dens=None):
    """
    Calculate density parameter Ω.
    
    Args:
        density (float): Density (kg/m³)
        critical_dens (float): Critical density (kg/m³), optional
    
    Returns:
        float: Density parameter (dimensionless)
    """
    if critical_dens is None:
        critical_dens = critical_density()
    return density / critical_dens


def age_of_universe(omega_m=0.31, omega_lambda=0.69):
    """
    Calculate age of universe for given cosmological parameters.
    
    Args:
        omega_m (float): Matter density parameter
        omega_lambda (float): Dark energy density parameter
    
    Returns:
        float: Age of universe (s)
    """
    hubble_time = 1 / HUBBLE_CONSTANT
    # Approximation for flat universe
    if omega_lambda > 0:
        integral = (2/3) * (1/math.sqrt(omega_lambda)) * math.asinh(math.sqrt(omega_lambda/omega_m))
        return hubble_time * integral
    else:
        # Matter-dominated universe
        return (2/3) * hubble_time / math.sqrt(omega_m)


def scale_factor(redshift):
    """
    Calculate scale factor from redshift.
    
    Args:
        redshift (float): Cosmological redshift z
    
    Returns:
        float: Scale factor a (dimensionless)
    """
    return 1 / (1 + redshift)


def redshift_from_scale_factor(scale_factor):
    """
    Calculate redshift from scale factor.
    
    Args:
        scale_factor (float): Scale factor a
    
    Returns:
        float: Redshift z
    """
    return (1 / scale_factor) - 1


def friedmann_equation(scale_factor, omega_m, omega_lambda, omega_k=0):
    """
    Calculate Hubble parameter using Friedmann equation.
    
    Args:
        scale_factor (float): Scale factor a
        omega_m (float): Matter density parameter
        omega_lambda (float): Dark energy density parameter  
        omega_k (float): Curvature density parameter
    
    Returns:
        float: Hubble parameter H(a) (s⁻¹)
    """
    h_squared = omega_m / scale_factor**3 + omega_k / scale_factor**2 + omega_lambda
    return HUBBLE_CONSTANT * math.sqrt(h_squared)


def radiation_temperature(redshift):
    """
    Calculate CMB temperature at given redshift.
    
    Args:
        redshift (float): Cosmological redshift z
    
    Returns:
        float: CMB temperature (K)
    """
    return COSMIC_MICROWAVE_BACKGROUND_TEMP * (1 + redshift)


def jeans_length_cosmological(temperature, density, redshift):
    """
    Calculate Jeans length in cosmological context.
    
    Args:
        temperature (float): Gas temperature (K)
        density (float): Gas density (kg/m³)
        redshift (float): Cosmological redshift z
    
    Returns:
        float: Jeans length (m)
    """
    sound_speed_sq = BOLTZMANN_CONSTANT * temperature / (2.33e-27)  # Mean molecular weight
    return math.sqrt(PI * sound_speed_sq / (GRAVITATIONAL_CONSTANT * density))


def horizon_distance(time):
    """
    Calculate particle horizon distance.
    
    Args:
        time (float): Cosmic time (s)
    
    Returns:
        float: Horizon distance (m)
    """
    return SPEED_OF_LIGHT * time


def sound_horizon(redshift_equality=3200):
    """
    Calculate sound horizon at recombination.
    
    Args:
        redshift_equality (float): Matter-radiation equality redshift
    
    Returns:
        float: Sound horizon (m)
    """
    # Simplified calculation
    c_s = SPEED_OF_LIGHT / math.sqrt(3)  # Sound speed in radiation-dominated era
    t_rec = age_of_universe() * 0.003  # Rough recombination time fraction
    return c_s * t_rec


def baryon_acoustic_oscillation_scale(redshift):
    """
    Calculate BAO angular scale.
    
    Args:
        redshift (float): Redshift of observation
    
    Returns:
        float: BAO angular scale (radians)
    """
    sound_horizon_rec = sound_horizon()
    da = angular_diameter_distance(redshift)
    return sound_horizon_rec / da


def silk_damping_scale(redshift):
    """
    Calculate Silk damping scale for acoustic oscillations.
    
    Args:
        redshift (float): Cosmological redshift z
    
    Returns:
        float: Silk damping scale (m)
    """
    # Simplified approximation
    omega_b = 0.05  # Baryon density parameter
    r_s = sound_horizon()
    return r_s / math.sqrt(1 + redshift) * math.sqrt(omega_b)


def dark_energy_equation_of_state(redshift, w0=-1, wa=0):
    """
    Calculate dark energy equation of state parameter.
    
    Args:
        redshift (float): Cosmological redshift z
        w0 (float): Present-day equation of state
        wa (float): Evolution parameter
    
    Returns:
        float: Equation of state w(z)
    """
    a = scale_factor(redshift)
    return w0 + wa * (1 - a)


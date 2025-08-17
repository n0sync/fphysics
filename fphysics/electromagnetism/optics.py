import numpy as np
from constants import *

# Snell's Law
def snells_law(n1, n2, theta1):
    return np.arcsin(n1 * np.sin(theta1) / n2)

def critical_angle(n1, n2):
    return np.arcsin(n2 / n1) if n1 > n2 else None

# Reflection and Refraction
def fresnel_equations(n1, n2, theta1):
    theta2 = snells_law(n1, n2, theta1)
    rs = ((n1 * np.cos(theta1) - n2 * np.cos(theta2)) /
          (n1 * np.cos(theta1) + n2 * np.cos(theta2)))
    rp = ((n2 * np.cos(theta1) - n1 * np.cos(theta2)) /
          (n2 * np.cos(theta1) + n1 * np.cos(theta2)))
    ts = 2 * n1 * np.cos(theta1) / (n1 * np.cos(theta1) + n2 * np.cos(theta2))
    tp = 2 * n1 * np.cos(theta1) / (n2 * np.cos(theta1) + n1 * np.cos(theta2))
    return rs, rp, ts, tp

def reflectance(rs, rp):
    return (abs(rs)**2, abs(rp)**2)

def transmittance(ts, tp, n1, n2, theta1, theta2):
    ref_trans_s = (n2 * np.cos(theta2) * abs(ts)**2) / (n1 * np.cos(theta1))
    ref_trans_p = (n2 * np.cos(theta2) * abs(tp)**2) / (n1 * np.cos(theta1))
    return ref_trans_s, ref_trans_p

# Lens and Mirrors
def lensmaker_equation(n, R1, R2, d=0):
    return 1 / ((n - 1) * (1/R1 - 1/R2 + ((n - 1) * d) / (n * R1 * R2)))

def mirror_equation(f, do):
    return 1 / (1 / f - 1 / do)

def magnification(hi, ho):
    return -hi / ho

def thin_lens_equation(f, do):
    return 1 / (1 / f - 1 / do)

# Interference
def youngs_double_slit(d, L, wavelength):
    return (wavelength * L) / d

def interference_intensity(I0, delta):
    return I0 * (1 + np.cos(delta))

def interference_maxima(d, m, wavelength):
    return d * m / wavelength

def interference_minima(d, m, wavelength):
    return d * (m + 0.5) / wavelength

def thin_film_interference(n1, n2, t, wavelength):
    return 2 * n1 * t / wavelength

# Diffraction
def single_slit_diffraction(a, wavelength, theta):
    return np.sin(theta) / a, wavelength

def diffraction_grating(d, m, wavelength):
    return np.arcsin(m * wavelength / d)

def rayleigh_criterion(D, wavelength):
    return 1.22 * wavelength / D

def airy_disk_radius(wavelength, f_number):
    return 1.22 * wavelength * f_number

# Polarization
def malus_law(I0, theta):
    return I0 * np.cos(theta)**2

def brewster_angle(n1, n2):
    return np.arctan(n2 / n1)

def polarization_ratio(I_parallel, I_perpendicular):
    return I_parallel / I_perpendicular

def dichroism_angle(I_max, I_min):
    return 0.5 * np.arctan2((I_max - I_min), (I_max + I_min))

# Optical Instruments
def focal_length_combine(f1, f2, d):
    return 1 / (1 / f1 + 1 / f2 - d / (f1 * f2))

def refractive_power(f):
    return 1 / f

def numerical_aperture(n, theta):
    return n * np.sin(theta)

def resolving_power(wavelength, D):
    return D / (1.22 * wavelength)

def microscope_magnification(oc, ob):
    return oc * ob

# Optical Coatings
def anti_reflection_coating(n1, n2, wavelength):
    return wavelength / (4 * n2)

def optical_thickness(n, t):
    return n * t

def coating_interference(n_film, n_substrate):
    return 2 * n_film / n_substrate

# Fiber Optics
def acceptance_angle(n_core, n_cladding):
    return np.arcsin(np.sqrt(n_core**2 - n_cladding**2))

def critical_angle_fiber(n_core, n_cladding):
    return np.arcsin(n_cladding / n_core)

def numerical_aperture_fiber(n_core, n_cladding):
    return np.sqrt(n_core**2 - n_cladding**2)

def mode_field_diameter(wavelength, n_core, n_cladding):
    return wavelength / (np.pi * np.sqrt(n_core**2 - n_cladding**2))

def v_number(d, n_core, n_cladding, wavelength):
    return np.pi * d * np.sqrt(n_core**2 - n_cladding**2) / wavelength

# Geometric Optics
def object_image_distance(f, s):
    return 1 / (1 / f - 1 / s)

def radius_of_curvature(f):
    return 2 * f

def optical_path_difference(n, s):
    return n * s

def ray_transfer_matrix(A, B, C, D):
    return np.array([[A, B], [C, D]])

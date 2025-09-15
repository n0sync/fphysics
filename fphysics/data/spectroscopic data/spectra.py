import numpy as np
from ..constants import *

# Data Loading
def load_spectrum_txt(filepath, delimiter="\t", skiprows=0):
    data = np.loadtxt(filepath, delimiter=delimiter, skiprows=skiprows)
    return data[:, 0], data[:, 1]  # x, y

def save_spectrum_txt(x, y, filepath, delimiter="\t"):
    data = np.column_stack((x, y))
    np.savetxt(filepath, data, delimiter=delimiter)

# Preprocessing
def normalize_spectrum(spectrum, method='max'):
    if method == 'max':
        return spectrum / np.max(spectrum)
    elif method == 'area':
        return spectrum / np.trapz(spectrum)
    elif method == 'rms':
        return spectrum / np.sqrt(np.mean(spectrum**2))

def baseline_correction(spectrum, method='linear'):
    if method == 'linear':
        x = np.arange(len(spectrum))
        slope = (spectrum[-1] - spectrum[0]) / (len(spectrum) - 1)
        baseline = spectrum[0] + slope * x
        return spectrum - baseline
    elif method == 'polynomial':
        x = np.arange(len(spectrum))
        poly = np.polyfit(x, spectrum, deg=2)
        baseline = np.polyval(poly, x)
        return spectrum - baseline

def smooth_spectrum(spectrum, window_size=5, method='moving_average'):
    if method == 'moving_average':
        kernel = np.ones(window_size) / window_size
        return np.convolve(spectrum, kernel, mode='same')
    elif method == 'gaussian':
        x = np.arange(-window_size//2 + 1, window_size//2 + 1)
        kernel = np.exp(-x**2 / (2 * (window_size/4)**2))
        kernel = kernel / np.sum(kernel)
        return np.convolve(spectrum, kernel, mode='same')

# Peak Analysis
def find_peaks_simple(spectrum, threshold=0.1, min_distance=10):
    peaks = []
    for i in range(min_distance, len(spectrum) - min_distance):
        if (spectrum[i] > threshold and 
            spectrum[i] > spectrum[i-1] and 
            spectrum[i] > spectrum[i+1]):
            is_peak = True
            for j in range(max(0, i-min_distance), min(len(spectrum), i+min_distance)):
                if spectrum[j] > spectrum[i] and j != i:
                    is_peak = False
                    break
            if is_peak:
                peaks.append(i)
    return np.array(peaks)

def peak_width_fwhm(x, y, peak_index):
    peak_height = y[peak_index]
    half_max = peak_height / 2
    
    left_idx = peak_index
    while left_idx > 0 and y[left_idx] > half_max:
        left_idx -= 1
    
    right_idx = peak_index
    while right_idx < len(y) - 1 and y[right_idx] > half_max:
        right_idx += 1
    
    return x[right_idx] - x[left_idx]

def peak_area_trapz(x, y, peak_center, width):
    start = max(0, peak_center - width//2)
    end = min(len(y), peak_center + width//2)
    return np.trapz(y[start:end], x[start:end])

def peak_fit_gaussian(x, y, center_guess, amp_guess=None, width_guess=1):
    if amp_guess is None:
        amp_guess = np.max(y)
    
    def gaussian(x, amp, center, width):
        return amp * np.exp(-(x - center)**2 / (2 * width**2))
    
    # Simple least squares fitting
    def residuals(params):
        amp, center, width = params
        return np.sum((y - gaussian(x, amp, center, width))**2)
    
    # Grid search for better initial guess
    best_params = [amp_guess, center_guess, width_guess]
    best_residual = residuals(best_params)
    
    for amp in np.linspace(amp_guess*0.5, amp_guess*1.5, 10):
        for center in np.linspace(center_guess-2, center_guess+2, 10):
            for width in np.linspace(0.5, 3, 10):
                params = [amp, center, width]
                res = residuals(params)
                if res < best_residual:
                    best_residual = res
                    best_params = params
    
    return best_params

# Spectral Operations
def interpolate_linear(x, y, new_x):
    new_y = np.zeros_like(new_x)
    for i, xi in enumerate(new_x):
        if xi <= x[0]:
            new_y[i] = y[0]
        elif xi >= x[-1]:
            new_y[i] = y[-1]
        else:
            idx = np.searchsorted(x, xi)
            if idx == 0:
                new_y[i] = y[0]
            else:
                x1, x2 = x[idx-1], x[idx]
                y1, y2 = y[idx-1], y[idx]
                new_y[i] = y1 + (y2 - y1) * (xi - x1) / (x2 - x1)
    return new_y

def resample_spectrum(x, y, num_points):
    new_x = np.linspace(x[0], x[-1], num_points)
    new_y = interpolate_linear(x, y, new_x)
    return new_x, new_y

def crop_spectrum(x, y, x_min, x_max):
    mask = (x >= x_min) & (x <= x_max)
    return x[mask], y[mask]

def subtract_spectra(y1, y2):
    return y1 - y2

def add_spectra(y1, y2):
    return y1 + y2

def multiply_spectra(y1, y2):
    return y1 * y2

def divide_spectra(y1, y2, avoid_zero=1e-10):
    return y1 / (y2 + avoid_zero)

# Calibration
def wavelength_to_wavenumber(wavelength):
    return 1e7 / wavelength

def wavenumber_to_wavelength(wavenumber):
    return 1e7 / wavenumber

def frequency_to_wavenumber(frequency):
    return frequency / SPEED_OF_LIGHT

def energy_to_wavenumber(energy):
    return energy / (PLANCK_CONSTANT * SPEED_OF_LIGHT)

def apply_calibration_polynomial(x, coefficients):
    return np.polyval(coefficients, x)

def linear_calibration(x, slope, intercept):
    return slope * x + intercept

# Signal Processing
def fourier_transform(spectrum):
    return np.fft.fft(spectrum)

def inverse_fourier_transform(ft_spectrum):
    return np.fft.ifft(ft_spectrum).real

def apply_window(spectrum, window_type='hann'):
    n = len(spectrum)
    if window_type == 'hann':
        window = 0.5 - 0.5 * np.cos(2 * np.pi * np.arange(n) / (n - 1))
    elif window_type == 'hamming':
        window = 0.54 - 0.46 * np.cos(2 * np.pi * np.arange(n) / (n - 1))
    elif window_type == 'blackman':
        window = (0.42 - 0.5 * np.cos(2 * np.pi * np.arange(n) / (n - 1)) + 
                 0.08 * np.cos(4 * np.pi * np.arange(n) / (n - 1)))
    else:
        window = np.ones(n)
    return spectrum * window

def zero_fill(spectrum, factor=2):
    zeros = np.zeros(len(spectrum) * (factor - 1))
    return np.concatenate([spectrum, zeros])

# Statistical Analysis
def signal_to_noise_ratio(spectrum, noise_start, noise_end, signal_index):
    noise = np.std(spectrum[noise_start:noise_end])
    signal = spectrum[signal_index]
    return signal / noise if noise > 0 else float('inf')

def spectral_correlation(spectrum1, spectrum2):
    mean1, mean2 = np.mean(spectrum1), np.mean(spectrum2)
    num = np.sum((spectrum1 - mean1) * (spectrum2 - mean2))
    den = np.sqrt(np.sum((spectrum1 - mean1)**2) * np.sum((spectrum2 - mean2)**2))
    return num / den if den > 0 else 0

def spectral_rmse(spectrum1, spectrum2):
    return np.sqrt(np.mean((spectrum1 - spectrum2)**2))

def spectral_mae(spectrum1, spectrum2):
    return np.mean(np.abs(spectrum1 - spectrum2))

# Quantitative Analysis
def beers_law_concentration(absorbance, path_length, molar_absorptivity):
    return absorbance / (molar_absorptivity * path_length)

def concentration_from_calibration(intensity, slope, intercept):
    return (intensity - intercept) / slope

def limit_of_detection(blank_std, slope, k=3):
    return k * blank_std / slope

def limit_of_quantification(blank_std, slope, k=10):
    return k * blank_std / slope

# Spectroscopic Techniques
def raman_shift(laser_wavenumber, scattered_wavenumber):
    return laser_wavenumber - scattered_wavenumber

def ir_transmittance_to_absorbance(transmittance):
    return -np.log10(np.maximum(transmittance, 1e-10))

def ir_absorbance_to_transmittance(absorbance):
    return 10**(-absorbance)

def fluorescence_quantum_yield(integrated_sample, integrated_reference, 
                             abs_reference, abs_sample, n_sample=1, n_reference=1):
    return (integrated_sample / integrated_reference * 
            abs_reference / abs_sample * 
            (n_sample / n_reference)**2)

def stokes_shift(excitation_max, emission_max):
    return emission_max - excitation_max

def bandgap_from_absorption(wavelength_nm):
    return PLANCK_CONSTANT * SPEED_OF_LIGHT / (wavelength_nm * 1e-9) / ELECTRON_CHARGE

# Utility Functions
def find_nearest_index(array, value):
    return np.abs(array - value).argmin()

def integrate_peak(x, y, x_start, x_end):
    mask = (x >= x_start) & (x <= x_end)
    return np.trapz(y[mask], x[mask])

def derivative_spectrum(x, y):
    return np.gradient(y, x)

def second_derivative_spectrum(x, y):
    dy_dx = np.gradient(y, x)
    return np.gradient(dy_dx, x)
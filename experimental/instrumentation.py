import numpy as np
from scipy import constants

def calculate_instrument_response(signal, impulse_response):
    """Calculate instrument response given an impulse response."""
    response = np.convolve(signal, impulse_response, mode='full')
    return response[:len(signal)]

def calibrate_instrument(data, calibration_factor):
    """Calibrate instrument data using calibration factor."""
    return data * calibration_factor

def calculate_signal_to_noise_ratio(signal, noise):
    """Calculate the Signal-to-Noise Ratio (SNR)."""
    signal_power = np.mean(signal**2)
    noise_power = np.mean(noise**2)
    return 10 * np.log10(signal_power / noise_power)

def characterize_frequency_response(frequencies, response):
    """Characterize frequency response of an instrument."""
    magnitude = 20 * np.log10(np.abs(response))
    phase = np.angle(response, deg=True)
    return magnitude, phase

def filter_signal(data, cutoff_frequency, filter_type='lowpass', order=4):
    """Apply a digital filter to the data."""
    from scipy.signal import butter, filtfilt
    nyquist = 0.5 * constants.c
    normal_cutoff = cutoff_frequency / nyquist
    b, a = butter(order, normal_cutoff, btype=filter_type, analog=False)
    filtered_data = filtfilt(b, a, data)
    return filtered_data

def detect_and_remove_outliers(data):
    """Detect and remove outliers from the dataset."""
    mean = np.mean(data)
    std = np.std(data)
    filtered_data = [x for x in data if (mean - 2 * std) < x < mean + 2 * std]
    return filtered_data

def synchronize_signals(signal1, signal2):
    """Synchronize two signals based on cross-correlation."""
    correlation = np.correlate(signal1, signal2, mode='full')
    delay = np.argmax(correlation) - len(signal1) + 1
    return np.roll(signal2, delay)

def generate_impulse_response(length, peak_position):
    """Generate a simple impulse response signal."""
    impulse_response = np.zeros(length)
    impulse_response[peak_position] = 1
    return impulse_response


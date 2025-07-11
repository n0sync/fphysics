import math
from constants import *

def wave_speed(frequency, wavelength):
    return frequency * wavelength

def wave_equation_displacement(amplitude, wave_number, angular_frequency, position, time, phase=0):
    return amplitude * math.sin(wave_number * position - angular_frequency * time + phase)

def wave_number(wavelength):
    return 2 * PI / wavelength

def wave_intensity(power, area):
    return power / area

def wave_energy_density(amplitude, density, angular_frequency):
    return 0.5 * density * angular_frequency**2 * amplitude**2

def doppler_effect_frequency(source_frequency, source_velocity, observer_velocity, wave_speed):
    return source_frequency * (wave_speed + observer_velocity) / (wave_speed - source_velocity)

def standing_wave_amplitude(amplitude1, amplitude2, wave_number, position):
    return 2 * amplitude1 * amplitude2 * math.sin(wave_number * position)

def beat_frequency(frequency1, frequency2):
    return abs(frequency1 - frequency2)

def wave_interference_amplitude(amplitude1, amplitude2, phase_difference):
    return math.sqrt(amplitude1**2 + amplitude2**2 + 2 * amplitude1 * amplitude2 * math.cos(phase_difference))

def wave_speed_string(tension, linear_density):
    return math.sqrt(tension / linear_density)

def fundamental_frequency_string(length, tension, linear_density):
    return (1 / (2 * length)) * math.sqrt(tension / linear_density)

def acoustic_impedance(density, sound_speed):
    return density * sound_speed

def sound_intensity_pressure(pressure_amplitude, density, sound_speed):
    return (pressure_amplitude**2) / (2 * density * sound_speed)
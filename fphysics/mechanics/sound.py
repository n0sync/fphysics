import math
from constants import *

def sound_intensity_level(intensity, reference_intensity=1e-12):
    return 10 * math.log10(intensity / reference_intensity)

def sound_speed_gas(gamma, pressure, density):
    return math.sqrt(gamma * pressure / density)

def sound_speed_solid(elastic_modulus, density):
    return math.sqrt(elastic_modulus / density)

def organ_pipe_frequency_open(length, wave_speed, harmonic=1):
    return harmonic * wave_speed / (2 * length)

def organ_pipe_frequency_closed(length, wave_speed, harmonic=1):
    return (2 * harmonic - 1) * wave_speed / (4 * length)
